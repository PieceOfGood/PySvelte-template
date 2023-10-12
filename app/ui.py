from aio_dt_protocol import Browser
from aio_dt_protocol import Connection
from aio_dt_protocol import BrowserName
from aio_dt_protocol.domains.fetch.types import EventRequestPaused, RequestPattern
from .functions import extend
from .const import UI_PORT, SOURCES, log
from .types import Source
from json import dumps
from asyncio import sleep, create_task, Task

from base64 import b64encode


async def run_ui(
        dev_mode: bool = False,
        **constants: any
) -> tuple[Task | None, Browser, Connection]:
    """ Запускает браузер и проводит первичную настройку.
    :param dev_mode:    Если True, UI будет перезагружаться
        при обновлении исходников.
    :param constants:   Словарь с константами. В контексте
        UI они будут доступны по указанным именам в верхнем
        регистре. Например:
        constants={
            'some_const': True,
            'some_other_const': 'FALSE'
            'some_integer': 42
        }
        Станут доступны из UI как глобальные константы:
        const SOME_CONST = true;
        const SOME_OTHER_CONST = 'FALSE';
        const SOME_INTEGER = 42;
    """
    # ? URL-адрес, на котором основана работа UI
    # ? Может быть любым валидным значением
    url_name = "svelte-app.magic"
    url = "https://" + url_name
    watch_task: Task | None = None

    # ? Получаем экземпляр браузера и соединения с единственной
    # ? страницей, на которой будет организован UI
    browser, conn = await Browser.run(
        url="",
        app=True,
        debug_port=UI_PORT,
        browser_name=BrowserName.CHROME,
        profile_path="SvelteAppUI",
    )

    # ? Шаблон перехвата всех исходящих запросов
    # ? относящихся к конкретному адресу
    req_pattern = RequestPattern(f"*{url_name}*", requestStage="Request")

    async def src_handler(data: EventRequestPaused) -> None:
        """ Перехватывает исходящие запросы браузера, предоставляя
        ресурсы вместо сервера.
        """
        # ? Если ресурс известен, предоставляем его браузеру
        if path := SOURCES.get(data.request.url.split("/")[-1], None):
            await conn.Fetch.fulfillRequest(
                requestId=data.requestId,
                body=b64encode(path.read_bytes()).decode("utf-8")
            )

        # ? Иначе, выводим полный адрес ресурса
        # ? и продолжаем выполнение
        else:
            log.error(f"Unprocessed resource request: {data.request.url=}")
            await conn.Fetch.continueRequest(requestId=data.requestId)

    # ? Отправляем константы
    if constants:
        await conn.Page.addScriptOnLoad(
            "\n".join([
                f"const {k.upper()} = {dumps(v)};"
                for k, v in constants.items()
            ])
        )

    # ? Регистрируем перехватчики вызовов из JS-контекста
    await extend(conn)

    # ? Разрешаем перехватчик исходящих запросов
    await conn.Fetch.enable([req_pattern], on_pause=src_handler)

    # ? Переходим на триггер-адрес, запускающий загрузку ресурсов
    await conn.Page.navigate(url)

    # ? Наблюдаем за изменением ресурсов
    if dev_mode:
        watch_task = create_task(watch_on_dev(conn))

    return watch_task, browser, conn


async def watch_on_dev(conn: Connection) -> None:
    """ Наблюдает за ресурсами и обновляет UI при изменении.
    """
    sources = [Source(path) for path in SOURCES.values()]

    async def watcher() -> None:
        log.debug("Watcher started")

        while True:
            condition = False
            for src in sources:
                condition |= src.changed()

            if condition:
                await conn.Page.reload(ignoreCache=True)
                log.debug(f"UI updated")

            await sleep(.5)

    watch_task = create_task(watcher())
    await conn.waitForClose()
    watch_task.cancel()
    log.debug("Watcher stopped")

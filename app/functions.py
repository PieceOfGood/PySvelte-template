from aio_dt_protocol import Connection
from .const import log
from .executor import Executor


async def extend(conn: Connection) -> None:
    """ Регистрация хендлеров, вызываемых из JS-контекста
    пользовательского интерфейса.
    """
    ui = Executor(conn)

    async def button_counter(count: int) -> None:
        # ? Выводит в stdout
        log.info(f"JS-counter value: <red>{count}</>")
        # ? И в консоли отладчика браузера
        await ui.exec("console.log", "You click me:", count)

    async def unload() -> None:
        """ Вызывается при перезагрузке UI, переходе на
        другой адрес и закрытии окна в расположении UI.
        Обработчик, вызывающий этот механизм находится в:
        html/jscss/main.js
        """
        log.info("JS-beforeunload")

    # ? Регистрируем слушателей
    await conn.bindFunctions(
        (button_counter, []),
        (unload, []),
    )

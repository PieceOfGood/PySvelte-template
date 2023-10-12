from aio_dt_protocol import Connection
from .const import log


async def extend(conn: Connection) -> None:
    """ Регистрация хендлеров, вызываемых из JS-контекста
    пользовательского интерфейса.
    """

    async def button_counter(count: int) -> None:
        log.info(f"JS-counter value: <red>{count}</>")

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

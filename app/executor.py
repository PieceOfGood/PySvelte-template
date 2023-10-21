from aio_dt_protocol import Connection
# from msgspec.json import encode
from json import dumps


class Executor:

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    async def exec(self, func: str, *data: any) -> None:
        """ Вызывает функцию в UI, передавая ей соответствующие аргументы.
        :param func:     Имя функции, которую нужно вызвать, без скобок.
            Например: "someJavascriptFunctionName"
        :param data:     Любое количество аргументов из простых python-типов.
        """
        # args = ", ".join((encode(d).decode("utf-8") for d in data))
        
        # ? Стандартный сериализатор будет выдавать исключение для
        # ? попыток преобразования `datetime`:
        # ! TypeError: Object of type datetime is not JSON serializable
        args = ", ".join((dumps(d) for d in data))
        await self.conn.extend.injectJS(f"{func}({args})")

from aio_dt_protocol import Connection
# from msgspec.json import encode
from json import dumps


class Executor:

    def __init__(self, conn: Connection) -> None:
        self.conn = conn

    async def exec(self, func: str, *data: any) -> any:
        """ Вызывает функцию в UI, передавая ей соответствующие аргументы и
        возвращает результат, если функция его так же возвращает.
        
        Важно! Функция должна возвращать простой тип, или используйте JSON.
        
        :param func:     Имя функции, которую нужно вызвать, без скобок.
            Например: "someJavascriptFunctionName", или "console.log"
        :param data:     Любое количество аргументов из простых python-типов.
        :return:         Возвращает результат вызова функции. 
        """
        # args = ", ".join((encode(d).decode("utf-8") for d in data))
        
        # ? Стандартный сериализатор будет выдавать исключение для
        # ? попыток преобразования `datetime`:
        # ! TypeError: Object of type datetime is not JSON serializable
        args = ", ".join((dumps(d) for d in data))
        return await self.conn.extend.injectJS(f"{func}({args})")

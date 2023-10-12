from pathlib import Path


class Source:
    """ Реализует простую обёртку для файла,
    призванную отвечать за проверку изменения.
    """
    def __init__(self, path: Path) -> None:
        self.path = path
        self.__last_mtime = path.stat().st_mtime

    def changed(self) -> bool:
        if (condition := self.path.stat().st_mtime != self.__last_mtime):
            self.__last_mtime = self.path.stat().st_mtime
        return condition

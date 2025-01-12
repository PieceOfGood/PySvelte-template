from pathlib import Path
from loguru import logger


ROOT_DIR = Path(__file__).parent.parent
HTML_DIR = ROOT_DIR / "html"
JSCSS_DIR = HTML_DIR / "jscss"
HTML_SRC_DIR = HTML_DIR / "src"

INDEX_HTML = HTML_DIR / "index.html"

# ? Список путей к ресурсам, которые будет запрашивать браузер
SOURCES: dict[str, Path] = {
    "": HTML_DIR / "index.html",
    "MuseoSansCyrl-300.woff2": HTML_SRC_DIR / "MuseoSansCyrl-300.woff2",
    "favicon.png": HTML_SRC_DIR / "favicon.png",
    "main-app.css": JSCSS_DIR / "main-app.css",
    "main-app.js": JSCSS_DIR / "main-app.js",
    "main.css": JSCSS_DIR / "main.css",
    "main.js": JSCSS_DIR / "main.js",
}

UI_PORT = 9234

log = logger.opt(colors=True)

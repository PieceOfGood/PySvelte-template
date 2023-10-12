import asyncio
from app import run_ui
from app.const import log


async def main() -> None:

    watch_task, browser, conn = await run_ui(
        dev_mode=True,
        some_const=True,
        some_other_const="FALSE",
        some_integer=42
    )
    log.success("UI started")
    await conn.waitForClose()
    log.success("UI stopped")

    if watch_task:
        await watch_task


if __name__ == "__main__":
    asyncio.run(main())

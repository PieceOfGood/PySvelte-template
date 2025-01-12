@echo off

rem Переключает кодировку вывода командной строки
rem на используемую Windows, для поддержки
rem кириллицы, если эта кодировка не используется
rem по умолчанию.
for /f "tokens=2 delims=:" %%a in ('chcp') do set /a codepage=%%a
if not %codepage% == 65001 (
	chcp 65001
)

echo Создание виртуального окружения ...
py -m venv venv

echo Активация виртуального окружения ...
call venv\Scripts\activate.bat

echo Upgrade pip ...
py -m pip install --upgrade pip

echo Установка зависимостей ...
pip install -r requirements.txt

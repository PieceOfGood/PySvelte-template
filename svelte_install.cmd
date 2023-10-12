@echo off

rem Устанавливает Svelte и копирует файл конфигурации
rem с актуальными настройками

for /f "tokens=2 delims=:" %%a in ('chcp') do set /a codepage=%%a
if not %codepage% == 65001 (
	chcp 65001
)

echo Создание шаблона Svelte ...
call npx degit sveltejs/template svelte

cd svelte

echo Установка ...
call npm install -D svelte-preprocess

echo Замена файла конфигурации ...
del rollup.config.js
cd ..
copy svelte_src\rollup.config.js svelte

echo Завершено.

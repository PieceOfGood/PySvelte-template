@echo off

rem Устанавливает Svelte и копирует файл конфигурации
rem с актуальными настройками

for /f "tokens=2 delims=:" %%a in ('chcp') do set /a codepage=%%a
if not %codepage% == 65001 (
	chcp 65001
)

echo Создание шаблона Svelte ...
call npm create vite@latest svelte -- --template svelte

cd svelte

echo Установка ...
call npm install

set FOLDERS=.vscode public
set RM_FILES=.gitignore index.html README.md vite.config.js src\lib\Counter.svelte src\main.js src\app.css

echo Удаление ненужных файлов и директорий ...
for %%f in (%FOLDERS%) do (
    if exist %%f (
        rmdir /S /Q %%f
    )
)

for %%f in (%RM_FILES%) do (
    if exist %%f (
        del %%f
    )
)

cd ..

echo Копирование исходников начального проекта ...

copy svelte_src\vite.config.js svelte

copy svelte_src\src\main-app.js svelte\src
copy svelte_src\src\main-app-global.css svelte\src
copy svelte_src\src\App.svelte svelte\src

copy svelte_src\src\lib\PyButton.svelte svelte\src\lib

echo Завершено.

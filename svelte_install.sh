#!/bin/bash

# Устанавливает Svelte и копирует файл конфигурации
# с актуальными настройками

echo Создание шаблона Svelte ...
npx degit sveltejs/template svelte

cd svelte

echo Установка ...
npm install -D svelte-preprocess

echo Замена файла конфигурации ...
rm -f rollup.config.js
cd ..
cp svelte_src/rollup.config.js svelte

echo Завершено.
# Data Processing Module

## Описание
Данный модуль предназначен для обработки данных в виде списка словарей. 
Функция filter_by_state  фильтрует данные по состоянию (`state`), 
Функция sort_by_date  сортирует данные по дате (`date`).

## Установка
1. Скачайте или клонируйте проект:
##   git clone https://github.com/nipigaz/nipigaz_homeworks/pull/3

## Примеры данных
Модуль включает два набора данных для тестирования:
data_state: Список операций с разными статусами.
data_date: Список операций с разными датами для демонстрации сортировки.

## Аннотации типов
Используются List и Dict из модуля typing для совместимости с Python 3.8+.

## Примеры входных данных и вывода
Данные для тестирования уже включены в модуль. Чтобы запустить примеры, выполните:
python processing.py
# Калькуляторы
## Возьми под контроль свои калории и расходы :)

Проект содержит два простых калькулятора(CaloriesCalculator/CashCalculator) для подсчета остатка калорий/денежных средств на день либо считает расход калорий/денежных средств за прошедшие 7 дней.

## Возможности
- Подсчета остатка калорий/денежных средств на день
- Подсчет расходов калорий/денежных средств за прошедшие 7 дней
- Денежный калькулятор пересчитывает остаток по курсу rub/eur/usd

## Особенности
- Данные передаваемые в калькулятор описываются классом Record
>class Record:</br>
>    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"""Класс используемый для хранения данных.</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Основное применение - хранения информации о расходах на конктретную дату</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--------</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Атрибуты</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;amount : float</br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;данные о расходах</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment : str</br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;комментарии к записи</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;date : str, optional (по умолчанию None)</br>
>       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;дата расходов</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--------</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Методы</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;не имеете публичных методов</br>
>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"""</br>
- Избыточное комментирование

## Цель
- Освоение ООП;
- Написать чистый и красивый код в соответствии с PEP8;
- Реализовать свой первый учебный проект;
- Выработать привычку комментирования своего кода.

## Tech

- [Python](https://www.python.org) - Python is free and easy to learn if you know where to start!.

## Installation

- Склонировать репозиторий;
- Импортировать нужный калькулятор и класс Record;
- Создать объект данного калькулятора и установить дневной лимит;
- Создать объект Record с данными о расходах;
- Использовать методы калькуляторы.
```sh
calculator = CaloriesCalculator(limit=1500)
record = Record(amout=100, comment='шаурма')
calculator.add_record(record)
calculator.get_week_stats()  # 100.00
calculator.get_calories_remained()  # Cегодня можно съесть....
```

## License

MIT
**Free Software, Hell Yeah!**

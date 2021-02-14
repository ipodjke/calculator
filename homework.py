import datetime as dt
from typing import Optional

from custom_exceptions import WrongDataFormat
from support_class_from_convert import ConvertNumber


class Calculator:
    """Класс используемый для создания калькуляторов расходов.

    --------
    Note
        - Для коррктной работы необходими импортировать ConvertNumber, datetime
        - Приводит тип перемоной limit к float. В случае невозможости
        приведения к типу генерирует исключение ValueError, TypeError
        и присвает переменой 0
    --------
    Атрибуты
    limit : float
        лимимт расходов
    records : list
        хранит записи о расходах
    --------
    Методы
    add_record()
        добавляет запись в records
    get_today_stats()
        считает расходы за сегодня
    get_week_stats()
        считает расходы за прошедшие 7 дней
    """
    def __init__(self, limit: float) -> None:
        """Устанавливает атрибуты и осуществляет приведение типов.

        Приводит тип перемоной limit к float. В случае невозможости
        приведения к типу генерирует исключение ValueError, TypeError
        и присвает переменой 0
        --------
        Методы
        limit : float
            лимимт расходов
        records : list
            хранит записи о расходах
        """
        self.number_converter = ConvertNumber()
        self.limit = self.number_converter.convert_to_float(limit)
        self.records = []

    def add_record(self, operation_record: object) -> None:
        """Добавляет запись в список records.

        Параметры
        operation_record : object
            запись для добавления в список records
        --------
        Возвращаемое значение
        None
        """
        self.records.append(operation_record)

    def get_today_stats(self) -> float:
        """Считает расходы за сегодня из списка records.

        Линейно проходит список records, ищет записи с
        сегоднящней датой и суммирует их значения
        --------
        Возвращаемое значение
        float
        """
        today = dt.date.today()
        expenses = [record.amount
                    for record in self.records
                    if record.date == today]
        return float(sum(expenses))

    def get_week_stats(self) -> float:
        """Считает расходы за прошедшие 7 дней из списка records.

        Линейно проходит список records, ищет записи с
        датой за прошедшие 7 дней и суммирует их значения
        --------
        Возвращаемое значение
        float
        """
        today = dt.date.today()
        week_offset = dt.timedelta(days=6)
        first_day_week = today - week_offset
        expenses = [record.amount
                    for record in self.records
                    if first_day_week <= record.date
                    and record.date <= today]
        return float(sum(expenses))


class CaloriesCalculator(Calculator):
    """Калькулятор для подсчета расхода каллорий.

    Являеся наследником класса Calculator. Не переопределяет и не расширяет
    поведение родительского класса
    --------
    Методы
    get_calories_remained()
        определяет остаток калорий на день
    """
    def get_calories_remained(self) -> str:
        """определяет остаток калорий на день

        Основное применени - определить остаток калорий и сформировать
        сообщение
        --------
        Возвращаемое значение
        str
        """
        calories_left = self.limit - self.get_today_stats()
        if calories_left > 0:
            return (f'Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью не более '
                    f'{calories_left:.0f} кКал')
        return 'Хватит есть!'


class CashCalculator(Calculator):
    """Калькулятор для подсчета расхода денег.

    Являеся наследником класса Calculator. Не переопределяет и не расширяет
    поведение родительского класса. Определяет констаны класса
    (USD_RATE, EURO_RATE), хранящие курсы валют. Хранит курс валют и
    обеспечивает перевод в указаную валюту
    --------
    Note
        В случае передачи отсутсвующей в классее валюты подсчет осуществляется
        в условной валюте сопостовимой с рублем
    --------
    Методы
    get_today_cash_remained()
        определяет остаток денег на день и переводит в указанную валюту
    """
    USD_RATE = 60.00
    EURO_RATE = 70.00
    __currency_rate = {
        'rub': [1, 'руб'],
        'usd': [USD_RATE, 'USD'],
        'eur': [EURO_RATE, 'Euro']
    }

    def get_today_cash_remained(self, currency: str) -> str:
        """Определяет остаток денег на день и переводит в указанную валюту.

        Результатом работы метода является строка зависющая от езультатов
        подсчета остатка денег. В случае передачи отсутсвующей в классе
        валюты подсчет осуществляется в условной валюте сопостовимой с рублем
        --------
        Параметры
        currency : str
            наименование валюты
        --------
        Возвращаемое значение
        str
        """
        cash_left = self.limit - self.get_today_stats()
        try:
            money_in_currency = cash_left / self.__currency_rate[currency][0]
            money_in_currency = abs(money_in_currency)
            phrase = (f'{money_in_currency:.2f} '
                      f'{self.__currency_rate[currency][1]}')
        except (KeyError, ZeroDivisionError):
            phrase = f'{cash_left}'
        if cash_left > 0:
            return f'На сегодня осталось {phrase}'
        if cash_left < 0:
            return f'Денег нет, держись: твой долг - {phrase}'
        return 'Денег нет, держись'


class Record:
    """Класс используемый для хранения данных.

    Основное применени - хранения информации о расходах на конктретную дату
    --------
    Note
        - Для коррктной работы необходими импортировать ConvertNumber,
        WrongDataFormat, datetime, typing
        - Приводит тип перемоной amount к float. В случае невозможости
        приведения к типу генерирует исключение ValueError, TypeError
        и присвает переменой 0
        - По умолчанию присваивает переменой date значение None
        - Приводит тип переменой date к datetime. В случае невозможости
        приведения к типу генерирует исключение WrongDataFormat и присвает
        переменой сегоднящнюю дату
    --------
    Атрибуты
    amount : float
        данные о расходах
    comment : str
        комментарии к записи
    date : str, optional (по умолчанию None)
        дата рассходов
    --------
    Методы
    не имеете публичных методов
    """
    def __init__(self,
                 amount: float,
                 comment: str,
                 date: Optional[str] = None) -> None:
        """Устанавливает и выполняет преобразование типов данных.

        Атрибуты
        amount : float
            данные о расходах
        comment : str
            комментарии к записи
        date : str, optional (по умолчанию None)
            дата рассходов
        """
        self.number_converter = ConvertNumber()
        self.amount = self.number_converter.convert_to_float(amount)
        self.comment = str(comment)
        try:
            self.date = self.__convert_to_date_frame(date)
        except WrongDataFormat:
            self.date = dt.date.today()

    def __convert_to_date_frame(self, date: str) -> object:
        """Преобразовывает дату в тип datetime"""
        if not isinstance(date, str):
            raise WrongDataFormat
        date_format = self.__get_date_format(date)
        return dt.datetime.strptime(date, date_format).date()

    def __get_date_format(self, date: str) -> str:
        """Получает шаблон(формат) даты"""
        date = date.strip()
        separators = [char for char in date if not char.isalnum()]
        unique_separators = set(separators)
        if len(unique_separators) != 1:
            raise WrongDataFormat
        separator = unique_separators.pop()
        parse_date = date.split(separator)
        month = int(parse_date[1])
        if (len(parse_date[2]) == 4
                and int(parse_date[0]) < 32 and month < 12):
            return f'%d{separator}%m{separator}%Y'
        if (len(parse_date[0]) == 4
                and int(parse_date[2]) < 32 and month < 12):
            return f'%Y{separator}%m{separator}%d'
        raise WrongDataFormat

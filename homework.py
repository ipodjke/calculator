import datetime as dt


class Calculator:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, operation_record: object) -> None:
        self.records.append(operation_record)

    def get_today_stats(self) -> float:
        today = dt.datetime.now().date()
        expenses = [record.amount
                    for record in self.records
                    if record.date == today]
        return float(sum(expenses))

    def get_week_stats(self) -> float:
        today = dt.datetime.now().date()
        week_offset = dt.timedelta(days=7)
        first_day_week = today - week_offset
        expenses = [record.amount
                    for record in self.records
                    if first_day_week <= record.date
                    and record.date <= today]
        return float(sum(expenses))


class CaloriesCalculator(Calculator):
    def get_calories_remained(self) -> str:
        calories_left = self.limit - self.get_today_stats()
        if calories_left > 0:
            return (f'Сегодня можно съесть что-нибудь ещё,'
                    f' но с общей калорийностью не более '
                    f'{calories_left:.0f} кКал')
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 60.00
    EURO_RATE = 70.00
    __currency_rate = {
        'rub': [1, 'руб'],
        'usd': [USD_RATE, 'USD'],
        'eur': [EURO_RATE, 'Euro']
    }

    def get_today_cash_remained(self, currency: str) -> str:
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
        elif cash_left < 0:
            return f'Денег нет, держись: твой долг - {phrase}'
        else:
            return 'Денег нет, держись'


class Record:
    def __init__(self,
                 amount: float,
                 comment: str,
                 date: str = dt.datetime.now().date()) -> None:
        try:
            self.amount = float(amount)
        except (ValueError, TypeError):
            self.amount = 0
        self.comment = str(comment)
        try:
            self.date = self.__convert_to_date_frame(date)
        except WrongDataFormat:
            self.date = dt.datetime.now().date()

    def __convert_to_date_frame(self, date: str) -> object:
        if isinstance(date, str):
            date_format = self.__get_date_format(date)
            return dt.datetime.strptime(date, date_format).date()
        else:
            raise WrongDataFormat

    def __get_date_format(self, date: str) -> str:
        date = date.strip()
        separators = [char for char in date if not char.isalnum()]
        unique_separators = set(separators)
        if len(unique_separators) == 1:
            separator = unique_separators.pop()
            parse_date = date.split(separator)
            month = int(parse_date[1])
            if (len(parse_date[2]) == 4
                    and int(parse_date[0]) < 32 and month < 12):
                return f'%d{separator}%m{separator}%Y'
            elif (len(parse_date[0]) == 4
                    and int(parse_date[2]) < 32 and month < 12):
                return f'%Y{separator}%m{separator}%d'
        raise WrongDataFormat


class WrongDataFormat(Exception):
    pass


if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=900, comment='Серёге за обед'))
    cash_calculator.add_record(Record(amount=3000,
                                      comment='бар в Танин др',
                                      date='08.11.2019'))
    print(cash_calculator.get_today_cash_remained('eur'))

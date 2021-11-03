class ConvertNumber:
    """Класс для пробразования чисел.

    Основное применение - преобразование типов чисел
    --------
    Note:
        - Приводит тип перемоной number к float. В случае невозможости
        приведения к типу генерирует исключение ValueError, TypeError
        и присвает переменой 0
    --------
    Методы:
        convert_to_float(number)
            приводит число к типу float и возвращает его,
            в случае невозможности приведения генерируется исключение
            и возвращается 0
    """
    def __init__(self) -> None:
        """Заглушка для дальнейшего расширения"""
        pass

    def convert_to_float(self, number: (int, float)) -> float:
        """Приводит тип числа к float

        В случае невозможости приведения к типу генерирует
        исключение ValueError, TypeError и присвает переменой 0
        --------
        Параметры:
            number : (int, float)
                число для приведения типа
        --------
        Возвращаемое значение:
            float
        """
        if isinstance(number, float):
            return number
        try:
            return float(number)
        except (ValueError, TypeError):
            return 0

def do_it(param_1: int, param_2: str, param_3: float) -> float:
    """
        Эта функция берет первые два параметра, складывает их и делит на третий.
		Результат печатается в консоль.
		Параметры должны быть числовыми.
    """
    result = (param_1 + param_2) * param_3
    return result
    


x = do_it(1, 2, 3.5)
y = x - 1.3
print(y)
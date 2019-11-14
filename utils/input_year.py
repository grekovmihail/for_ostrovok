__all__ = (
    'input_year',
)


def input_year(now):
    print("Введите год")
    try:
        year = int(input())
        if (year > 2013) & (year <= now.year):
            return year
        else:
            print("По этому году нет обоев")
            return (input_year(now))

    except:
        print("Неверный ввод")
        return (input_year(now))

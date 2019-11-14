__all__ = (
    'input_month',
)


def input_month():
    print("Введите номер месяца")
    try:
        month = int(input()) - 1
        months = [
            "january",
            "febuary",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december"]
        return month, months[month]
    except:
        print("Неверный ввод")
        return (input_month())

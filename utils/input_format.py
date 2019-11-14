__all__ = (
    'input_format',
)


def input_format():
    example_format = ["1024x768", "1024x1024", "1152x864", "1280x720", "1280x800", "1280x960", "1280x1024", "1366x768", "1440x900", "1440x1050", "1600x1200", "1680x1050", "1680x1200", "1920x1080", "1920x1200", "1920x1440", "2560x1440"]
    print(
        " Введите формат, пожалуйста  (" + str(example_format) + ")"
    )
    format = input()
    #B = list(filter(lambda i: i  == format, example_format))
    #print(B)
    if (list(filter(lambda i: i  == format, example_format))):
        return format
    else:
        print("Неверный ввод")
        return (input_format())

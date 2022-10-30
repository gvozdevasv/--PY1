def get_count_char(str_):
    counter = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for symbol in str_:
        if symbol.isalpha():
            if symbol in counter:
                counter[symbol] = counter[symbol] + 1
            else:
                counter[symbol] = 1
    return counter


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_summ(one, two, delimeter='&'):
    return(f'{one}{delimeter}{two}')
one = str(input('Введите первый параметр: '))
two = str(input('Введите второй параметр: '))
stroke = get_summ(one, two)
print(stroke.upper())
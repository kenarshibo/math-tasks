def total(num):  # считаем сколько чисел в числе
    total_nums = 0
    point = False

    for letters in num:
        total_nums += 1

        if letters == '.':
            point = True

    if point:
        total_nums -= 1  # точка
    return total_nums


def backwards_part(num, tot_num):  # Находим часть от числа наоборот
    backwards = 0

    for i in range(tot_num):
        backwards += num % 10 * (10 ** (tot_num - 1))
        num //= 10
        tot_num -= 1
    return backwards


def float_nums(num):  # Находим вещественную часть
    float_num = ''
    sign_point = 0
    for letters in num:

        if sign_point == 1:
            float_num += letters

        if letters == '.':
            sign_point += 1
    return int(float_num)


# первое число
first_num = float(input('Enter the first num: '))
# Делаем перевертнутой целую часть:
whole_first_num = int(first_num)  # делаем число целым
total_nums = total(str(whole_first_num))  # узнаем сколько чисел в целой части
backward_first_part = backwards_part(whole_first_num, total_nums)  # Получаем перевернутую, целую часть
# делаем перевертнутой дробную часть:
total_float_nums = total(str(first_num)) - total_nums  # Кол-во цифр в вещественной части
float_num = float_nums(str(first_num))  # вещественная часть
backward_first_part2 = backwards_part(float_num, total_float_nums)  # Вещественная часть наоборот
# Результат:
result1 = backward_first_part + backward_first_part2 / (10 ** total_float_nums)
# второе число:
second_num = float(input('Enter the second num: '))
whole_sec_num = int(second_num)  # делаем число целым
total_nums = total(str(whole_sec_num))  # узнаем сколько чисел в целой части
backward_sec_part = backwards_part(whole_sec_num, total_nums)  # Получаем перевернутую, целую часть
# делаем перевертнутой дробную часть:
total_float_nums = total(str(second_num)) - total_nums  # Кол-во цифр в вещественной части
float_num = float_nums(str(second_num))  # вещественная часть
backward_sec_part2 = backwards_part(float_num, total_float_nums)  # Вещественная часть наоборот
# Результат:
result2 = backward_sec_part + backward_sec_part2 / (10 ** total_float_nums)
print(f'\n{result1}- the first backward number')
print(result2, '- the second backward number')
print(f'\nThe ammount of this nums is {result1 + result2}')

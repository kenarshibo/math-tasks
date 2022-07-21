def scary_years(start, stop):
    print(f'Годы от {start} до {stop} с тремя одинаковыми символами:')

    for years in range(start, stop):
        round = 0
        first_digit_score = 0
        second_digit_score = 0
        first_digit = years // 1000
        sec_digit = years // 100 % 10

        for i in str(years):

            if int(i) == int(first_digit):
                first_digit = i
                first_digit_score += 1

            elif int(i) == int(sec_digit):
                sec_digit = i
                second_digit_score += 1

        max_score = max(first_digit_score, second_digit_score)

        if max_score > 2:
            print(years)

f_year = int(input('Введите превый год: '))
s_year = int(input('Введите второй год: '))
scary_years(f_year, s_year)
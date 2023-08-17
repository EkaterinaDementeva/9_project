import re

with open("C:/Users/Admin/Documents/Maya/Уроки/9 неделя август/1.txt") as file:
    for item in file:
        print('была строка: ', item)
        a = item.strip("\n").strip()
        answer = ''

        if a[0] == '+' or a[0] == '-':
            answer = a[0]
            a = a[1:]
        if re.fullmatch("\d{1,100000}", a):
            answer = answer + a
        else:
            continue
        if int(answer) == 0 and answer not in ['0', '+0', '-0']:
            continue
        print(answer)

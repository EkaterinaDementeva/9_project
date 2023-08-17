# 9_project
Cкрипт, который пройдется по каждой строке этого файла, найдет числа, поподающие под определенные условия, и выводит эти числа (программа должна вывести не отформатированое число, а то как оно написано в данной строке, т.е. "   03" без пробелов и нуля это 3, оно попадает под условия, а значит будет распечатана строка "   03").



Условие задачи:

Используйте генератор и регулярные выражения
Путь к файлу в скрипте должен быть  указан явно
Cкрипт должен распечатать числа, которые:
Имеют значение в диапазоне от -1000000 до +1000000 (включительно. Т.е. строка "1000000" будет распечатана)
имеют знак +, - или вообще никакого знака перед числом
Знак перед числом может быть только один, число ++3 или ---7 распечатывать нельзя
Если строка имеет пробелы перед числом, или после - удалить пробелы и уже потом проверить число
Если число это ноль 0 - то число можно распечатать, если несколько нулей подряд 00000 - то не выводить его
Если это число 03 или 0003 и т.д. (т.е. перед числом какое-то количество нулей) - то такое число также должно печататься
В числе не может быть никаких специальных знаков (. ? ! , и т.д.), пробелов или букв
Число должно быть именно число, слово "five" не должно быть распечатано
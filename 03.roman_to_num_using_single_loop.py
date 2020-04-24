# Write a Python class to convert an integer to a roman numeral.


class Py_solution:

    def roman_to_int(self, num):
        # make a list of major number
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        # make a list of major roman number, all roman numbers can be made using these
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        # declare variable which contain the output
        number = 0
        # convert the input roman number into list
        num = [char for char in num]
        print('after split -->', num)
        # single roman number like 'I'  can be easily converted into number
        # but two character roman numbers like 'IV', 'IX' need some special approach
        # after splitting each char in input roman number
        for i in range(1, len(num)-1):
            # print('jjj', j)
            if num[i-1] == 'C' and num[i] == 'M':
                temp = num[i-1] + num[i]
                num.insert(i-1, temp)
                print('after insertion', num)
                num.pop(i)
                num.pop(i)
                print('num', num)
                continue
            elif num[i-1] == 'X' and num[i] == 'C':
                temp = num[i-1] + num[i]
                num.insert(i-1, temp)
                print('after insertion', num)
                num.pop(i)
                num.pop(i)
                print('num', num)
                continue
            elif num[i-1] == 'X' and num[i] == 'L':
                temp = num[i - 1] + num[i]
                num.insert(i - 1, temp)
                print('after insertion', num)
                num.pop(i)
                num.pop(i)
                print('num', num)
                continue
            elif num[i-1] == 'I' and num[i] == 'X':
                temp = num[i - 1] + num[i]
                num.insert(i - 1, temp)
                print('after insertion', num)
                num.pop(i)
                num.pop(i)
                print('num', num)
                continue
            elif num[i-1] == 'I' and num[i-1] == 'V':
                temp = num[i - 1] + num[i]
                num.insert(i - 1, temp)
                print('after insertion', num)
                num.pop(i)
                num.pop(i)
                print('num', num)
                continue
            elif num[i-1] == 'C' and num[i] == 'D':
                temp = num[i - 1] + num[i]
                num.insert(i - 1, temp)
                print('after insertion', num)
                num.pop(i)
                num.pop(i)
                print('num', num)
                continue
            else:
                continue

        print('Roman number after splitting = ', num)
        print('Original input roman num-->', "".join(num))
        for i in num:
            temp = syb.index(i)
            number += val[temp]

        return "number for roman number is {}".format(number)


find_roman = Py_solution()
print(find_roman.roman_to_int('LXV'))
print(find_roman.roman_to_int('MXCIX'))
print(find_roman.roman_to_int('MMX'))
print(find_roman.roman_to_int('LXXVIII'))
print(find_roman.roman_to_int('MV'))
print(find_roman.roman_to_int('DCCCVII'))
print(find_roman.roman_to_int('MMMDLXXXVII'))
print(find_roman.roman_to_int('MCXXI'))

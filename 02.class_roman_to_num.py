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
        # after splitting each char in input roman number, join characters like 'IV', 'IX
        for i in range(len(num)):
            # print('iii', i)
            for j in range(i+1, len(num)):
                # print('jjj', j)
                # join 'CM'
                if num[i] == 'C' and num[j] == 'M':
                    temp = num[i] + num[j]
                    num.insert(i, temp)
                    print('after insertion', num)
                    num.pop(i+1)
                    num.pop(i+1)
                    print('num', num)
                    # break the j loop
                    break
                # join 'XC'
                elif num[i] == 'X' and num[i+1] == 'C':
                    temp = num[i] + num[i+1]
                    num.insert(i, temp)
                    print('after insertion', num)
                    num.pop(i+1)
                    num.pop(i+1)
                    print('num', num)
                    break
                # join 'XL'
                elif num[i] == 'X' and num[j] == 'L':
                    temp = num[i] + num[j]
                    num.insert(i, temp)
                    print('after insertion', num)
                    num.pop(i + 1)
                    num.pop(i + 1)
                    print('num', num)
                    break
                # join 'IX'
                elif num[i] == 'I' and num[j] == 'X':
                    temp = num[i] + num[j]
                    num.insert(i, temp)
                    print('after insertion', num)
                    num.pop(i + 1)
                    num.pop(i + 1)
                    print('num', num)
                    break
                # join 'IV'
                elif num[i] == 'I' and num[j] == 'V':
                    temp = num[i] + num[j]
                    num.insert(i, temp)
                    print('after insertion', num)
                    num.pop(i + 1)
                    num.pop(i + 1)
                    print('num', num)
                    break
                # join 'CD'
                elif num[i] == 'C' and num[j] == 'D':
                    temp = num[i] + num[j]
                    num.insert(i, temp)
                    print('after insertion', num)
                    num.pop(i + 1)
                    num.pop(i + 1)
                    print('num', num)
                    break
                # else break the loop
                else:
                    break

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



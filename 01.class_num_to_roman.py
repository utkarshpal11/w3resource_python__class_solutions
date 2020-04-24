# Write a Python class to convert an integer to a roman numeral.


class py_solution:

    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while num > 0:
            print('num == ', num)
            print('iii -->', i)
            for _ in range(num // val[i]):
                print('__', _)
                print('i == ', i)
                roman_num += syb[i]
                num -= val[i]
                print('num2 == ', num)
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print('\n')
print(py_solution().int_to_Roman(4000))
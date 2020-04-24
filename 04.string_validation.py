"""Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)",
"({[)]" and "{{{" are invalid.
"""


class String_validation:

    def input_string(self, string):
        stack, pchar = [], {'(': ')', '[': ']', '{': '}'}
        print('stack after declaration: ', stack)
        print('pchar after declaration:', pchar)
        for i in string:
            print('IIII', i)
            print('stack', stack)
            if i in pchar:
                stack.append(i)
                print('i{}, STACK{}'.format(i, stack))
            elif len(stack) == 0 or pchar[stack.pop()] != i:
                return False
        return len(stack) == 0


s = String_validation()
print(s.input_string('()[]{}'))
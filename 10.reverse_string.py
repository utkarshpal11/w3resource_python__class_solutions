# Write a Python class to reverse a string word by word.


class Reverse:

    def input(self, string):
        previous = string.split()
        previous.reverse()
        previous = ' '.join(previous)
        return print(previous)


r = Reverse()
r.input('hello dear, how are you?')
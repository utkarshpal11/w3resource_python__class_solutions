# Write a Python class which has two methods get_String and print_String. get_String
# accept a string from the user and print_String print the string in upper case.

class String_methods:

    def __init__(self):         # if no value is defined inside, then no argument needs to be passed
        self.string = ''        # instance variable as empty string

    def get_String(self):
        self.string = input("Enter the string: ")

    def print_String(self):
        return print(self.string.upper())


s = String_methods()
s.get_String()
s.print_String()
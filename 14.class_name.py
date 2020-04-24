# Write a Python program to get the class name of an instance in Python.


class Name:

    def __init__(self):
        self.name = 'Name'

    def print_class_name(self):
        return self.name


n = Name()
print(n.print_class_name())


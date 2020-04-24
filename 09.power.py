# Write a Python class to implement pow(x, n).


class Power:

    def power(self, x, n):

        return print("power {x} to {n} is {output}".format(x=x, n=n, output=x**n))

p = Power()
p.power(7, 3)
p.power(7, -3)
p.power(7, 0)
p.power(7, 10)
p.power(-6, 3)
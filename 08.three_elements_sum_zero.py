# Write a Python class to find the three elements that sum to zero from a set of n real numbers.
# in this approach i'll use list index for iteration

class three_elements_sum_zero:

    def input_target(self, target=0):

        l = [-10, 3, 4, 0, 6, -13, -7, 20, -67, 21, 34, 46]
        print(len(l))
        output = []
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                for k in range(j+1, len(l)):
                    if l[i] + l[j] + l[k] == 0:
                        output.append((l[i], l[j], l[k]))
                    else:
                        continue
        if len(output) != 0:
            return print("output:", output)
        return print("no elements found")


o = three_elements_sum_zero()
o.input_target()
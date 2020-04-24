# Write a Python class to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number.

class find_target_sum_no:

    def input_target_no(self, target):
        # target = 50
        l = [10, 20, 30, 40, 50, 60, 70]
        for i in range(len(l)):
            for j in range(len(l)):
                if l[i] + l[j] == target:
                    return print(l.index(l[i]), l.index(l[j]))
                else:
                    continue
        return print("No pair available for {}".format(target))


f = find_target_sum_no()
f.input_target_no(121)
f.input_target_no(120)
f.input_target_no(30)
f.input_target_no(90)
f.input_target_no(50)
f.input_target_no(100)

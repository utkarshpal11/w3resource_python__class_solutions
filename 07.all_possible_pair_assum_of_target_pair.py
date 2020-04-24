# Write a Python program to find all pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number.


class all_possible_pair:

    def input_number(self, target):
        list_of_no = [100, 20, 40, 50, 70, 60, 30, 10, 90, 80]
        list_of_all_pairs = []

        for i in range(len(list_of_no)):
            for j in range(i+1, len(list_of_no)):
                if list_of_no[i] + list_of_no[j] == target:
                    list_of_all_pairs.append((list_of_no.index(list_of_no[i]), list_of_no.index(list_of_no[j])))
                else:
                    continue

        if len(list_of_all_pairs) != 0:
            return print(list_of_all_pairs)

        return print("no pair available for {}".format(target))


name = all_possible_pair()
name.input_number(100)
name.input_number(170)
name.input_number(70)
name.input_number(10)
name.input_number(140)
name.input_number(190)
name.input_number(90)

name.input_number(45)
name.input_number(54)
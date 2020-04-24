# Write a Python class to get all possible unique subsets from a set of distinct integers


class Possible_subsets:

    def input_data(self, l):
        out = []
        out.append([])
        print(l)
        temp = []
        for i in range(len(l)):
            if l[i] not in temp:
                temp.append(l[i])
                pass
                if l[i+1] not in temp:
                    temp.append(l[i+1])
                    out.append(temp)
                    continue
            temp = []
        return out


c = Possible_subsets()
print(c.input_data([4, 5, 6, 7]))


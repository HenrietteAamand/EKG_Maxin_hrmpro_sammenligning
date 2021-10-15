
class correction_class:
    def __init__(self):
        pass
    def correct_3_lists(self, list_a, list_b, list_c):
        dictionary= {}
        lengths = []
        dictionary[len(list_a)] = list_a
        dictionary[len(list_b)] = list_b
        dictionary[len(list_c)] = list_c

        lengths.append(len(list_a))
        lengths.append(len(list_b))
        lengths.append(len(list_c))

        print(len(dictionary[lengths[len(lengths)-1]]))
        print(len(dictionary[lengths[len(lengths)-2]]))
        print(len(dictionary[lengths[len(lengths)-3]]))

        lengths.sort()

        i = 1
        for element in dictionary:
            while(len(dictionary[lengths[len(lengths)-1]]) > len(dictionary[lengths[len(lengths)-i]])):
                dictionary[lengths[len(lengths)-i]].append(60)
            i += 1
        corrected_length = [list_a, list_b, list_c]

        return corrected_length



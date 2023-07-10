from itertools import combinations_with_replacement
from collections import Counter


class SemigroupElement:
    def __init__(self, multiset, k):
        self.multiset = multiset
        self.cardinality = k

    def number(self):
        return sum(self.multiset)

    def coefficients(self, generators):
        counter = Counter(self.multiset)
        factorization = []
        for gen in generators:
            if gen in counter:
                factorization.append(counter[gen])
            else:
                factorization.append(0)
        return tuple(factorization)







# Returns the smallest value c > k for which the intersection of the set of elements
# of length k and the set of elements of length c is empty
def min_value_length_c(generators, maximal_length):
    k = maximal_length
    # Assign a value to the largest element in the set of elements of length k
    max_element_of_length_k = k * generators[-1]
    # Assign to j the value of k and increment j until the intersection of sets
    # of length k and j are nonempty
    j = k + 1
    while j * generators[0] <= max_element_of_length_k:
        j += 1
    return j


# Function to create a list of objects of class Semigroup where each class object
# contains the multiset, the length, and a method called number() to calculate
# the number.
def create_semigroup(generators, max_length):
    semigroup = []
    for k in range(1, max_length):
        multisets_of_size_k = combinations_with_replacement(generators, k)
        for multisubset in multisets_of_size_k:
            semigroup.append(SemigroupElement(multisubset, k))
    return semigroup


# Calculate the maximal decomposition length of each number
def calculate_max_factorization_length(semigroup, generators, c):
    # Calculate the maximum factorization length for each element in the semigroup
    #
    # The index of this list corresponds to the semigroup element and the element
    # associated to each index is the max factorization length.
    #
    # The variable c is the smallest multiset length/cardinality such
    # c > max_length and the intersection of the multisets
    # of length max_length and the multisets of length c is empty.
    # The size of the list is
    #
    # The length of this list will be the largest generator times c - 1 (this element
    # will be in the semigroup) plus 1 to align the indexes.

    list0 = [0] * (generators[-1] * (c - 1) + 1)

    for element in semigroup:
        current_number = element.number()
        current_length = element.cardinality
        # Check if the current length is greater than the maximum length seen for the number
        if current_length > list0[current_number]:
            # Update the maximum length for the number
            list0[current_number] = current_length
    return list0


def calculate_num_of_elements_with_max_length_k(list0):
    # Count the frequency of the lengths in max_lengths, excluding 0
    list1 = Counter(num for num in list0 if num != 0)
    return list1


def create_invariants(semigroup, generators):
    invariant_dict = {0: [[(0, 0)], 0, 0, 0]}
    # Assign to each of the first 12 numbers in semigroup an empty list
    for i in range(20):
        invariant_dict[semigroup[i].number()] = [[], 0, 0, 0]
    for i in range(20):
        number = semigroup[i].number()
        invariant_dict[number][0].append(semigroup[i].coefficients(generators))

    for value in invariant_dict.values():
        factorization_lengths = []
        coefficient_list = value[0]
        for i in range(len(coefficient_list)):
            factorization_lengths.append(sum(list(coefficient_list[i])))
        value[1] = max(factorization_lengths)
        value[2] = min(factorization_lengths)
        if value[2] == 0:
            value[3] = 0
        else:
            value[3] = round(value[1] / value [2],2)

    invariant_dict = dict(list(invariant_dict.items())[:10])
    return invariant_dict

def example1(generators):
    semigroup = []
    for k in range(1, 5):
        multisets_of_size_k = combinations_with_replacement(generators, k)
        for multisubset in multisets_of_size_k:
            semigroup.append(SemigroupElement(multisubset, k))
    semigroup = set(semigroup)
    return semigroup

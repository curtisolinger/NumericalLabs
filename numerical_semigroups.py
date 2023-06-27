from itertools import combinations_with_replacement
from collections import Counter



class NumericalSemigroup:
    def __init__(self, multiset, k):
        self.multiset = multiset
        self.cardinality = k

    def number(self):
        return sum(self.multiset)

# Returns the smallest value c for which the intersection of the set of elements
# of length k and the set of elements of length c is empty
def min_value_length_c(generators, maximal_length):
    k = maximal_length
    # Assign a value to the largest element in the set of elements of length k
    max_element_of_length_k = k * generators[-1]
    # Assign to c the value of k and increment while the intersection of sets
    # of length k and c are nonempty
    j = k + 1
    while j * generators[0] <= max_element_of_length_k:
        j += 1
    return j


# Function to create a list of objects of class Number where each class object
# contains the multiset, the length, and a method number() to calculate the num.
def generate_multisets(list1, c):
    list0 = []
    for x in range(1, c):
        multisets = combinations_with_replacement(list1, x)
        for multiset in multisets:
            list0.append(NumericalSemigroup(multiset, x))
    return list0


# Calculate the maximal decomposition length of each number
def calculate_max_factorization_length(element_set, generators, c):
    # Create a list of size N+1 where each element is initialized to 0. The index of
    # this list will be each numerical semigroup element, and it will contain the
    # maximum factorization length.
    list0 = [0] * (generators[-1] * (c - 1) + 1)

    for element in element_set:
        current_number = element.number()
        current_length = element.cardinality
        # Check if the current length is greater than the maximum length seen for the number
        if current_length > list0[current_number]:
            # Update the maximum length for the number
            list0[current_number] = current_length
    return list0


def calculate_num_of_elements_with_max_decomposition_length_k(list0):
    # Count the frequency of the lengths in max_lengths, excluding 0
    list1 = Counter(num for num in list0 if num != 0)
    return list1
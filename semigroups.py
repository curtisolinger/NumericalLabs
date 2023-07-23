from itertools import combinations_with_replacement
from collections import Counter
import pandas as pd
import json
import plotly
import plotly.express as px


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


# Function to create a list of objects of class Semigroup where each class
# object contains the multiset, the length, and a method called number() to
# calculate the number.
def create_semigroup(gen, N):
    # Calculate the multiset length c such that the max num of length
    # 'n' is less than or equal to min num of length c. So,
    # for example, if gen = {2, 3} and N = 4, then c = 6 since 3 times
    # 4 = 12 and 12 is equal to 2 times 6.
    max_num_of_len_n = gen[-1] * N
    c = N + 1
    while max_num_of_len_n > gen[0] * c:
        c += 1

    semigroup = []
    for k in range(1, c):
        multisets_of_size_k = combinations_with_replacement(gen, k)
        for multiset in multisets_of_size_k:
            semigroup.append(SemigroupElement(multiset, k))

    semigroup.sort(key=lambda x: x.number())
    return semigroup


# Calculate the max factorization length of each number and the number of
# elements of length k
def calc_num_of_elements_of_len_k(semigroup, gen, N):
    max_len_list = [0] * (N * gen[-1] + 1)
    max_num = N * gen[-1]
    for element in semigroup:
        current_num = element.number()
        current_len = element.cardinality
        # Check if the current length is greater than the maximum length
        # seen for the number
        if max_num >= current_num and current_len > max_len_list[current_num]:
            # Update the maximum length for the number
            max_len_list[current_num] = current_len
    counts_of_len_k = Counter(num for num in max_len_list if num != 0)
    return counts_of_len_k


def create_invariants(semigroup, gen):
    invariant_dict = {0: [[(0, 0)], 0, 0, 0]}
    # Assign to each of the first 12 numbers in semigroup an empty list
    for i in range(20):
        invariant_dict[semigroup[i].number()] = [[], 0, 0, 0]
    for i in range(20):
        number = semigroup[i].number()
        invariant_dict[number][0].append(semigroup[i].coefficients(gen))

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
            value[3] = round(value[1] / value[2], 2)

    invariant_dict = dict(list(invariant_dict.items())[:10])
    return invariant_dict

def create_invariants_for_single_element(semigroup, single_element, gen):
    # invariant_list = []
    invariant_list = [[], 0, 0]

    for semigroup_element in semigroup:
        if semigroup_element.number() == single_element:
            invariant_list[0].append(semigroup_element.coefficients(gen))

    factorization_lengths = []
    coefficient_list = invariant_list[0]
    for i in range(len(coefficient_list)):
        factorization_lengths.append(sum(list(coefficient_list[i])))
    invariant_list[1] = max(factorization_lengths)
    invariant_list[2] = min(factorization_lengths)

    print(invariant_list)
    return invariant_list

    # i = 0
    # while semigroup[i].number() <= single_element:
    #     if semigroup[i].number() == single_element:
    #         invariant_dict[single_element][0].append(semigroup[i].coefficients(
    #         gen))
    #     i += 1




# def example1(gen):
#     semigroup = []
#     for k in range(1, 5):
#         multisets_of_size_k = combinations_with_replacement(gen, k)
#         for multisubset in multisets_of_size_k:
#             semigroup.append(SemigroupElement(multisubset, k))
#     semigroup = set(semigroup)
#     return semigroup


def create_factorization_fig(N, length_counts):
    df = pd.DataFrame.from_dict(length_counts, orient='index', columns=['num'])
    df = df[df.index <= N]
    df.sort_index(inplace=True)
    # Insert a row with index 0 and num value 0
    df.loc[-1] = [0]
    df.index = df.index + 1
    df.sort_index(inplace=True)
    fig = px.line(df)
    graphjson = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphjson


def create_example_1(semigroup):
    numbers = []
    for element in semigroup[:50]:
        num = element.number()
        if num not in numbers and num <= 20:
            numbers.append(num)
    numbers.sort()
    return numbers


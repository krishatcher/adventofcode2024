"""

Solution to the Day 1, Challenge 1 challenge for the 2024 Advent of Code event

Details: https://adventofcode.com/2024/day/1

"""

import pandas as pd

def run():
    '''Orchestration function'''
    g1, g2 = import_source()
    answer = calculate_distances(g1, g2)

    print(f"The total distance is: {answer}")

def import_source():
    '''Import the list data'''
    data = pd.read_csv('input.tsv', sep='\t')

    group1 = data["group1"].tolist()
    group2 = data["group2"].tolist()

    return (group1, group2)

def calculate_distances(group1: list, group2: list):
    '''Calculate the total distances for all pairs'''
    final_distance = 0

    # ensure that the lists are sorted with the smallest at the beginning
    group1.sort()
    group2.sort()

    # calculate the differences between the index pairs for the full list
    for index, value in enumerate(group1):
        difference = abs(value - group2[index])
        final_distance += difference

    return final_distance

if __name__ == "__main__":
    run()

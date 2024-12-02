"""

Solution to the Day 1, Challenge 2 challenge for the 2024 Advent of Code event

Details: https://adventofcode.com/2024/day/1#part2

Note that the input provided by the challenge site was converted to a TSV file with headers for the two columns of 'group1' and 'group2'

"""

import pandas as pd

def run():
    '''Orchestration function'''
    g1, g2 = import_source()
    answer = calculate_similarity(g1, g2)

    print(f"The similarity score is: {answer}")

def import_source():
    '''Import the list data'''
    data = pd.read_csv('input.tsv', sep='\t')

    group1 = data["group1"].tolist()
    group2 = data["group2"].tolist()

    return (group1, group2)

def calculate_similarity(group1: list, group2: list):
    '''Calculate the total distances for all pairs'''
    final_similarity = 0

    # calculate the similarity between the two lists
    for value in group1:
        count = group2.count(value)
        new_similarity = value * count
        final_similarity += new_similarity

    return final_similarity

if __name__ == "__main__":
    run()

#!/usr/bin/python

"""Needleman-Wunsch algorithm for sequence alignment, and application
to NorthEuraLex data."""

import pandas
import itertools


def needleman_wunsch(sequence1, sequence2):
    """Generate an alignment between sequence1 and sequence2.

    Use Needleman and Wunsch's dynamic programming algorithm to create
    an alignment between sequence1 and sequence2, and return the
    corresponding edit distance.

    """
    data = [[None for _ in range(len(sequence1) + 1)]
            for _ in range(len(sequence2) + 1)]
    traceback = [[None for _ in range(len(sequence1) + 1)]
                 for _ in range(len(sequence2) + 1)]

    for top in range(len(sequence1) + 1):
        data[0][top] = top
        traceback[0][top] = "←"
    for left in range(len(sequence2) + 1):
        data[left][0] = left
        traceback[left][0] = "↑"

    for column in range(len(sequence1)):
        for row in range(len(sequence2)):
            topleft = data[row][column]
            top = data[row][column + 1]
            left = data[row + 1][column]

            replace_cost = 0 if sequence1[column] == sequence2[row] else 1

            from_topleft = topleft + replace_cost
            from_top = top + 1
            from_left = left + 1

            if from_topleft < from_top and from_topleft < from_left:
                direction = "↖"
                cell = from_topleft
            elif from_top < from_left:
                direction = "↑"
                cell = from_top
            else:
                direction = "←"
                cell = from_left
            data[row + 1][column + 1] = cell
            traceback[row + 1][column + 1] = direction

    distance = data[-1][-1]
    column = len(sequence1)
    row = len(sequence2)
    alignment = []
    while row > 0 or column > 0:
        if traceback[row][column] == "↖":
            alignment.insert(0, (sequence1[column - 1], sequence2[row - 1]))
            row = row - 1
            column = column - 1
        elif traceback[row][column] == "←":
            alignment.insert(0, (sequence1[column - 1], None))
            column = column - 1
        elif traceback[row][column] == "↑":
            alignment.insert(0, (None, sequence2[row - 1]))
            row = row - 1
        else:
            raise RuntimeError

    return distance, alignment


def all_pairs():
    data = pandas.read_csv(
        "../Aehnlichkeitsmatrix/beispieldaten_northeuralex.tsv",
        keep_default_na=False,
        sep="\t")
    for concept, block in data.groupby("gloss"):
        for _, group in block.groupby("class"):
            if len(group) > 1:
                for (index1, data1), (index2, data2) in itertools.combinations(
                        group.iterrows(), 2):
                    yield needleman_wunsch(data1["IPA"], data2["IPA"])[1]

import pandas
import itertools
from numpy import log

northeuralex = pandas.read_csv("beispieldaten_northeuralex.tsv", sep="\t")

shared = {}
for (l1, language1), (l2, language2) in itertools.combinations(
        northeuralex.groupby("language"), 2):
    sv = 0
    c = 0
    for concept in set(language1["gloss"]) | set(language2["gloss"]):
        words1 = set(language1[language1["gloss"] == concept]["class"])
        words2 = set(language2[language2["gloss"] == concept]["class"])
        sv += len(words1 & words2) / len(words1 | words2)
        c += 1
    sv /= c

    print(l1, l2, sv, 1000 * log(sv) / 2 / log(0.86))
    shared[l1, l2] = sv

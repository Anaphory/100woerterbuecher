import pandas

data = pandas.read_csv("beispieldaten_northeuralex.tsv",
                       names=["gloss", "language", "orthographic", "IPA", "class"], sep="\t")

data_part = data[(data["language"] =="deu") | (data["language"] == "eng") | (data["language"] == "dan")]

all_concepts = sorted(set(data_part["gloss"]), key=str.upper)

concepts = [all_concepts[0],
            all_concepts[500],
            all_concepts[900],
            all_concepts[-1]]

filter = data_part["gloss"] == None
for c in concepts:
    filter |= data_part["gloss"] == c

data_small = data_part[filter]

data_small.reset_index(inplace=True, drop=True)

data_small.to_csv(
        "beispieldaten_northeuralex_kurz.tsv", sep="\t", index=False,
        encoding="utf-8")
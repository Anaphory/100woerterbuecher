import pandas

data = pandas.read_csv(
    "beispieldaten_northeuralex.tsv",
    names=["gloss", "language", "orthographic", "IPA", "class"],
    sep="\t")

data_part = data[(data["language"] =="deu")
                 | (data["language"] == "eng")
                 | (data["language"] == "dan")]

all_concepts = sorted(set(data_part["gloss"]), key=str.upper)

concepts = [concepts[0], concepts[len(concepts)//2], concepts[-1]]

filter = 
data_part["gloss"] == concepts

data_three = data_part[

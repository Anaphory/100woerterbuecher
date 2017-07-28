#!python

"""Calculate pairwise shared vocabulary."""

import pandas

def calculate_pairwise_shared_vocabulary(data, language1, language2):
    return 0.0


def test_small_data_set():
    data = pandas.DataFrame(columns=[
    "gloss", "language", "orthographic", "IPA", "class"], data=[
    ["Abend::N", "deu", "Abend", "aabɛnt", "7"],
    ["Abend::N", "eng", "evening", "iivnɪŋ", "35"],
    ["Abend::N", "dan", "aften", "ɑfdən", "37"],
    ["lesen::V", "deu", "lesen", "leezən", "2"],
    ["lesen::V", "dan", "læse", "lɛɛsə", "2"],
    ["lesen::V", "eng", "read", "ɹiid", "37"],
    ["versinken::V", "eng", "sink", "sɪŋk", "26"],
    ["versinken::V", "dan", "synke", "søŋɡə", "26"],
    ["versinken::V", "deu", "versinken", "fɛɐzɪŋkən", "26"],
    ["versinken::V", "dan", "synke_ned", "søŋɡə_neðˀ", "37"],
    ["übersetzen::V", "eng", "translate", "tɹænsleɪt", "7"],
    ["übersetzen::V", "dan", "oversætte", "ɔuəʀsɛdə", "16"],
    ["übersetzen::V", "deu", "übersetzen", "yybɐzɛt͡sən", "44"]]
    )
    
    # Every language shares all its vocabulary with itself.
    assert calculate_pairwise_shared_vocabulary(data, "dan", "dan") == 1
    
    # Pairwise shared vocabulary proportion is symmetric.
    assert calculate_pairwise_shared_vocabulary(
            data, "dan", "eng") == calculate_pairwise_shared_vocabulary(
                    data, "eng", "dan")
    
    # German and English share the words for one concept (versinken::V) in a
    # list of 4 concepts.
    assert calculate_pairwise_shared_vocabulary(data, "deu", "eng") == 1/4
    
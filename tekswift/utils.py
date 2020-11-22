"""Utilities for deriving functionality from pytekswift and pycctek."""
import string
import collections
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from fuzzywuzzy import fuzz

try:
    from nltk.corpus import stopwords
except LookupError:
    import nltk

    nltk.download("stopwords")

import cctek
from tekswift import dataloader

stopwords = stopwords.words("english")


def fuzz_prob(issuer, institution):
    """Return Fuzz wuzz simple ratio divided by 100."""
    return fuzz.ratio(issuer, institution) / 100


def transform_country_data(country_data):
    """Return a new flattened representation of the swiftcode_data."""
    new_data = []
    for key, value in country_data.items():
        new_transform = collections.defaultdict()
        new_transform["swiftcode"] = key
        new_transform.update(value)
        new_data.append(new_transform)
    return new_data


def clean_string(text):
    """Return cleaned string."""
    text = "".join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = "".join([word for word in text.split() if word not in stopwords])
    return text


def cosine_sim_vectors(vec1, vec2):
    """Calculate the cosine similarity of 2 vectors.

    Note `cosine_similarity()` expects 2D arrays and the input vectors are 1D
    vectors so we need to reshape them.
    """
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]


def vectorize(cleaned_strings: list):
    """Return vectors of CountVectorizer.

    Where vectors[0] is first string,and vectors[1] is the second string.
    """
    vectorizer = CountVectorizer().fit_transform(cleaned_strings)
    vectors = vectorizer.toarray()
    return vectors


def issuer_institution_similarity(issuer: str, institution: str) -> float:
    """Return prob[0,1] that issuer and institution strings are similar."""
    cleaned = list(map(clean_string, [issuer, institution]))
    vectors = vectorize(cleaned)
    probability = cosine_sim_vectors(vectors[0], vectors[1])
    return probability


def get_institutions_from_swift(country_code):
    """Return a list of institutions and swiftcodes from country code."""
    return transform_country_data(dataloader.load_country_data(country_code))


def issuer_institutions_probmap(issuer, institutions, fuzz=False):
    """Return a map of swiftcode to probabilty"""
    probmap = collections.defaultdict()
    for ins in institutions:
        if fuzz:
            probmap[ins.get("swiftcode")] = fuzz_prob(
                issuer, ins.get("institution"))
        else:
            probmap[ins.get("swiftcode")] = issuer_institution_similarity(
                issuer, ins.get("institution")
            )
    return probmap


def filter_probmap(probmap, probability):
    """Return a filtered list of swiftcodes."""
    return [k for k, v in probmap.items() if v >= probability]


def bin_to_swifts(bin_no, p=0.8, fuzz=True):
    """Bank Identification Number to Swift matches."""
    bin_data = cctek.bin_checker(bin_no)
    issuer = bin_data.get("issuer")
    country_code = bin_data.get("country").get("alpha_2")
    institutions = get_institutions_from_swift(country_code)
    probmap = issuer_institutions_probmap(issuer, institutions, fuzz=fuzz)
    swifts = {c: dataloader.lookup_swiftcode(
        c) for c in filter_probmap(probmap, p)}
    return swifts, bin_data, probmap

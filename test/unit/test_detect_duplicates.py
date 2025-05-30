import pytest
from src.util.detector import detect_duplicates
# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True


def test_all_fields_match_duplicate_detected(): #exakt same entry
    articles = [
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
    ]
    result = detect_duplicates(data="", articles=articles)
    assert len(result) == 1


def test_same_doi_one_missing_doi(): #same title and year, but one has no doi
    articles = [
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
        {"title": "sometihn", "year": "2020", "doi": None},
    ]
    result = detect_duplicates(data="", articles=articles)
    assert len(result) == 1  


def test_both_missing_doi():    #same title and year, but both have no doi
    articles = [
        {"title": "sometihn", "year": "2022", "doi": None},
        {"title": "sometihn", "year": "2022", "doi": None},
    ]
    result = detect_duplicates(data="", articles=articles)
    assert len(result) == 1  


def test_unique_doi_same_title_and_year(): #same title and year, but different doi
    articles = [
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
        {"title": "sometihn", "year": "2022", "doi": "33.1234/abc"},
    ]
    result = detect_duplicates(data="", articles=articles)
    assert len(result) == 0  


def test_different_titles_same_year_and_doi(): #same year and doi, but different titles
    articles = [
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
        {"title": "another title", "year": "2022", "doi": "10.1234/xyz"},
    ]
    result = detect_duplicates(data="", articles=articles)
    assert len(result) == 1


def test_different_titles_and_years_same_doi(): #all fields are different
    articles = [
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
        {"title": "another title", "year": "2023", "doi": "10.1234/xyz"},
    ]
    result = detect_duplicates(data="", articles=articles)
    assert len(result) == 0


def test_all_fields_unique(): #all fields are unique
    articles = [
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
        {"title": "ML", "year": "2023", "doi": "33.1234/abc"},
    ]
    result = detect_duplicates(data="", articles=articles)
    assert len(result) == 0

def test_empty_entry():
    articles = [
        {},
        {"title": "sometihn", "year": "2022", "doi": "10.1234/xyz"},
    ]
    result = detect_duplicates(data="", articles=articles) 
    assert len(result) == 0



import pytest
from src.util.detector import detect_duplicates


# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True



@pytest.mark.unit
def test_detect_duplicates1():
    bibtex_data = ""
    result = detect_duplicates(bibtex_data)
    assert result == [] 


@pytest.mark.unit
def test_detect_duplicates2():
    bibtex_data = "something"
    result = detect_duplicates(bibtex_data)
    assert result == [] 



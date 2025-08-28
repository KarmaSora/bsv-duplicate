import pytest
from src.util.detector import detect_duplicates


# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True



@pytest.mark.unit
def test_detect_duplicatesLessThan1():
    bibtex_data = ""
    with pytest.raises(ValueError):
        detect_duplicates(bibtex_data)




import pytest
from src.util.detector import detect_duplicates


# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True



@pytest.mark.unit
def test_detect_duplicatesNoEntries():
    bibtex_data = ""
    with pytest.raises(ValueError):
        detect_duplicates(bibtex_data)



@pytest.mark.unit
def test_detect_duplicatesOneSingleEnrty():
        bibtex_data = """
        @article{key1,
            author = {Author One},
            title = {Title One}
        }
        """
        result = detect_duplicates(bibtex_data)
        assert result == []



@pytest.mark.unit
def test_detect_duplicatesTwoIdenticalEntries():
        bibtex_data = """
        @article{key1,
            author = {Author One},
            title = {Title One}
        }
            @article{key1,
            author = {Author One},
            title = {Title One}
        }
        """
        result = detect_duplicates(bibtex_data)
        assert len(result) == 1



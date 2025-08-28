import pytest
from src.util.detector import detect_duplicates
# Import Article for direct value comparison in tests
from src.util.parser import Article


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




@pytest.mark.unit
def test_detect_duplicatesTwoIdenticalEntriesdiffDoi():
        bibtex_data = """
        @article{key1,
            author = {Author One},
            title = {Title One}
        }
            @article{key1,
            author = {me},
            title = {again}
        }
        """
        result = detect_duplicates(bibtex_data)
        
        assert len(result) == 0


@pytest.mark.unit
def test_detect_duplicatesTwoDifferentEntries():
    bibtex_data = """
    @article{key1,
        author = {Author One},
        title = {Title One}
    }
    @article{key2,
        author = {Author Two},
        title = {Title Two}
    }
    """
    result = detect_duplicates(bibtex_data)
    assert result == []


@pytest.mark.unit
def test_detect_duplicatesTwoIdenticalEntriesActualValue():
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
    assert result == [Article(key="key1")]

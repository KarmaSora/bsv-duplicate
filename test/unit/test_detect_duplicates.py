import pytest
from src.util.detector import detect_duplicates
from unittest.mock import patch, MagicMock


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
        @article{frattini2023requirements,
            title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
            author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
            journal={Requirements Engineering},
            pages={1--14},
            year={2023},
            publisher={Springer},
            doi={10.1007/s00766-023-00405-y}
        }
        """
        result = detect_duplicates(bibtex_data)
        assert result == []


@pytest.mark.unit
def test_detect_duplicatesTwoUnique():
    bibtex_data = """
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian ...},
        doi={10.1007/s00766-023-00405-y}
    }
    @article{karma,
        title={Another article},
        author={Someone Else},
        doi={10.1007/s00766-023-00406-y}
    }
    """
    result = detect_duplicates(bibtex_data)
    assert result == []


@pytest.mark.unit
def test_detect_duplicatesTwoIdenticalEntries():
    bibtex_data = """
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    """
    mock_article = MagicMock(key="frattini2023requirements", doi="10.1007/s00766-023-00405-y")
    with patch('src.util.parser.Article', return_value=mock_article):
        result = detect_duplicates(bibtex_data)
        assert result == [mock_article]




@pytest.mark.unit
def test_detect_duplicatesTwoIdenticalEntriesdiffDoi():
    bibtex_data = """
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    @article{karma,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},
        doi={10.1007/s00766-023-00405-y}
    }
    """
    mock_article1 = MagicMock(key="frattini2023requirements", doi="10.1007/s00766-023-00405-y")
    mock_article2 = MagicMock(key="karma", doi="10.1007/s00766-023-00405-y")
    with patch('src.util.parser.Article', side_effect=[mock_article1, mock_article2]):
        result = detect_duplicates(bibtex_data)
        assert result == []


@pytest.mark.unit
def test_detect_duplicatesDifferentKeySameDoi():
    bibtex_data = """
    @article{key1,
        title={Article One},
        author={Author One},
        doi={10.1007/s00766-023-00405-y}
    }
    @article{key2,
        title={Article Two},
        author={Author Two},
        doi={10.1007/s00766-023-00405-y}
    }
    """
    mock_article1 = MagicMock(key="key1", doi="10.1007/s00766-023-00405-y")
    mock_article2 = MagicMock(key="key2", doi="10.1007/s00766-023-00405-y")
    with patch('src.util.parser.Article', side_effect=[mock_article1, mock_article2]):
        result = detect_duplicates(bibtex_data)
        assert result == []


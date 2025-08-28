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
        result = detect_duplicates(bibtex_data)
        
        assert len(result) == 1




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
        result = detect_duplicates(bibtex_data)
        
        assert len(result) == 0


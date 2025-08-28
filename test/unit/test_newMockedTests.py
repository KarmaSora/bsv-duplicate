# new tests after exam was over!  saving old code/tests in old.txt!!!
import pytest
from unittest.mock import patch, MagicMock
from src.util.detector import detect_duplicates


def make_article(key, doi=None):
    art = MagicMock()
    art.key = key
    art.doi = doi
    return art


def test_raises_when_zero_articles():
    with patch("src.util.detector.parse", return_value=[]):
        with pytest.raises(ValueError):
            detect_duplicates("")


def test_raises_when_one_article():
    with patch("src.util.detector.parse", return_value=[make_article("only")]):
        with pytest.raises(ValueError):
            detect_duplicates("data")


def test_duplicates_when_same_key_missing_doi():
    arts = [make_article("frattini2023"), make_article("frattini2023")]
    with patch("src.util.detector.parse", return_value=arts):
        dups = detect_duplicates("data")
        assert dups == [arts[1]]


def test_no_duplicates_when_diff_key_and_missing_doi():
    arts = [make_article("a"), make_article("b")]
    with patch("src.util.detector.parse", return_value=arts):
        assert detect_duplicates("data") == []


def test_duplicates_when_same_doi_even_if_keys_differ():
    arts = [make_article("a", "10.1000/x"), make_article("b", "10.1000/x")]
    with patch("src.util.detector.parse", return_value=arts):
        dups = detect_duplicates("data")
        assert dups == [arts[1]]


def test_duplicates_when_same_key_even_if_doi_differs():
    arts = [make_article("same", "10.1/alpha"), make_article("same", "10.1/beta")]
    with patch("src.util.detector.parse", return_value=arts):
        dups = detect_duplicates("data")
        assert dups == [arts[1]]


def test_no_duplicates_when_keys_and_dois_all_different():
    arts = [
        make_article("a", "10.1/a"),
        make_article("b", "10.1/b"),
        make_article("c", "10.1/c"),
    ]
    with patch("src.util.detector.parse", return_value=arts):
        assert detect_duplicates("data") == []


def test_multiple_duplicates_mixed_reasons():
    a1 = make_article("alpha", "10.9/dup")
    a2 = make_article("beta", "10.9/dup")  
    a3 = make_article("konly")             
    a4 = make_article("konly")           
    a5 = make_article("gamma", "10.9/unique")
    arts = [a1, a2, a3, a4, a5]

    with patch("src.util.detector.parse", return_value=arts):
        dups = detect_duplicates("data")
        assert dups == [a2, a4]

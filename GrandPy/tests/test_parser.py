from GrandPy.controller.parser import Parser
import pytest


def test_parser_is_ok_1():
    test = Parser()
    expected_result = "tour eiffel"
    result = test.my_parser("hello, je souhaite aller à la tour eiffel ?")
    assert result == expected_result


def test_parser_is_ok_2():
    test = Parser()
    expected_result = "musée art histoire fribourg"
    result = test.my_parser(
        "Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? "
        "Au fait, pendant que j'y pense, pourrais-tu m'indiquer "
        "où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?"
    )
    assert result == expected_result


def test_parser_is_ok_3():
    test = Parser()
    expected_result = "tour eiffel"
    result = test.my_parser(
        "Bonsoir Grandpy, j'espère que tu as passé une belle semaine. "
        "Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? "
        "Merci d'avance et salutations à Mamie"
    )
    assert result == expected_result


def test_parser_is_str():
    test = Parser()
    result = type(test.my_parser("je souhaite aller à la tour eiffel ?"))
    expected_result = str
    assert result == expected_result


def test_parser_with_upper():
    test = Parser()
    result = test.my_parser("HELLO, je souhaite aLler à la tour eiffel ?")
    expected_result = "tour eiffel"
    assert result == expected_result


def test_parser_with_signs():
    test = Parser()
    result = test.my_parser("HELLO, je souhaite aLler à la tour eiffel /+<!°?")
    expected_result = "tour eiffel"
    assert result == expected_result


def test_parser_empty():
    with pytest.raises(ValueError):
        test = Parser()
        test.my_parser("")

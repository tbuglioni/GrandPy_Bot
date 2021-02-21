from GrandPy.controller.parser import Parser


def test_parser_is_ok():
    test = Parser()
    assert (
        test.my_parser("hello, je souhaite aller à la tour eiffel ?") == "tour eiffel"
    )


def test_parser_is_str():
    test = Parser()
    assert type(test.my_parser("hello, je souhaite aller à la tour eiffel ?")) == str


def test_parser_with_upper():
    test = Parser()
    assert (
        test.my_parser("HELLO, je souhaite aLler à la tour eiffel ?") == "tour eiffel"
    )


def test_parser_with_signs():
    test = Parser()
    assert (
        test.my_parser("HELLO, je souhaite aLler à la tour eiffel ?./+/><!°?")
        == "tour eiffel"
    )

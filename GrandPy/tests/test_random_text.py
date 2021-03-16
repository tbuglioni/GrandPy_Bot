from GrandPy.controller.random_text import RandomText


def test_return_random_text():
    test = RandomText()
    result = test.return_random()
    assert result in test.text_list

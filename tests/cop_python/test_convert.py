from pytest import mark, raises

from cop_python.convert import capitalize


def test_capitalize():
    assert capitalize('suzie') == 'Suzie'

@mark.parametrize(
    ["text", "expected_capitalized_text"],
    [
        ("suzie", "Suzie"),
        ("Suzie", "Suzie"),
        ("étienne", "Étienne"),
        ("SUZIE", "Suzie"),
        ("t", "T"),
        ("T", "T"),
        ("音楽", "音楽"),
    ],
)
def test_capitalize_with_valid_params(text, expected_capitalized_text):
    assert capitalize(text) == expected_capitalized_text

@mark.parametrize(
    ["invalid_text", "expected_error_message"],
    [
        (None, "text must be a non-empty string, got None"),
        ("", "text must be a non-empty string, got "),
        (18, "text must be a non-empty string, got 18"),
        (["t", "i"], "text must be a non-empty string, got ['t', 'i']"),
    ],
)
def test_capitalize_with_invalid_params(invalid_text, expected_error_message):
    with raises(ValueError) as error:
        capitalize(invalid_text)
    assert str(error.value) == expected_error_message

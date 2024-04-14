from datetime import date
from seasons import convert_days_to_words

def test_convert_to_words():
    """
    Test convert_to_words function.
    """
    # Test case with 10477 days
    expected_output = "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert convert_days_to_words(10477) == expected_output



import pytest
from working import convert

def test_valid_format_12_hour():
    # Test valid input with 12-hour format
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_invalid_time():
    # Test invalid time
    with pytest.raises(ValueError):
        convert(":60 AM to 5:60 PM")  # Minutes out of range

def test_invalid_format():
    # Test invalid format
    with pytest.raises(ValueError):
        convert("09:00 AM = 17:00 PM")  # Invalid separator
    with pytest.raises(ValueError):
        convert("08:60 AM to 4:60 PM")

if __name__ == "__main__":
    pytest.main()

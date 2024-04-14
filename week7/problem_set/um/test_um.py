from um import count


def test_single_um():
    assert count("um") == 1


def test_question_um():
    assert count("um?") == 1

def test_capitalized_um():
    assert count("Um, yeah no") == 1

def test_multiple_um():
    assert count("um so here is my um presentation") == 2

def test_no_um():
    assert count("where did the ums go?") == 0

def test_words_with_um():
    assert count("conundrum?") == 0
    assert count("rumpus, umbrella, humongous") == 0

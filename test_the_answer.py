from the_answer import the_answer

def test_the_answer_no_args():
    answer = the_answer()
    assert answer == 42

def test_the_answer_args():
    answer = the_answer('life', 'universe', 'everything')
    assert answer == 42

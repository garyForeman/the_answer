from the_answer import the_answer

def test_the_answer_no_args():
    answer = the_answer()
    assert answer == 42

def test_the_answer_args():
    answer = the_answer('life', 'universe', 'everything')
    assert answer == 42

def test_the_answer_kwargs():
    answer = the_answer(rush=2112, yes='roundabout')
    assert answer == 42

def test_the_answer_both():
    answer = the_answer('foo', 'bar', bat='baz')
    assert answer == 42
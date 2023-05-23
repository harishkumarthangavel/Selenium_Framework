def sample_function(param):
    return param + 1

def test_success():
    assert sample_function(2) == 3

def test_failure():
    assert sample_function(1) == 3


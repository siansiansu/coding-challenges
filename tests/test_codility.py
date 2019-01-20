from codility import iterations_binarygap

def test_binary_gap():
    ans1 = iterations_binarygap.solution(1041)
    ans2 = iterations_binarygap.solution2(1041)
    assert (ans1 == 5) and (ans2 == 5)
    
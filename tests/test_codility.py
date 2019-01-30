from codility import iterations_BinaryGap
from codility import arrays_OddOccurrencesInArray
from codility import arrays_CyclicRotation



def test_binary_gap():
    ans1 = iterations_BinaryGap.solution(1041)
    ans2 = iterations_BinaryGap.solution2(1041)
    assert (ans1 == 5) and (ans2 == 5)

def test_odd_occurrences_in_array():
    ans1 = arrays_OddOccurrencesInArray.solution([9, 3, 9, 3, 9, 7, 9])
    assert ans1 == 7

def test_cyclic_rotation():
    ans1 = arrays_CyclicRotation.solution([3, 8, 9, 7, 6], 3)
    assert ans1 == [9, 7, 6, 3, 8]
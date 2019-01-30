from codility import iterations_binary_gap
from codility import arrays_odd_occurrences_in_array
from codility import arrays_cyclic_rotation

def test_binary_gap():
    ans1 = iterations_binary_gap.solution(1041)
    ans2 = iterations_binary_gap.solution2(1041)
    assert (ans1 == 5) and (ans2 == 5)

def test_odd_occurrences_in_array():
    ans1 = arrays_odd_occurrences_in_array.solution([9, 3, 9, 3, 9, 7, 9])
    assert ans1 == 7

def test_cyclic_rotation():
    ans1 = arrays_cyclic_rotation.solution([3, 8, 9, 7, 6], 3)
    assert ans1 == [9, 7, 6, 3, 8]
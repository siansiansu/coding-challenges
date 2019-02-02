from codility import binary_gap
from codility import odd_occurrences_in_array
from codility import cyclic_rotation
from codility import frog_jmp
from codility import perm_missing_elem
from codility import tape_equilibrium
from codility import perm_check
from codility import missing_integer
from codility import distinct

def test_binary_gap():
    ans1 = binary_gap.solution(1041)
    ans2 = binary_gap.solution2(1041)
    assert (ans1 == 5) and (ans2 == 5)

def test_odd_occurrences_in_array():
    ans1 = odd_occurrences_in_array.solution([9, 3, 9, 3, 9, 7, 9])
    assert ans1 == 7

def test_cyclic_rotation():
    ans1 = cyclic_rotation.solution([3, 8, 9, 7, 6], 3)
    assert ans1 == [9, 7, 6, 3, 8]

def test_frog_jmp():
    ans1 = frog_jmp.solution(10, 85, 30)
    assert ans1 == 3

def test_perm_missing_elem():
    ans1 = perm_missing_elem.solution([2, 3, 1, 5])
    assert ans1 == 4

def test_tape_equilibrium():
    ans1 = tape_equilibrium.solution([3, 1, 2, 4, 3])
    assert ans1 == 1

def test_perm_check():
    ans1 = perm_check.solution([4, 1, 3, 2])
    assert ans1 == 1

def test_missing_integer():
    ans1 = missing_integer.solution([1, 2, 3])
    assert ans1 == 4

def test_distinct():
    ans1 = distinct.solution([2, 1, 1, 2, 3, 1])
    assert ans1 == 3
import pytest

from task3.solution import (
    appearance,
    to_intervals,
    merge_intervals,
    intersect_intervals,
)


# fmt: off
tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513,
                             1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009,
                             1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773,
                             1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503,
                             1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
    },
]
# fmt: on
@pytest.mark.parametrize("test_case", tests)
def test_appearance(test_case):
    result = appearance(test_case["intervals"])
    assert result == test_case["answer"]


def test_to_intervals():
    lesson_start = 10
    lesson_end = 50
    times = [5, 20, 15, 60, 30, 40]
    expected = [(10, 20), (15, 50), (30, 40)]
    assert to_intervals(times, lesson_start, lesson_end) == expected
    assert to_intervals([], lesson_start, lesson_end) == []


def test_merge_intervals():
    intervals = [(1, 3), (2, 5), (6, 8), (7, 10)]
    expected = [(1, 5), (6, 10)]
    assert merge_intervals(intervals) == expected
    assert merge_intervals([]) == []
    intervals = [(1, 5), (6, 10)]
    assert merge_intervals(intervals) == [(1, 5), (6, 10)]


def test_intersect_intervals():
    a = [(1, 5), (10, 15)]
    b = [(3, 6), (12, 20)]
    assert intersect_intervals(a, b) == 5
    a = []
    b = [(1, 2)]
    assert intersect_intervals(a, b) == 0
    a = [(1, 2)]
    b = []
    assert intersect_intervals(a, b) == 0

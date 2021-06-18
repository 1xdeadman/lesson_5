import pytest
import random as rnd
import tasks.task_13 as task_13


@pytest.mark.task_13
def test_find_max_word():
    text = "самое большое слово - это СЛОВО, находящееся здесь. Но это не факт."
    assert 'находящееся' == task_13.find_max_word(text)


@pytest.mark.task_13
@pytest.mark.parametrize(
    ('data'),
    [
        pytest.param([x for x in range(100)]),
        pytest.param([x for x in range(100, 300, 2)]),
        pytest.param([x for x in range(100, 300, 3)]),
        pytest.param([x for x in range(100, -100, -2)]),
        pytest.param([]),
        pytest.param([1]),
        pytest.param([1, 1])
    ]
)
def test_bubble_sort(data: list[int]):
    input_data = data.copy()
    data.sort()
    rnd.shuffle(input_data)
    task_13.bubble_sort(input_data)
    assert data == input_data


@pytest.mark.bin_search
@pytest.mark.task_13
@pytest.mark.parametrize(
    ('value', 'result'),
    [
        pytest.param(20, 10),
        pytest.param(10, 0),
        pytest.param(11, 1),
        pytest.param(99, 89),
        pytest.param(60, 50)
    ]
)
def test_bin_search(value, result):
    res_data = [x for x in range(10, 100)]
    assert result == task_13.bin_search(res_data, value)


@pytest.mark.bin_search
@pytest.mark.task_13
@pytest.mark.parametrize(
    ('value',),
    [
        pytest.param(5),
        pytest.param(0),
        pytest.param(11),
        pytest.param(30),
        pytest.param(100),
        pytest.param(-10)
    ]
)
def test_bin_searc_wrong(value):
    res_data = [1, 10, 60]
    assert task_13.bin_search(res_data, value) is None






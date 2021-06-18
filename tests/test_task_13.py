import pytest
import random as rnd
import tasks.task_13 as task_13


@pytest.mark.task_13
def test_find_max_word():
    text = "самое большое слово - это СЛОВО, находящееся здесь. Но это не факт."
    assert 'находящееся' == task_13.find_max_word(text)


@pytest.mark.task_13
def test_bubble_sort():

    res_data = [x for x in range(100)]
    input_data = res_data.copy()
    rnd.shuffle(input_data)
    assert res_data == task_13.bubble_sort(input_data)


@pytest.mark.task_13
def test_bin_search():
    res_data = [x for x in range(10, 100)]
    assert 10 == task_13.bin_search(res_data, 20)
    assert 0 == task_13.bin_search(res_data, 10)
    assert 1 == task_13.bin_search(res_data, 11)
    assert 99 == task_13.bin_search(res_data, 109)
    assert 50 == task_13.bin_search(res_data, 60)


@pytest.mark.task_13
def test_bin_searc_2h():
    res_data = [1, 10, 60]
    assert task_13.bin_search(res_data, 0) is None
    assert task_13.bin_search(res_data, 5) is None
    assert task_13.bin_search(res_data, 11) is None
    assert task_13.bin_search(res_data, 30) is None
    assert task_13.bin_search(res_data, 100) is None
    assert task_13.bin_search(res_data, -10) is None






import price_info


def test_cost_of_fruits_apple():
    result = price_info.cost_of_fruits("apple", 10)

    assert result == 12.00


def test_cost_of_fruits_orange():
    result = price_info.cost_of_fruits("orange", 5)

    assert result == 7.00


def test_total_cost_shopping():
    result = price_info.total_cost_shopping()

    assert round(result, 2) == 46.75
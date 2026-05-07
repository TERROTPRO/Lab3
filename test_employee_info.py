import employee_info


def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(25, 35)

    assert len(result) == 2
    assert result[0]["name"] == "John"
    assert result[1]["name"] == "Mike"


def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()

    assert round(result, 2) == 60166.67


def test_get_employees_by_dept_marketing():
    result = employee_info.get_employees_by_dept("Marketing")

    assert len(result) == 2
    assert result[0]["name"] == "Jane"
    assert result[1]["name"] == "Mary"


def test_get_employees_by_dept_engineering():
    result = employee_info.get_employees_by_dept("Engineering")

    assert len(result) == 2
    assert result[0]["name"] == "Chloe"
    assert result[1]["name"] == "Mike"


def test_get_employees_by_dept_sales():
    result = employee_info.get_employees_by_dept("Sales")

    assert len(result) == 2
    assert result[0]["name"] == "John"
    assert result[1]["name"] == "Peter"
import Lab2.bmi as bmi

def test_bmi_underweight():
    expected_result = -1
    actual_result = bmi.calculate_bmi(1.73, 40)
    assert (actual_result == expected_result)

def test_bmi_normal():
    expected_result = 0
    actual_result = bmi.calculate_bmi(1.73, 60)
    assert (actual_result == expected_result)

def test_bmi_overweight():
    expected_result = 1
    actual_result = bmi.calculate_bmi(1.73, 80)
    assert (actual_result == expected_result)
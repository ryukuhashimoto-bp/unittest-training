from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_example():
    input_value = 3
    expected_output = "Fizz"
    result = fizzbuzz(input_value)
    assert result == expected_output


def test_fizzbuzz_example_5():
    input_value = 5
    expected_output = "Buzz"
    result = fizzbuzz(input_value)
    assert result == expected_output


def test_fizzbuzz_example_15():
    input_value = 15
    expected_output = "FizzBuzz"
    result = fizzbuzz(input_value)
    assert result == expected_output


def test_fizzbuzz_example_1():
    input_value = 1
    expected_output = "1"
    result = fizzbuzz(input_value)
    assert result == expected_output


# --- 以下、例外系テスト ---


def test_fizzbuzz_raises_valueerror_for_zero():
    try:
        fizzbuzz(0)
        assert False, "ValueError が発生しませんでした"
    except ValueError:
        pass


def test_fizzbuzz_raises_valueerror_for_over_1000():
    try:
        fizzbuzz(1001)
        assert False, "ValueError が発生しませんでした"
    except ValueError:
        pass


def test_fizzbuzz_raises_typeerror_for_string():
    try:
        fizzbuzz("a")
        assert False, "TypeError が発生しませんでした"
    except TypeError:
        pass


def test_fizzbuzz_raises_typeerror_for_float():
    try:
        fizzbuzz(3.14)
        assert False, "TypeError が発生しませんでした"
    except TypeError:
        pass


def test_fizzbuzz_example_999():
    input_value = 999
    expected_output = "Fizz"
    result = fizzbuzz(input_value)
    assert result == expected_output

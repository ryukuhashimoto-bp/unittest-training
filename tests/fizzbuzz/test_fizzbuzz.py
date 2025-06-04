from fizzbuzz.fizzbuzz import fizzbuzz
import pytest


# def test_fizzbuzz_example():
#     input_value = 3
#     expected_output = "Fizz"
#     result = fizzbuzz(input_value)
#     assert result == expected_output


# def test_fizzbuzz_example_5():
#     input_value = 5
#     expected_output = "Buzz"
#     result = fizzbuzz(input_value)
#     assert result == expected_output


# def test_fizzbuzz_example_15():
#     input_value = 15
#     expected_output = "FizzBuzz"
#     result = fizzbuzz(input_value)
#     assert result == expected_output


# def test_fizzbuzz_example_1():
#     input_value = 1
#     expected_output = "1"
#     result = fizzbuzz(input_value)
#     assert result == expected_output


# # --- 以下、例外系テスト ---


# def test_fizzbuzz_raises_valueerror_for_zero():
#     try:
#         fizzbuzz(0)
#         assert False, "ValueError が発生しませんでした"
#     except ValueError:
#         pass


# def test_fizzbuzz_raises_valueerror_for_over_1000():
#     try:
#         fizzbuzz(1001)
#         assert False, "ValueError が発生しませんでした"
#     except ValueError:
#         pass


# def test_fizzbuzz_raises_typeerror_for_string():
#     try:
#         fizzbuzz("a")
#         assert False, "TypeError が発生しませんでした"
#     except TypeError:
#         pass


# def test_fizzbuzz_raises_typeerror_for_float():
#     try:
#         fizzbuzz(3.14)
#         assert False, "TypeError が発生しませんでした"
#     except TypeError:
#         pass


# def test_fizzbuzz_example_999():
#     input_value = 999
#     expected_output = "Fizz"
#     result = fizzbuzz(input_value)
#     assert result == expected_output



def test_fizzbuzz_fizz(): assert fizzbuzz(3) == "Fizz"
def test_fizzbuzz_buzz(): assert fizzbuzz(5) == "Buzz"
def test_fizzbuzz_fizzbuzz(): assert fizzbuzz(15) == "FizzBuzz"
def test_fizzbuzz_number(): assert fizzbuzz(1) == "1"
def test_fizzbuzz_large(): assert fizzbuzz(999) == "Fizz"

def test_fizzbuzz_valueerror_zero():
    with pytest.raises(ValueError, match="n must be between 1 and 1000"):
        fizzbuzz(0)

def test_fizzbuzz_valueerror_too_large():
    with pytest.raises(ValueError, match="n must be between 1 and 1000"):
        fizzbuzz(1001)

def test_fizzbuzz_typeerror_str():
    with pytest.raises(TypeError, match="n must be an integer"):
        fizzbuzz("a")

def test_fizzbuzz_typeerror_float():
    with pytest.raises(TypeError, match="n must be an integer"):
        fizzbuzz(3.14)

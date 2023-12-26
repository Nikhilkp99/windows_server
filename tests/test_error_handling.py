import pytest
from services.error_handling import MyMathOperations


class TestMyMathOperations:
    @staticmethod
    def test_divide_valid_inputs():
        math_operations = MyMathOperations()
        result = math_operations.divide(6, 2)
        assert result == 3

    @staticmethod
    def test_divide_by_zero():
        math_operations = MyMathOperations()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            math_operations.divide(8, 0)

    @staticmethod
    def test_divide_invalid_inputs():
        math_operations = MyMathOperations()
        with pytest.raises(ValueError, match="Both inputs must be numbers"):
            math_operations.divide("a", 2)

    @staticmethod
    def test_multiply_valid_inputs():
        math_operations = MyMathOperations()
        result = math_operations.multiply(3, 4)
        assert result == 12

    @staticmethod
    def multiply(self, a, b):
        try:
            result = a * b
            return result
        except Exception as e:
            raise RuntimeError(f"An error occurred during multiplication: {e}")

    @staticmethod
    def test_check_positive_number_positive():
        math_operations = MyMathOperations()
        math_operations.check_positive_number(5)

    @staticmethod
    def test_check_positive_number_negative():
        math_operations = MyMathOperations()
        with pytest.raises(ValueError, match="Input must be a positive number"):
            math_operations.check_positive_number(-3)

    @staticmethod
    def test_process_data_valid():
        math_operations = MyMathOperations()
        data = {'value': 4}
        result = math_operations.process_data(data)
        assert result == 8

    @staticmethod
    def test_process_data_missing_key():
        math_operations = MyMathOperations()
        with pytest.raises(ValueError, match="Data must contain 'value' key"):
            math_operations.process_data({'other_key': 3})

    @staticmethod
    def test_process_data_negative_value():
        math_operations = MyMathOperations()
        with pytest.raises(RuntimeError, match="Error processing data: Input must be a positive number"):
            math_operations.process_data({'value': -2})
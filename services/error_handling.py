class MyMathOperations:
    def divide(self, a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        except TypeError:
            raise ValueError("Both inputs must be numbers")

    def multiply(self, a, b):
        try:
            result = a * b
            return result
        except Exception as e:
            raise RuntimeError(f"An error occurred during multiplication: {e}")

    def check_positive_number(self, num):
        if not isinstance(num, (int, float)) or num < 0:
            raise ValueError("Input must be a positive number")

    def process_data(self, data):
        try:
            # Assume data is a dictionary with 'value' key
            value = data['value']
            self.check_positive_number(value)
            return value * 2
        except KeyError:
            raise ValueError("Data must contain 'value' key")
        except ValueError as ve:
            raise RuntimeError(f"Error processing data: {ve}")

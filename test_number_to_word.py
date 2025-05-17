from number_to_word import number_to_word
import builtins
from unittest.mock import patch

def test_number_to_word():
    """Тестирование функции number_to_word"""
    test_cases = [
        (1, "one"),
        (2, "two"),
        (3, "three"),
        (4, "four"),
        (5, "five")
    ]
    
    for num, expected in test_cases:
        with patch('builtins.input', return_value=str(num)):
            with patch('builtins.print') as mock_print:
                number_to_word()
                mock_print.assert_called_with(f"The number is: {expected}")
    
    print("✓ All tests passed successfully!")

if __name__ == "__main__":
    test_number_to_word()

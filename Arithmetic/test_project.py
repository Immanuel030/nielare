import pytest
from unittest.mock import patch
from project import (  # Replace 'your_module' with the actual name of your Python file without the .py extension
    ifAddition,
    ifSubtraction,
    ifMultiplication,
    ifDivision,
    ifModulus,
    ifMixed
)

# Test for ifAddition function
def test_ifAddition():
    mock_previous_pairs = []
    mock_user_id = "test_user"
    mock_leaderboard = {}
    
    with patch('builtins.input', side_effect=['5']), patch('random.randint', side_effect=[2, 3]):
        score = ifAddition(1, 0, mock_previous_pairs, mock_user_id, mock_leaderboard)
        assert score == 1  # Expecting score to increase by 1

# Test for ifSubtraction function
def test_ifSubtraction():
    mock_previous_pairs = []
    mock_user_id = "test_user"
    mock_leaderboard = {}
    
    with patch('builtins.input', side_effect=['1']), patch('random.randint', side_effect=[3, 2]):
        score = ifSubtraction(1, 0, mock_previous_pairs, mock_user_id, mock_leaderboard)
        assert score == 1  # Expecting score to increase by 1

# Test for ifMultiplication function
def test_ifMultiplication():
    mock_previous_pairs = []
    mock_user_id = "test_user"
    mock_leaderboard = {}
    
    with patch('builtins.input', side_effect=['6']), patch('random.randint', side_effect=[2, 3]):
        score = ifMultiplication(1, 0, mock_previous_pairs, mock_user_id, mock_leaderboard)
        assert score == 1  # Expecting score to increase by 1

# Test for ifDivision function
def test_ifDivision():
    mock_previous_pairs = []
    mock_user_id = "test_user"
    mock_leaderboard = {}
    
    with patch('builtins.input', side_effect=['2']), patch('random.randint', side_effect=[6, 3]):
        score = ifDivision(1, 0, mock_previous_pairs, mock_user_id, mock_leaderboard)
        assert score == 1  # Expecting score to increase by 1

# Test for ifModulus function
def test_ifModulus():
    mock_previous_pairs = []
    mock_user_id = "test_user"
    mock_leaderboard = {}
    
    with patch('builtins.input', side_effect=['1']), patch('random.randint', side_effect=[5, 2]):
        score = ifModulus(1, 0, mock_previous_pairs, mock_user_id, mock_leaderboard)
        assert score == 1  # Expecting score to increase by 1

# Test for ifMixed function
def test_ifMixed():
    mock_previous_pairs = []
    mock_user_id = "test_user"
    mock_leaderboard = {}
    
    with patch('builtins.input', side_effect=['8']), patch('random.randint', side_effect=[5, 3]):
        score = ifMixed(1, 0, mock_previous_pairs, mock_user_id, mock_leaderboard)
        assert score == 1  # Expecting score to increase by 1

if __name__ == "__main__":
    pytest.main()
class InvalidScoreError(Exception):
    """Custom exception for invalid exam scores."""
    def __init__(slef,score):
        super().__init__(f"Invailid score: {score}. score ,must be between 0 and 100.")

def validate_score(score):
    """validates the given score and raises an exception if its invalid."""
    if score<0 or score>100:
        raise InvalidScoreError(score)
    return f"score {score} is valid."

try:
    score = int(input("Enter the exam score: "))
    print(validate_score(score))
except InvalidScoreError as e:
    print(f"Error:{e}")
except ValueError:
    print("Error:Please enter a valid integer.")

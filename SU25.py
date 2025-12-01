from typing import List

def q1(sentence: str) -> str:
    """
    Write a program to convert a given text to title case and remove extra spaces. Assume the text contains only letters and spaces.

    Input: A string containing the text. 
    Desired Output: The text in title case with no extra spaces.

    Example:
    Input: "hello world this is a test"
    Output: "Hello World This Is A Test"
    """


assert q1("hello world this is a test") == "Hello World This Is A Test"
assert q1("   hello    world   ") == "Hello World"
assert q1("python") == "Python"
assert q1("hELLo WoRLD") == "Hello World"


def q2(sentence: str) -> float:
    """
    Write a program to calculate the average length of words in a given text. Words are separated by spaces. Round the result to two decimal places.

    Input: A string containing the text. 
    Desired Output: The average word length as a float rounded to two decimal places.

    Example:
    Input: "The quick brown fox"
    Output: 4.00
    """


assert q2("The quick brown fox") == 4.00
assert q2("Python is great") == 4.33 
assert q2("One") == 3.00
assert q2("   spaces   everywhere   ") == 8.00


def q3(sentence: str) -> List[str]:
    """
    Write a program to extract all words longer than 5 characters from a given text. Words are separated by spaces.

    Input: A string containing the text. 
    Desired Output: A list of words longer than 5 characters, in the order they appear.

    Example:
    Input: "Natural Language Processing is fascinating"
    Output: ['Natural', 'Language', 'Processing', 'fascinating']
    """



assert q3("Natural Language Processing is fascinating") == ['Natural', 'Language', 'Processing', 'fascinating']
assert q3("Short words only") == []
assert q3("Programming in Python is enjoyable") == ['Programming', 'Python', 'enjoyable']
assert q3("   Leading and trailing spaces   ") == ['Leading', 'trailing', 'spaces']


def q4(name: str) -> bool:
    """
    Write a program to check if a given string is a valid Python identifier. A valid identifier:
    - Starts with a letter (a-z, A-Z) or an underscore (_).
    - Is followed by letters, digits (0-9), or underscores.
    - Is not a Python keyword. (Use the keyword module to check for keywords)

    Input: A string. 
    Desired Output: True if it is a valid identifier, False otherwise.

    Example:
    Input: "_my_variable1" Output: True
    Input: "2nd_variable" Output: False
    Input: "for" Output: False
    """


assert q4("_my_variable1") is True
assert q4("variable") is True
assert q4("var_123") is True
assert q4("2nd_variable") is False
assert q4("for") is False
assert q4("my-variable") is False
assert q4("") is False
assert q4("_") is True
from typing import List

def q1(sentence: str) -> List[str]:
    """
    Write a Python program that takes a sentence as input and outputs a list of the words in the sentence.

    Input: A sentence: "The quick brown fox jumps over the lazy dog"
    Desired Output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    """

assert q1("The quick brown fox jumps over the lazy dog") == \
       ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

assert q1("Hello World") == ['Hello', 'World']

assert q1("") == []

assert q1("   multiple    spaces   here  ") == ['multiple', 'spaces', 'here']


def q2(input_name:str, output_name:str):
    """
    Write a Python program that inputs a text file and outputs a new file where all the words are converted to lowercase.

    Input: A text file named "upper.txt" with the following content:
        THIS IS A SAMPLE TEXT FILE.
        ALL LETTERS ARE UPPERCASE.

    Desired Output: A new file named "lower.txt" with the following content:
        this is a sample text file.
        all letters are lowercase.
    """


def q3(doc: str) -> List[tuple[str, str]]:
    """
    Write a Python program that takes a document as input and outputs a list of the named entities (people, organizations, locations) in the document.
    Hint: This requires using a named entity recognition library like spaCy.

    Example: 
    Input: A document: "Apple Inc. is an American multinational technology company. Its headquarters are in Cupertino, California."
    Output: [('Apple Inc.', 'ORG'), ('American', 'NORP'), ('Cupertino', 'GPE'), ('California', 'GPE')]
    """

assert q3("Apple Inc. is an American multinational technology company. Its headquarters are in Cupertino, California.") == \
       [('Apple Inc.', 'ORG'), ('American', 'NORP'), ('Cupertino', 'GPE'), ('California', 'GPE')]
assert q3("Barack Obama was born in Hawaii and was the president of the USA.") == \
       [('Barack Obama', 'PERSON'), ('Hawaii', 'GPE'), ('USA', 'GPE')]
assert q3("") == []
assert q3("Google and Microsoft are tech giants in the United States.") == \
       [('Google', 'ORG'), ('Microsoft', 'ORG'), ('the United States', 'GPE')]


def q4(sentence: str) -> str:
    """
    Write a Python program that takes a sentence as input and outputs a new sentence where all the words are sorted alphabetically.

    Input: A sentence: "the quick brown fox jumps over the lazy dog"
    Output: "brown dog fox jumps lazy over quick the the"
    """

assert q4("the quick brown fox jumps over the lazy dog") == "brown dog fox jumps lazy over quick the the"
assert q4("Hello world in Python") == "Hello Python in world"
assert q4("") == ""
assert q4("apple Apple banana Banana Apple") == "Apple Apple Banana apple banana"
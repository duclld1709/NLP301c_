from typing import List

def q1(sentence: str) -> list: 
    """
    Given a sentence, write a Python program to tokenize it into words and punctuation marks.

    Input:
    This is a sample sentence. It's a simple task.

    Desired Output:
    ['This', 'is', 'a', 'sample', 'sentence', '.', 'It', "'s", 'a', 'simple', 'task', '.']
    """
    

assert q1(
    "This is a sample sentence. It's a simple task."
) == ['This', 'is', 'a', 'sample', 'sentence', '.', 'It', "'s", 'a', 'simple', 'task', '.']

assert q1(
    "Hello world this is Python"
) == ['Hello', 'world', 'this', 'is', 'Python']

assert q1(
    "...?!"
) == ['...', '?', '!']

assert q1(
    "Wait ... What?!"
) == ['Wait', '...', 'What', '?', '!']

assert q1(
    "I don't know."
) == ['I', 'do', "n't", 'know', '.']

assert q1(
    "Yes, no; maybe: always."
) == ['Yes', ',', 'no', ';', 'maybe', ':', 'always', '.']

assert q1(
    "I have 2 apples!"
) == ['I', 'have', '2', 'apples', '!']

assert q1("") == []


def q2(sentence: str) -> List[tuple]: 
    """
    Create a Python program to analyze a given text.
    - Count the frequency of each word in a given text.
    - Sort the words by their frequency in descending order.
    - Return empty list for sentence not containing characters.

    Input:
    This is a sample text. This text is for testing purposes.

    Output:
    [
        ("This", 2),
        ("is", 2),
        ("a", 1),
        ("sample", 1),
        ("text.", 1),
        ("text", 1),
        ("for", 1),
        ("testing", 1),
        ("purposes.", 1)
    ]
    """


assert q2(
    "This is a sample text. This text is for testing purposes."
) == [
    ("This", 2),
    ("is", 2),
    ("a", 1),
    ("sample", 1),
    ("text.", 1),
    ("text", 1),
    ("for", 1),
    ("testing", 1),
    ("purposes.", 1),
]

assert q2("Hello") == [("Hello", 1)]

assert q2("test test test") == [("test", 3)]

assert q2(
    "Apple apple Apple"
) == [("Apple", 2), ("apple", 1)]

assert q2(
    "Hi! Hi? Hi."
) == [("Hi!", 1), ("Hi?", 1), ("Hi.", 1)]

assert q2(
    "Python 3 is Python"
) == [("Python", 2), ("3", 1), ("is", 1)]

assert q2("") == []


def q3(sentence: str) -> str:
    """
    Write a program to correct the spelling errors in the given text

    Input:
    He is a gret person. He beleives in bod

    Desired Output:
    He is a great person. He believes in god
    """


assert q3(
    "I may bake a cake for my birthday. The talk will introduce reader about Use of baking."
) == ['may bake', 'will introduce']

assert q3(
    "She can swim and he will drive."
) == ['can swim', 'will drive']

assert q3(
    "They might consider postponing the meeting."
) == ['might consider']

assert q3(
    "He eats food every day."
) == []

assert q3("") == []


def q4(sentence: str) -> List[str]:
    """
    Write a **program to clean the following tweet and tokenize them**

    Input:

    Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro:

    Desired Output:

    ['Having', 'lots', 'of', 'fun', 'goa', 'vaction', 'summervacation', 'Fancy', 'dinner', 'Beachbay', 'restro']
    """

assert q4(
    "Having lots of fun #goa #vaction #summervacation. Fancy dinner @Beachbay restro:"
) == [
    'Having', 'lots', 'of', 'fun',
    'goa', 'vaction', 'summervacation',
    'Fancy', 'dinner', 'Beachbay', 'restro'
]

assert q4("#happy #coding #Python") == ['happy', 'coding', 'Python']

assert q4("Thanks @OpenAI @ChatGPT") == ['Thanks', 'OpenAI', 'ChatGPT']

assert q4("Great work! @john #success #AI.") == [
    'Great', 'work', 'john', 'success', 'AI'
]

assert q4("Wow!!! Amazing??? #fun") == ['Wow', 'Amazing', 'fun']

assert q4("Version 2.0 released #update") == ['Version', '2', '0', 'released', 'update']

assert q4("") == []

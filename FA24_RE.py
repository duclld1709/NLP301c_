from typing import List

def q1(sentence: str) -> List[str]:
    """
    Given a text, write a Python program to stem the words using the PorterStemmer.

    Input: The cats were playing in the garden, and they were having fun.
    Desired Output: ['the', 'cat', 'were', 'play', 'in', 'the', 'garden',s ',', 'and', 'they', 'were', 'have', 'fun', '.']
    """


assert q1("The cats were playing in the garden, and they were having fun.") == \
       ['the', 'cat', 'were', 'play', 'in', 'the', 'garden', ',', 'and', 'they', 'were', 'have', 'fun', '.']
assert q1("Dogs are running fast.") == \
       ['dog', 'are', 'run', 'fast', '.']
assert q1("He studies studying studied.") == \
       ['he', 'studi', 'studi', 'studi', '.']


def q2(sentence1: str, sentence2: str) -> float:
    """
    Create a Python program to analyze a given text.
    Compare two texts to determine their similarity.
    Use a simple technique like Jaccard similarity to measure similarity.

    Input: 
       - text1 = "The quick brown fox jumps over the lazy dog" 
       - text2 = "A quick brown fox jumped over a lazy dog"
    Desired Output: Jaccard similarity: 0.5
    """



assert q2(
    "The quick brown fox jumps over the lazy dog",
    "A quick brown fox jumped over a lazy dog"
) == 0.5
assert q2(
    "data science machine learning",
    "data science deep learning"
) == 0.6
assert q2(
    "hello world",
    "hello world"
) == 1.0
assert q2(
    "completely different words",
    "nothing in common"
) == 0.0


def q3(sentence: str) -> List[str]:
    """
    Write a program to extract the Verb Phrases from the given text.

    Input: I may bake a cake for my birthday. The talk will introduce reader about Use of baking.
    Desired Output: ['may bake', 'will introduce']
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


def q4(sentences: List[str]) -> List[List[str]]:
    """
    Write a program to create bigrams from the given texts using Gensim library's Phrases.

    Input: The mayor of new york was there", "new york mayor was present
    Desired Output:
    ['The', 'mayor', 'of', 'new_york', 'was', 'there']
    ['new_york', 'mayor', 'was', 'present']
    """


assert q4([
    "The mayor of new york was there",
    "new york mayor was present"
]) == [
    ['The', 'mayor', 'of', 'new_york', 'was', 'there'],
    ['new_york', 'mayor', 'was', 'present']
]
assert q4([
    "san francisco is beautiful",
    "I love san francisco city"
]) == [
    ['san_francisco', 'is', 'beautiful'],
    ['I', 'love', 'san_francisco', 'city']
]
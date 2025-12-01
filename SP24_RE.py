from typing import List

def q1(nats: List[str]) -> List[str]:
    """
    Write code to convert nationality adjectives like Canadian and Australian to the corresponding nouns Canada and Australia.

    Example:
    Input: ['Argentinian', 'Australian', 'Canadian']
    Output: ['Argentina', 'Australia', 'Canada']
    """

assert q1(['Argentinian', 'Australian', 'Canadian']) == [
    'Argentina', 'Australia', 'Canada'
]
assert q1(['Brazilian', 'Mexican']) == [
    'Brazil', 'Mexico'
]
assert q1([]) == []
assert q1(['Italian']) == ['Italy']


def q2(sentence: str) -> List[str]:
    """
    Write a program to extract and print all the nouns present in the below text. Hint: using spacy package

    Example:
    Input: "James works at Microsoft. She lives in Manchester and likes to play the flute."
    Output: ["James", "Microsoft", 'Manchester", "flute"]
    """


assert q2(
    "James works at Microsoft. She lives in Manchester and likes to play the flute."
) == ["James", "Microsoft", "Manchester", "flute"]

assert q2(
    "Alice bought a new phone from Apple."
) == ["Alice", "phone", "Apple"]

# assert q2(
#     "Running is fun"
# ) == ["Running"]

assert q2("") == []


def q3(data: dict[str, str]) -> List[str]:
    """
    Write a function that takes a text and a vocabulary as its arguments and returns the set of words that appear in the text and in the vocabulary. Both arguments can be represented as lists of strings.

    Example:
    Input:
    {
        text: 'a text and a vocabulary'
        vocab: 'a vocabulary'
    }
    Output: ['a', 'vocabulary']
    """

assert q3({
    "text": "a text and a vocabulary",
    "vocab": "a vocabulary"
}) == ['a', 'vocabulary']

assert q3({
    "text": "machine learning is fun",
    "vocab": "deep learning machine"
}) == ['machine', 'learning']

assert q3({
    "text": "no match here",
    "vocab": "nothing common"
}) == []

assert q3({
    "text": "",
    "vocab": "some words"
}) == []


def q4(words: List[str]) -> List[str]:
    """
    Write code to initialize a two-dimensional array of sets called word_vowels and process a list of words, 
    adding each word to word_vowels[l][v] where l is the length of the word and v is the number of vowels it contains. 
    Print l and v for one example.

    Example:
    Input: ['Write', 'code', 'to', 'initialize', 'an', 'array', 'and', 'process', 'a', 'list', 'of', 'words']
    Output: An array with shape (max(len(word)), max(len(word)))
    """

result = q4(['Write', 'code', 'to', 'initialize', 'an', 'array', 'and', 'process', 'a', 'list', 'of', 'words'])
assert 'Write' in result[5][2]
assert 'code' in result[4][2]
assert 'to' in result[2][1]
assert 'initialize' in result[10][6]
assert 'an' in result[2][1]
assert 'array' in result[5][2]


result = q4(['cat', 'dog', 'apple', 'moon'])
assert 'cat' in result[3][1]
assert 'dog' in result[3][1]
assert 'apple' in result[5][2]
assert 'moon' in result[4][2]

result = q4(['banana', 'kiwi', 'grape', 'pear', 'orange', 'fig', 'plum'])
assert 'banana' in result[6][3]
assert 'kiwi' in result[4][2]
assert 'grape' in result[5][2]
assert 'pear' in result[4][2]
assert 'orange' in result[6][3]
assert 'fig' in result[3][1]
assert 'plum' in result[4][1]


from typing import List
import re

def q1(flowers: list) -> List[list]:
    """
    Define flowers to be the list of words ['camellia', 'pendulum', 'petunias', 'begonia', 'dahlia', 'hostas', 'pelorism', 'paperwhite']. Now write code to perform the following tasks:

    a. Print all words ending with lia 
    b. Print all words longer than eight characters

    Input: ['camellia', 'pendulum', 'petunias', 'begonia', 'dahlia', 'hostas', 'pelorism', 'paperwhite']
    Desired Output: 
    a. ['camellia', 'dahlia'] 
    b. ['paperwhite']
    """


assert(q1(['rose', 'tulip', 'orchid']) == [[], []])
assert(q1(['marigold', 'paperwhite', 'rhododendron']) == [[], ['paperwhite', 'rhododendron']])
assert(q1(['camellia', 'petunias', 'begonia', 'azalealia']) == [['camellia', 'azalealia'], ['azalealia']])
assert(q1([]) == [[], []])

def q2(sentence: str) -> List[str]:
    """
    Write the slice expression that extracts the first three words of text.

    Input: text = 'She received the news of the discovery with equanimity'
    Desired Output: ['She', 'received', 'the']
    """


assert q2('She received the news of the discovery with equanimity') == ['She', 'received', 'the']
assert q2('Hello world') == ['Hello', 'world']
assert q2('I love Python') == ['I', 'love', 'Python']
assert q2('Python is an amazing programming language') == ['Python', 'is', 'an']

def q3(sentence: str) -> List[str]:
    """
    Write a program to extract the FPT University email addresses present in the text.

    Input: text = 'Please contact us at contact@fpt.edu.vn for further information. You can also give feedback at feedback@gmail.com'
    Output: ['contact@fpt.edu.vn']
    """



assert q3('Please contact us at contact@fpt.edu.vn for further information. You can also give feedback at feedback@gmail.com') == ['contact@fpt.edu.vn']
assert q3('Emails: alice@fpt.edu.vn, bob@fpt.edu.vn, charlie@gmail.com') == ['alice@fpt.edu.vn', 'bob@fpt.edu.vn']
assert q3('Reach us at info@gmail.com or support@yahoo.com') == []
assert q3('Contact: first.last@fpt.edu.vn, user-name@fpt.edu.vn, normal@domain.com') == ['first.last@fpt.edu.vn', 'user-name@fpt.edu.vn']

def q4(word_list: List[str]) -> List[str]:
    """
    Write a function that takes a list of words (containing duplicates) and returns a list of words (with no duplicates) sorted by ascending frequency.

    Input: ['table', 'table', 'table', 'table', 'table', 'table', 'table', 'table', 'table', 'table', 'chair', 'chair', 'chair', 'chair', 'chair']
    Output: ['chair', 'table']
    """


assert q4([
    'table','table','table','table','table','table','table','table','table','table',
    'chair','chair','chair','chair','chair'
]) == ['chair', 'table']
assert q4(['pen', 'pen', 'pen']) == ['pen']
assert q4(['apple', 'banana', 'apple', 'apple', 'banana', 'cherry']) == ['cherry', 'banana', 'apple']
assert q4(['dog', 'cat', 'dog', 'cat']) == ['cat', 'dog']
assert q4([]) == []
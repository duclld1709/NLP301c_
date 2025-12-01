from typing import List

def q1(flowers: List[str]) -> List[List[str]]:
    """
    Define flowers to be the list of words ['carnation', 'pendulum', 'petunias', 'begonia', 'receptacle', 'hostas', 'pelorism', 'paperwhite']. Now write code to perform the following tasks:

    a. Print all words beginning with pe 
    b. Print all words less than eight characters

    Input: ['carnation', 'pendulum', 'petunias', 'begonia', 'receptacle', 'hostas', 'pelorism', 'paperwhite']
    Desired Output: a. ['pendulum', 'petunias', 'pelorism'] 
                    b. ['begonia', 'hostas']
    """

assert q1([
    'carnation', 'pendulum', 'petunias', 'begonia',
    'receptacle', 'hostas', 'pelorism', 'paperwhite'
]) == [
    ['pendulum', 'petunias', 'pelorism'],
    ['begonia', 'hostas']
]
assert q1(['rose', 'tulip', 'lily', 'orchid']) == [
    [],
    ['rose', 'tulip', 'lily', 'orchid']
]
assert q1(['pen', 'pencil', 'people', 'perfect']) == [
    ['pen', 'pencil', 'people', 'perfect'],
    ['pen', 'pencil', 'people', 'perfect']
]
assert q1(['carnation', 'receptacle', 'paperwhite']) == [
    [],
    []
]
assert q1([]) == [[], []]
assert q1(['pet', 'peg', 'cat', 'dog']) == [
    ['pet', 'peg'],
    ['pet', 'peg', 'cat', 'dog']
]
assert q1(['receptacle', 'paperwhite', 'carnation']) == [
    [],
    []
]
assert q1(['pendulum', 'pelorism', 'cat']) == [
    ['pendulum', 'pelorism'],
    ['cat']
]
assert q1(['sun', 'moon', 'star']) == [
    [],
    ['sun', 'moon', 'star']
]



def q2(sentence: str) -> List[str]:
    """
    Write the slice expression that extracts the last two words of text.

    Input: text = 'She received the news of the discovery with equanimity'
    Desired Output: ['with', 'equanimity']
    """


assert q2("She received the news of the discovery with equanimity") == ['with', 'equanimity']
assert q2("Hello world") == ['Hello', 'world']
assert q2("Python is very powerful") == ['very', 'powerful']
assert q2("Alone") == ['Alone']
assert q2("   spaces   everywhere   ") == ['spaces', 'everywhere']



def q3(sentence: str) -> List[str]:
    """
    Write a program to extract the email addresses present in the text.

    Input: text = 'Please contact us at contact@fpt.edu.vn for further information. You can also give feedback at feedback@fpt.edu.vn'
    Output: ['contact@fpt.edu.vn', 'feedback@fpt.edu.vn']
    """



assert q3(
    "Please contact us at contact@fpt.edu.vn for further information. "
    "You can also give feedback at feedback@fpt.edu.vn"
) == ['contact@fpt.edu.vn', 'feedback@fpt.edu.vn']
assert q3(
    "Send an email to admin@fpt.edu.vn"
) == ['admin@fpt.edu.vn']
assert q3(
    "Contact us at info@gmail.com or support@yahoo.com"
) == ['info@gmail.com', 'support@yahoo.com']
assert q3(
    "Emails: a@fpt.edu.vn,b-8@fpt.edu.vn;c.evn@fpt.edu.vn."
) == ['a@fpt.edu.vn', 'b-8@fpt.edu.vn', 'c.evn@fpt.edu.vn']
assert q3(
    "There is no email address here"
) == []



def q4(words: List[str]) -> List[str]:
    """
    Write a function that takes a list of words (containing duplicates) and returns a list of words (with no duplicates) sorted by decreasing frequency.

    Input: ['table', 'table', 'table', 'table', 'table', 'table', 'table', 'table', 'table', 'table', 'chair', 'chair', 'chair', 'chair', 'chair']
    Output: ['table', 'chair']
    """ 


assert q4([
    'table','table','table','table','table','table','table','table','table','table',
    'chair','chair','chair','chair','chair'
]) == ['table', 'chair']
assert q4(['apple','banana','cherry','banana','apple','cherry']) == ['apple', 'banana', 'cherry']
assert q4(['orange']) == ['orange']
assert q4(['cat','dog','dog','cat','cat','mouse','mouse','mouse','mouse']) == ['mouse','cat','dog']
assert q4([]) == []
assert q4(['kiwi','fig','fig','kiwi','pear','pear']) == ['fig','kiwi','pear']

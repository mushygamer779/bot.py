import random

'''def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password'''


def gen_pass(me = 8):
   
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(me):
        password += random.choice(elements)
    return password


def flip_coin():
    return random.choice(['heads','tails'])
    '''coin = random.choice([1,2]) 
    result = ''
    if coin == 1:
        result = 'heads'
    elif coin == 2:
        Rresult = 'tails'
    return result'''
def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result


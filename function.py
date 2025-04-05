import random

'''def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password'''


def gen_pass():
    me = int(input('how long?'))
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(me):
        password += random.choice(elements)
    return password

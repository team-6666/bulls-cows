import random

def numOfBullsCows(num,guess):
    bull_cow = [0,0]
    num_li = getDigits(num)
    guess_li = getdigits(guess)

    for i,j in zip(num_li,guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    # bull_cow return값 지정
    return bull_cow

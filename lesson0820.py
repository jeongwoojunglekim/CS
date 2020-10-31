# -*- coding: utf-8 -*-
"""ßßß
Created on Tue Aug 20 13:26:35 2019

@author: Administrator
"""

"""
채권 가격 계산 프로그램
원금 : 10000
yield : 0.04
n : 6
c : 100
이 때 채권의 가격을 구하시오.
"""

nominal = 10000
r = 0.04
n = 6
coupon = 100

price = coupon * (1 - (1 + r) ** -n) / r + nominal / (1 + r) ** n

print(price)

#%%

# List

list1 = [0, 0.4, [0, 1, 2]]

print(list1[2][2])

# Slicing, Range

# [start:end:step]
# range(100)
# range(10, 100)
# range(10, 100, 5)

#%%

# List Method

list2 = list(range(5))
#list2.append(-1)
#list2.extend([1,2,3])
#
#list2.sort()
#

list2[2] = 3
del list2[2]
# list 는 변환이 가능하
#%%
# Tuple

tuple1 = (1, 2, 3)
print(tuple1[0:2])

tuple1[1] = 100

list_tuple = list(tuple1)


#%%

# 함수
# def + 함수 이름 + 함수 인자 
def greeting(name):
    
    print("안녕하세요 " + name + "님")
    print("파이썬 수업에 오신것을 환영합니다")

greeting("김영욱")
greeting("신성민")
greeting("심형민")

#%%


# 함수, 그리고 리턴 
def bond_price(c, r, n, f):
    first_term = c * (1 - (1 + r) ** -n) / r 
    second_term = f / (1 + r) ** n
    
    return first_term + second_term
    
    

bond1 = bond_price(200, 0.04, 8, 10000)
bond2 = bond_price(150, 0.03, 1, 10000)
bond3 = bond_price(100, 0.10, 5, 10000)

print(bond_price(100, 0.04, 6, 10000))



#%% 
# module
from math import sin, pi

print(sin(pi / 2))

import math as m

print(m.sin(m.pi / 2))

#%% 
#
#import random as rn

from random import randint

def random_dice():
    print("주사위 놀이 - 결과")
    print(randint(1, 6))

random_dice()
random_dice()
random_dice()
random_dice()
random_dice()
random_dice()


#%%

from scipy.stats import norm
from numpy import log, exp


def black_scholes(s0, K, r, T, vol):
    
    d1 = (log(s0 / K) + (r + vol ** 2 / 2) * T) / (vol * T ** 0.5)
    d2 = d1 - vol * T ** 0.5
    
    price = s0 * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
    
    return price


print(black_scholes(100, 80, 0.03, 1, 0.10))


#%%


## 반복 
#for i in range(100):
#    print("hello world")

#
#for j in [10, 3, 4]:
#    print(j)
#    print("for 문 한바퀴")
#
#for c in "hello world":
##    print(c)
#
#for t in ("tuple", "list", "black" ,"scholes"):
#    print(t)
#
#for i in range(4):
#    print("*" * i)

#for i in range(4):
#    print(" " * (4 - i) + "*" * (2 * i + 1) )

# while
n = 0
while n < 5:
    print(" " * (5 - n) + "*" * n)
    n += 1    

#%%
# 조건문
def give(grade):
    print("당신의 학점은 " + grade + "입니다")

score = 75

def give_grade(score):
    if score > 90:
        give("A")
    elif 90 >= score and score > 80:
        give("B")
    elif 80 >= score and score > 70:
        give("C")
    else:
        give("D")
    
#
#scores = [75, 65, 81, 98, 51]
#for score in scores:
#    give_grade(score)
## 점수의 평균, 점수의 총합 


        

#%%
from random import randint
NUM_EXPERIMENT = 10000

trials = []

for i in range(NUM_EXPERIMENT):
    trial = 1
    prev = randint(1, 2)
    while True:
        trial = trial + 1
        cur = randint(1, 2)
        if prev == 1 and cur == 1:
            break
        else:
            prev = cur
    trials.append(trial)

print(sum(trials))
        






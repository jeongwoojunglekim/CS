# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:56:31 2019

@author: Administrator
"""
import random


file = open("./금융공학프로그램19사전교육.txt", encoding="utf-8")

# 파일을 읽는 방법
# 1. read
# 2. readlines
# 3. readline

# 두명 랜덤 선택 프로그램

# 1. 파일 읽기
# 2. 랜덤 두명 선택
from time import sleep

student_list = file.readlines()

def choice():
    return random.randint(1, 3)


students = random.sample(student_list, 2)
cnt = 1
for name in students:
    print("{}번째 학생은..".format(cnt))
    for i in range(1,2):
        sleep(1)
        print("."*i)
    print("{}입니다".format(name))
    cnt += 1





#%%





### 다음과 같은 출력을 하는 프로그램을 작성하세요.

# 예시
# 입력 --> 4
# 출력 -->
# 1
# 22
# 333
# 4444
#
#for i in range(1, 5):
#    print(str(i) * i)
#

def prob1(n):
    for i in range(1, n + 1):
        print(str(i) * i)

prob1(4)


#%%

# 주어진 두 숫자에 대해서 절대 거리를 계산하는 함수를 작성하세요

# 예시
# 입력 5, 17
# 출력 12
# 입력 0 -3
# 출력 3
def distance(x, y):
    if y > x:
        print((x - y) * -1)
    else:
        print(x - y)

print(abs(3 - 17))

#%% 

# 구구단 출력

# 구구단을 1단부터 9단까지 작성하세

# 6 x 7 = 42
#for i in range(2, 10):
#    for j in range(1, 10):
#        if j == 9:
#            print(i * j)
#        else:
#            print(i * j, end = " ")
#

for a in range(1, 10):
    print("")
    for b in range(1, 10):
        print(a, "x", b, "=", a*b, " ", end="")

#%%

# 삼각형인지 아닌지 보는 함수


# 임의의 세 양의 실수를 입력 받아 세 수가 삼각형을 만들 수 있는지 확인하시오
        
def istriangle(a, b, c):
    edges = [a, b, c]
    edges.sort()
    return edges[2] < (edges[0] + edges[1])





istriangle(3, 2, 3)

#%%

# datetime

# 오늘, 내일 ,어제 
from datetime import datetime, timedelta

today = datetime.now()

year, month, day = today.year, today.month, today.day

yesterday = datetime(year, month, day - 1)
tomorrow = datetime(year, month, day + 1)
print(today, yesterday, tomorrow)


#%%

# standard normal distribution 에서 임의로 추출한 수가
# 1.96 이상일 확률을 구해라 



from numpy.random import normal

NUM_SIMUL = 100000
samples = normal(size=NUM_SIMUL)


sum(samples > 1.96) / NUM_SIMUL



#%%

# dictionary

# 두 딕셔너리의 공통 키값을 가진 값들을 더해서 새로운 딕셔너리를 만들어라
# 예시
new_a = {"a" : 30, "e" : 40, "c" : 10}
new_b = {"a" : 10, "b" : 30, "d" : 30}
#
#n = 0
#for i in range(len(list(a))):
#    if list(a)[i] in list(b):
#        n = n + 1
result_dict = {}
for key_a in a:
    if key_a in b:
        result_dict[key_a] = a[key_a] + b[key_a]
    else:
        result_dict[key_a] = a[key_a]

for key_b in b:
    if key_b in a:
        result_dict[key_b] = a[key_b] + b[key_b]
    else:
        result_dict[key_b] = b[key_b]

def counter(d1, d2):
    rd = {}
    for key_1 in d1:
        if key_1 in d2:
            rd[key_1] = d1[key_1] + d2[key_1]
        else:
            rd[key_1] = d1[key_1]
    for key_2 in d2:
        if key_2 in d1:
            rd[key_2] = d1[key_2] + d2[key_2]
        else:
            rd[key_2] = d2[key_2]
            
    return rd

counter(new_a, new_b)
#%%

from collections import Counter
new_a = {"a" : 30, "e" : 40, "c" : 10}
new_b = {"a" : 10, "b" : 30, "d" : 30}
c1 = Counter(new_a)
c2 = Counter(new_b)

c1 + c2




# d3 = {a : 40, b: 70, c : 10, d : 30}

    

#%% 
import numpy as np
def normal():
    total_trial = 0
    event = 0
    while total_trial < 1000:
        if np.random.normal() > 1.96:
            event = event + 1
        total_trial = total_trial + 1
    return event / total_trial

normal()
            
#%%
            
import numpy as np
cnt = 0
for i in range(1000000):
    if np.random.normal(0, 1) > 1.96:
        cnt += 1
print(100 * cnt / 1000000)



#%%

# 주어진 문장 속에 문자의 개수를 딕셔너리로 저장하는 프로그램을 만드세요

# 예시
# 'thequickbrownfoxjumpsoverthelazydog'
# -> o : 4, e : 3, u : 2, h : 2, r : 2, t : 2 
# 

#%%

# 주어진 리스트에서 중복값을 제거한 리스트를 리턴하세요.
# 예시
# [1,1,1,1, 2,2, 3,3,3,3, 4,4,4] --> [1,2,3,4]
# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  分发扑克牌
   Description :  AIM: 
                  Functions: 1. 
                             2. 
   Envs        :  python == 
                  pip install  -i https://pypi.douban.com/simple 
   Author      :  errol
   Date        :  2020/5/12  10:14
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2020/5/12 : 新建
-------------------------------------------------
'''


import random
import operator
def auto():
  pokers=[]
  poker=[]
  for i in ['♥','♠','♦','♣']:
    for j in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
      poker.append(i)
      poker.append(j)
      pokers.append(poker)
      poker=[]
  return pokers
poker=auto()
random.shuffle(poker)
li={}
for k in ['player1','player2','player3','player4']:
  b=random.sample(poker,13)
  for s in b:
    poker.remove(s)
  li.setdefault(k,b)
print('player1：',sorted(li['player1'],key=operator.itemgetter(0,1)))
print('player2：',sorted(li['player2'],key=operator.itemgetter(0,1)))
print('player3：',sorted(li['player3'],key=operator.itemgetter(0,1)))
print('player4：',sorted(li['player4'],key=operator.itemgetter(0,1)))

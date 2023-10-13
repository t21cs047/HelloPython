'''
Created on 2023/10/13

@author: t21cs047
'''

import random

def janken(player_a, player_b):
    count = 0
    
    hands = ["グー", "チョキ", "パー"]
    
    for i in range (3):
    # プレイヤーの手をランダムに生成
        hand_a = random.randint(0, 2)
        hand_b = random.randint(0, 2)

    # プレイヤーの手を表示
        print(player_a,f"の手: {hands[hand_a]} v.s.", player_b,f"の手: {hands[hand_b]}")

    # 勝敗判定
        result = (hand_a - hand_b + 3) % 3
        if result == 0:
            print("引き分け")
        elif result == 1:
            print(player_b,"の勝ち")
            count -= 1
        else:
            print(player_a,"の勝ち")
            count += 1
        
    if count == 0:
        print("総合結果　引き分け")
    elif count < 0:
        print("総合結果　",player_b,"の勝ち")
    else:
        print("総合結果　",player_a,"の勝ち")
        
        
janken("A", "B")
        
        
        
        
"""
def janken_3(player_a, player_b,player_c):
    count = 0
    
    hands = ["グー", "チョキ", "パー"]
    
    
    # プレイヤーの手をランダムに生成
    hand_a = random.randint(0, 2)
    hand_b = random.randint(0, 2)
    hand_c = random.randint(0, 2)

    # プレイヤーの手を表示
    print(player_a,f"の手: {hands[hand_a]} v.s.", player_b,f"の手: {hands[hand_b]} v.s.",player_c,f"の手: {hands[hand_c]} ")

    # 勝敗判定
    result1 = (hand_a - hand_b + 3) % 3
    result2 = (hand_a - hand_c + 3) % 3
    
    
    if result1 == result2:
        
        print("引き分け")
    elif result == 1:
        print(player_b,"の勝ち")
        count -= 1
    else:
        print(player_a,"の勝ち")
        count += 1"""
        
   
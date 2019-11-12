##?????????
import random
import time

## ????
card_model = ('武则天','嬴政','诸葛亮','宫本武藏','李白')

## ????
card_bag = { }

## ??????
card_list =  [5,10,20,50,100]

## ??????
card_num = [5,15,35,85,185]

## ???
while 1:
    ## ?????????
    master = int(input('''
    抽卡小游戏，普通玩家请氪金！
    请输入你的指令：
    1. 抽卡
    2. 查看背包
    3. 离开
    '''))

    ## ????? 1 ?????????
    if master == 1:
        num = int(input('请输入抽卡次数'))
        ## ?????????????
        for i in range(0,num):
            randcard = random.randint(1,card_num[-1])
            i = 0
            while randcard  > card_num[i]:
                i += 1
            print('你抽到的卡是: {}'.format(card_model[i]))

            if card_bag.get(card_model[i]):
                card_bag[card_model[i]] += 1
            else :
                card_bag[card_model[i]] = 1
            time.sleep(0.3)

        ## ??????????????
        print('卡已存入背包')
        print('________________')

    ## ????? 2???????
    if master == 2:
        ## ????????????????
        if len(card_bag) == 0:
            print('你的背包里没有卡片，请先抽卡')
            print('________________')
        else:
            for key,value in card_bag.items():
                print('{} - 数量:{}'.format(key,value))
            print('________________')


    ## ????? 3?????
    if master == 3:
        break


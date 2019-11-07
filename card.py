import random
##导入随机库

card_model = ('张三','李四','王麻子','老五','老张')
##定义卡池的数量和种类

user_card = []

while 1 :
	master = int(input('''
	抽卡小游戏，普通玩家请先氪金。
	请选择你需要的功能
	1：抽卡，并输入你需要的次数
	2：查看自己的背包已有卡类
	3：整理背包
	4：退出游戏
	'''))
##进入循环，开始游戏

	if master == 1:
		num = int(input('请输入需要抽奖的次数：'))
		for i in range(0,num):
			n = random.randint(0,4)
			print('你抽到了卡片有：{}'.format(card_model[n]))		
			user_card.append(card_model[n])
			##使用随机参数，获取一个随机整数
			##整数在序组里不大于卡池数，随机抽取卡池的序号赋值给用户卡组user_card
			
	if master == 2:
		if len(user_card)==0 :
			print('你的背包里没有卡片，请先抽卡')
			##背包里无卡提示。
		else :
			for i in user_card :
				print(i)
			##背包里有卡提示。
			
	if master == 3:
		if len(user_card)==0 :
			print('你的背包里没有卡片，请先抽卡')
		##背包里无卡提示。
		else :
			user_card.sort()
			for i in user_card:
				print(i)
		##整理背包，并打印背包内容
	if master == 4 :
		break

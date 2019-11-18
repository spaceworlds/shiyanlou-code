##原始收入，获取用户输入
yssr = int(input('请输入你的薪资:'))

##税后收入
shsr = 0

##应交所得税额
yjsds = 0

#纳税金额
nsje = 0

def calculator(num):
	yjsds = num - 5000
	if yjsds <= 0 :
		nsje = 0
	elif 0 < yjsds <= 3000:
		nsje = yjsds * 0.03 -0
	elif 3000 < yjsds <= 12000:
		nsje = yjsds * 0.1 - 210
	elif 12000 < yjsds <= 25000:
		nsje = yjsds * 0.2 - 1410
	elif 25000 < yjsds <= 35000:
		nsje = yjsds * 0.25 - 2660
	elif 35000 < yjsds <= 55000:
		nsje = yjsds * 0.3 - 4410
	elif 55000 < yjsds <= 80000:
		nsje = yjsds * 0.35 -7160
	else :
		nsje = yjsds * 0.45 - 15160
	shsr = yssr - nsje
	return '{:.2f}'.format(shsr)
	
print('你的税后收入是:{}'.format(calculator(yssr)))

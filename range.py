# range 範圍
# python內建清單產生器
import random

range(6)

for i in range(6):
	r = random.randint(1, 49)
	print('這是第', i + 1, '組大樂透號碼:', r)
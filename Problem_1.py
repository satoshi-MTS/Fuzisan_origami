# 富士山の高さ
HEIGHT_OF_MT_FUZI = 3776
# 厚さの初期値
THICKNESS = 0.00008
# 折った回数
number_of_folding = 0
# 折る紙の厚さの初期値
height = THICKNESS

# 計算
while height < HEIGHT_OF_MT_FUZI:
	height = THICKNESS * (2 ** number_of_folding)
	number_of_folding += 1

# 結果の表示
print('厚さ{}の紙を{}回折ると富士山の高さを超えます'.format(THICKNESS, number_of_folding))


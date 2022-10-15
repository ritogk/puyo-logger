# 画像認識サンプル2
import cv2

# 動画の開始フレーム
frameIndex = 10000
# frameIndex = 16912

# 動画読み込み
cap = cv2.VideoCapture("puyo_video.mp4")
cap.set(cv2.CAP_PROP_POS_FRAMES, frameIndex)
ref, frame = cap.read()
# img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGRA)
img = frame

# トリミング
field = img[30: 335, 90: 250]

row_1 = field[255: 276, 8: 150]
row_2 = field[233: 254, 8: 150]
row_3 = field[211: 232, 8: 150]
row_4 = field[188: 210, 8: 150]
row_5 = field[165: 187, 8: 150]
row_6 = field[142: 164, 8: 150]
row_7 = field[119: 141, 8: 150]
row_8 = field[96: 118, 8: 150]
row_9 = field[73: 95, 8: 150]
row_10 = field[50: 72, 8: 150]
row_11 = field[27: 49, 8: 150]
row_12 = field[4: 26, 8: 150]

field_1_1 = row_1[0: 22, 0: 24]
field_1_2 = row_1[0: 22, 24: 48]
field_1_3 = row_1[0: 22, 48: 72]
field_1_4 = row_1[0: 22, 72: 96]
field_1_5 = row_1[0: 22, 96: 120]
field_1_6 = row_1[0: 22, 120: 144]

field_2_1 = row_2[0: 22, 0: 24]
field_2_2 = row_2[0: 22, 24: 48]
field_2_3 = row_2[0: 22, 48: 72]
field_2_4 = row_2[0: 22, 72: 96]
field_2_5 = row_2[0: 22, 96: 120]
field_2_6 = row_2[0: 22, 120: 144]

field_3_1 = row_3[0: 22, 0: 24]
field_3_2 = row_3[0: 22, 24: 48]
field_3_3 = row_3[0: 22, 48: 72]
field_3_4 = row_3[0: 22, 72: 96]
field_3_5 = row_3[0: 22, 96: 120]
field_3_6 = row_3[0: 22, 120: 144]


field_4_1 = row_4[0: 22, 0: 24]
field_4_2 = row_4[0: 22, 24: 48]
field_4_3 = row_4[0: 22, 48: 72]
field_4_4 = row_4[0: 22, 72: 96]
field_4_5 = row_4[0: 22, 96: 120]
field_4_6 = row_4[0: 22, 120: 144]

field_5_1 = row_5[0: 22, 0: 24]
field_5_2 = row_5[0: 22, 24: 48]
field_5_3 = row_5[0: 22, 48: 72]
field_5_4 = row_5[0: 22, 72: 96]
field_5_5 = row_5[0: 22, 96: 120]
field_5_6 = row_5[0: 22, 120: 144]

field_6_1 = row_6[0: 22, 0: 24]
field_6_2 = row_6[0: 22, 24: 48]
field_6_3 = row_6[0: 22, 48: 72]
field_6_4 = row_6[0: 22, 72: 96]
field_6_5 = row_6[0: 22, 96: 120]
field_6_6 = row_6[0: 22, 120: 144]

field_7_1 = row_7[0: 22, 0: 24]
field_7_2 = row_7[0: 22, 24: 48]
field_7_3 = row_7[0: 22, 48: 72]
field_7_4 = row_7[0: 22, 72: 96]
field_7_5 = row_7[0: 22, 96: 120]
field_7_6 = row_7[0: 22, 120: 144]

field_8_1 = row_8[0: 22, 0: 24]
field_8_2 = row_8[0: 22, 24: 48]
field_8_3 = row_8[0: 22, 48: 72]
field_8_4 = row_8[0: 22, 72: 96]
field_8_5 = row_8[0: 22, 96: 120]
field_8_6 = row_8[0: 22, 120: 144]

field_9_1 = row_9[0: 22, 0: 24]
field_9_2 = row_9[0: 22, 24: 48]
field_9_3 = row_9[0: 22, 48: 72]
field_9_4 = row_9[0: 22, 72: 96]
field_9_5 = row_9[0: 22, 96: 120]
field_9_6 = row_9[0: 22, 120: 144]

field_10_1 = row_10[0: 22, 0: 24]
field_10_2 = row_10[0: 22, 24: 48]
field_10_3 = row_10[0: 22, 48: 72]
field_10_4 = row_10[0: 22, 72: 96]
field_10_5 = row_10[0: 22, 96: 120]
field_10_6 = row_10[0: 22, 120: 144]

field_11_1 = row_11[0: 22, 0: 24]
field_11_2 = row_11[0: 22, 24: 48]
field_11_3 = row_11[0: 22, 48: 72]
field_11_4 = row_11[0: 22, 72: 96]
field_11_5 = row_11[0: 22, 96: 120]
field_11_6 = row_11[0: 22, 120: 144]

field_12_1 = row_12[0: 22, 0: 24]
field_12_2 = row_12[0: 22, 24: 48]
field_12_3 = row_12[0: 22, 48: 72]
field_12_4 = row_12[0: 22, 72: 96]
field_12_5 = row_12[0: 22, 96: 120]
field_12_6 = row_12[0: 22, 120: 144]

field_list = [
    [field_1_1, field_1_2, field_1_3, field_1_4, field_1_5, field_1_6],
    [field_2_1, field_2_2, field_2_3, field_2_4, field_2_5, field_2_6],
    [field_3_1, field_3_2, field_3_3, field_3_4, field_3_5, field_3_6],
    [field_4_1, field_4_2, field_4_3, field_4_4, field_4_5, field_4_6],
    [field_5_1, field_5_2, field_5_3, field_5_4, field_5_5, field_5_6],
    [field_6_1, field_6_2, field_6_3, field_6_4, field_6_5, field_6_6],
    [field_7_1, field_7_2, field_7_3, field_7_4, field_7_5, field_7_6],
    [field_8_1, field_8_2, field_8_3, field_8_4, field_8_5, field_8_6],
    [field_9_1, field_9_2, field_9_3, field_9_4, field_9_5, field_9_6],
    [field_10_1, field_10_2, field_10_3, field_10_4, field_10_5, field_10_6],
    [field_11_1, field_11_2, field_11_3, field_11_4, field_11_5, field_11_6],
    [field_12_1, field_12_2, field_12_3, field_12_4, field_12_5, field_12_6],
]

frameIndex = 16912
# 動画読み込み
cap = cv2.VideoCapture("puyo_video.mp4")
cap.set(cv2.CAP_PROP_POS_FRAMES, frameIndex)
ref, frame = cap.read()
img = frame

# トリミング
field = img[30: 335, 90: 250]
row2_3 = field[211: 232, 8: 150]

field_3_4 = row2_3[0: 22, 72: 96]

puyo_green = field_1_4
puyo_red = field_2_4
puyo_yellow = field_8_1
puyo_parerpul = field_3_1
puyo_ozyama = field_5_6
puyo_blue = field_3_4

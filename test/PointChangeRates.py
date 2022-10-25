from os import major
import cv2
import matplotlib.pyplot as plt
import numpy as np


class PointChangeRates:
    # ぷよを消したタイミングのフレームを取得する
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path

    def conversion(self):
        # 動画読み込み
        cap = cv2.VideoCapture(self.video_path)

        fps = cap.get(cv2.CAP_PROP_FPS)
        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        # 動画から画像を抽出
        frames = []
        while True:
            # generator にしたほうが使いやすい
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        # ツモ部分のみ抽出
        point_frames = []
        for frame in frames:
            point_frames.append(frame[310: 335, 105: 239])

        # グレースケール変換
        gray_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                       for f in point_frames]

        # 全フレームの差分を計算
        diff_frames = [cv2.absdiff(aft, bef) for bef, aft in zip(
            gray_frames, gray_frames[1:])]
        # 2値化して計算しやすくする。
        th = 40  # しきい値
        for i, x in enumerate(diff_frames):
            x[x < th] = 0
            x[x >= th] = 1
            diff_frames[i] = x

        area = w * h  # １フレームのピクセル数
        # フレーム間の変化率を計算
        # ※１フレームのピクセル数と「２値化した変化ピクセル？」から変化率を求める
        # Maxは1, Minは0
        diff_rates = np.array([(d != 0).sum() / area for d in diff_frames])

        # 変化率の平均
        mean = diff_rates.mean()
        # 変化率の中央値
        median = np.median(diff_rates)

        # 連鎖と関係のない変化率を消す
        change_frames = []
        for i, diff_rate in enumerate(diff_rates):
            frame_no = i
            if diff_rate > 0.0035:
                change_frames.append(frame_no)

        chain_frame = []
        a = 0
        for i, change_frame in enumerate(change_frames):
            if i >= a:
                chain_frame.append(change_frame)
                a = i + 2

        return chain_frame

from os import major
import cv2
import numpy as np


class TumoChangeRates:
    # ツモったタイミングのフレームを取得する
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path

    def conversion(self):
        # 動画読み込み
        cap = cv2.VideoCapture(self.video_path)

        fps = cap.get(cv2.CAP_PROP_FPS)
        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        sec = frame_count / fps

        # 動画から画像を抽出
        frames = []
        while True:
            # generator にしたほうが使いやすい
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)

        # ツモ部分のみ抽出
        tumo_frames = []
        for frame in frames:
            tumo_frames.append(frame[35: 138, 256: 315])

        # グレースケール変換
        gray_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                       for f in tumo_frames]

        # 全フレームの差分を計算
        diff_frames = [cv2.absdiff(aft, bef)
                       for bef, aft in zip(gray_frames, gray_frames[1:])]
        # 2値化して計算しやすくする。
        th = 30  # しきい値
        for i, x in enumerate(diff_frames):
            x[x < th] = 0
            x[x >= th] = 1
            diff_frames[i] = x
        n_diff_pixels = (diff_frames[0] != 0).sum()

        area = w * h  # １フレームのピクセル数
        # フレーム間の変化率を計算
        # ※１フレームのピクセル数と「２値化した変化ピクセル？」から変化率を求める
        # Maxは1, Minは0
        diff_rates = np.array([(d != 0).sum() / area for d in diff_frames])

        # 変化率の平均
        mean = diff_rates.mean()
        # 変化率の中央値
        median = np.median(diff_rates)

        tumo_frame_no_list = []

        max = 0.0065
        min = 0.0035
        max_tumo_frame_range = 6

        a = -1

        # フレーム間で全く変わらない場合があるのでその考慮
        # 連続していない0は消す。
        hairetu = []
        next = 1
        for i, x in enumerate(diff_rates):
            if diff_rates.size == i + 1:
                break
            if diff_rates[i] == 0 and diff_rates[i+1] != 0:
                diff_rates[i] = diff_rates[i+1]

        # ツモ判定
        for i, x in enumerate(diff_rates):
            if x == 0 or i <= a:
                continue
            frame_no = i

            next_zero_frame = np.where(diff_rates[i:] == 0)[0][0] + i

            range_frame = np.array(diff_rates[frame_no: next_zero_frame])
            result = range_frame[np.where(
                (range_frame > min) & (range_frame < max))]

            first = range_frame[0]
            end = range_frame[-1]
            mannaka = range_frame[int(range_frame.size / 2)]

            max_value = range_frame.max()

            value = max_value * (3 / 4)

            if result.size >= 3 and mannaka < value:
                # print(i)
                a = i + result.size
                tumo_frame_no_list.append(i)

        return tumo_frame_no_list

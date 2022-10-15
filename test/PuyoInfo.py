from FieldRecognition import FieldRecognition

field_recogniton = FieldRecognition(
    video_path='./resources/puyo_video.mp4', frame_index=15500)

field_recogniton2 = FieldRecognition(
    video_path='./resources/puyo_video.mp4', frame_index=9900)

puyo_red = field_recogniton.field_img_list[0][5]
puyo_yellow = field_recogniton.field_img_list[0][1]
puyo_blue = field_recogniton.field_img_list[3][1]
puyo_parpul = field_recogniton.field_img_list[2][1]
puyo_green = field_recogniton2.field_img_list[0][3]
puyo_ozyama = field_recogniton.field_img_list[7][2]

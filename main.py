import time

from yolov5_dnn import mult_test
import cv2
if __name__ == "__main__":
    # print(cv2.__version__)
    # onnx_path = './weights/yolov5n.onnx'
    # onnx_path = './weights/yolov5s.onnx'
    onnx_path = './weights/yolov5s_house.onnx'

    # onnx_path = './weights/mymodel.onnx'
    input_path = './test_img'
    # save_path = './output_image'
    save_path = './test_img2'


    # video=True代表开启摄像头
    # mult_test(onnx_path, input_path, save_path, video=False)
    print("正在执行...")
    while True:
        mult_test(onnx_path, input_path, save_path, video=False)
        time.sleep(30)

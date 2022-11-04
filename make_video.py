import random as rd
import cv2
import os
import numpy as np

path = '/home/car/exps/OpenPCDet/tools/jpg'   # image path


class RecordMovie(object):

    def __init__(self, img_width, img_height):
        self.video_writer = None  # 视频对象
        self.is_end = False  # 结束保存视频
        self.img_width = img_width  # 宽度
        self.img_height = img_height  # 高度
        self.freq = 5    # frames per second

    # 创建 视频写入对象
    def start(self, file_name):
        # 创建视频格式
        four_cc = cv2.VideoWriter_fourcc(*'mp4v')
        img_size = (self.img_width, self.img_height)  # 视频尺寸

        # 创建视频写入对象
        self.video_writer = cv2.VideoWriter()
        self.video_writer.open(file_name, four_cc, self.freq, img_size, True)

    # write image into frame
    def record(self, img):
        if self.is_end is False:
            self.video_writer.write(img)


    # 完成视频 释放资源
    def end(self):
        self.is_end = True
        self.video_writer.release()


def main():
    # 1.读取第一张图片确定视频的高和宽

    filelist = os.listdir(path)
    filelist.sort()
    filelist = filelist[30:]

    img0 = os.path.join(path, filelist[0])
    img_org = cv2.imread(img0, cv2.IMREAD_GRAYSCALE)

    # 2.显示图片
    cv2.imshow("org", img_org)
    cv2.namedWindow("shift")

    # 3.视频文件生成
    height, width = img_org.shape[:2]
    print(height, width)
    rm = RecordMovie(width, height)

    # 设置视频文件名称 频率
    rm.start("test.mp4", 5)

    # 4.图片写入视频
    for i in range(len(filelist)):
        item = os.path.join(path, filelist[i])
        img = cv2.imread(item)
        rm.record(img)
        cv2.imshow("shift", img)
        key = cv2.waitKey(10)
        # esc 按键
        if key == 27:
            break

    # 5.关闭视频文件
    rm.end()


if __name__ == '__main__':
    main()

#coding=utf-8
import numpy as np

video_file_path="numpy_dem/video.csv"
video_1_file_path="numpy_dem/video.csv"

video_loadtxt = np.loadtxt(video_file_path, delimiter=",",dtype="int")
#unpack 转置
video_loadtxt_1 = np.loadtxt(video_file_path, delimiter=",",dtype="int",unpack=True)
print(video_loadtxt)
print(video_loadtxt_1)

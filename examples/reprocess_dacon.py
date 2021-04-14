from matplotlib import pyplot as plt
import json
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
keypoints = []
box = []
i = 0
tmp_1 = [0 for j in range(1650)]
for file_name in glob("/home/jinyoung/share/AlphaPose/result_dacon_test/*"):
    loca = os.path.basename(file_name)
    video_name = os.path.splitext(loca)[0]
    file_n = os.path.join(file_name,"alphapose-results.json")
    print(video_name)
    with open(file_n,"r") as alpha:
        data = json.load(alpha)
    #data = np.array(data)
    data_len = len(data)
    #print(data_len)
    tmp_box = [[0 for col in range(1)] for row in range(10)]
    tmp_list = [[0 for col in range(1)] for row in range(10)]
    #print(data_len)
    image_id = os.path.splitext(data[0]['image_id'])[0]
    keypoints = data[0]['keypoints']
    box = data[0]['box']
    tmp_list=keypoints
    tmp_box=box
    #print(tmp_list)
    #print(len(tmp_box))
    #print(tmp_list)
    tmp_1[i] = {'name':video_name, 'keypoints':tmp_list, 'box':tmp_box}
    #tmp_1 = {'keypoints':tmp_list, 'box':tmp_box}
    #pickle.dump

    print(video_name + 'DONE!') 
    i = i+1
print(tmp_1[1599])
with open("output_test.json", "w") as f:  
    json.dump(tmp_1, f, indent=2)
    #print(tmp_1['box'])
    #print(len(tmp_1['box']))
    #print(len(tmp_1['keypoints'][0]))
    #os.mkdir("/home/wlsdud7907/github/PyTorch_Speaker_Verification/seoul_mal/kws_DB/TRAIN/%s"%dd)
    #os.mkdir("/home/nas/DB/JY_VoxCeleb1/TES"%dd)
    #aa=glob("%s/*/*.wav"%pp)
    #print(i)
    #print("%s\n"%loca)
    #i = i+1
    #command = ("python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/fast_res50_256x192.pth --video /home/jinyoung/share/AlphaPose/example_videos/wxdRVAZk_0.avi")
    #output = subprocess.call(command, shell=True, stdout=None)
    
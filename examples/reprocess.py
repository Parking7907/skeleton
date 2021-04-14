from matplotlib import pyplot as plt
import json
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
keypoints = []
box = []
for file_name in glob("/home/jinyoung/share/AlphaPose/result_train_fight/*"):
    loca = os.path.basename(file_name)
    video_name = os.path.splitext(loca)[0]
    file_n = os.path.join(file_name,"alphapose-results.json")
    print(video_name)
    with open(file_n,"r") as alpha:
        data = json.load(alpha)
    #data = np.array(data)
    data_len = len(data)
    #print(data_len)
    tmp_box = [[0 for col in range(1)] for row in range(150)]
    tmp_list = [[0 for col in range(1)] for row in range(150)]
    #print(data_len)
    for i in range(data_len):
        image_id = int(os.path.splitext(data[i]['image_id'])[0])
        keypoints = data[i]['keypoints']
        box = data[i]['box']
        #print(box)
        #print(image_id)
        #print(keypoints)
        #tmp_list = np.append([tmp_list,keypoints], axis=0)
        #print(tmp_list[image_id])
        if tmp_list[image_id] == [0]:
            tmp_list[image_id][0]=keypoints
        elif tmp_list[image_id] != [0]:
            tmp_list[image_id].append(keypoints)
        if tmp_box[image_id] == [0]:
            tmp_box[image_id][0]=box
        elif tmp_box[image_id] != [0]:
            tmp_box[image_id].append(box)
    #print(tmp_list)
    #print(len(tmp_box))
    #print(tmp_list)
    #tmp_1 = {'name':video_name, 'keypoints':tmp_list, 'box':tmp_box}
    tmp_1 = {'keypoints':tmp_list, 'box':tmp_box}
    #pickle.dump
    with open('train/Fight/'+video_name+'.pkl', 'wb') as f:  
        pickle.dump(tmp_1, f)
    print(video_name + 'DONE!') 
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
    
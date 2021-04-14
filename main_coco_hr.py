from matplotlib import pyplot as plt
import pandas as pd
import json
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
#pdb.set_trace()



################################################################################################################################################################################################

def run_alphapose(new):

    for image_name in new:
        print(image_name)
        image_n = os.path.basename(image_name)
        #command = ("./scripts/inference.sh ./configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml pretrained_models/halpe26_fast_res50_256x192.pth %s ./result_dacon_test/%s "%(image_name,image_n))
        #COCO 17-Fast Pose (DUC) ResNet152
        command = ("./scripts/inference.sh configs/coco/hrnet/256x192_w32_lr1e-3.yaml pretrained_models/hrnet_w32_256x192.pth %s ./result_dacon_test_coco_hr/%s"%(image_name,image_n))
        output = subprocess.call(command, shell=True, stdout=None)


def json_process():
    k = 0
    tmp_1 = [0 for pp in range(1600)]
    for file_name in glob("./result_dacon_test_coco_hr/*"):
        loca = os.path.basename(file_name)
        #pdb.set_trace()
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
        #print(image_id)
        keypoints = data[0]['keypoints']
        box = data[0]['box']
        tmp_list=keypoints
        tmp_box=box
        #print(len(tmp_box))
        tmp_1[k] = {'name':video_name, 'keypoints':tmp_list, 'box':tmp_box}
        #tmp_1 = {'keypoints':tmp_list, 'box':tmp_box}
        #pickle.dump
        print(video_name + 'DONE!') 
        k = k+1
        
    #print(tmp_1)
    with open("output_test_coco_hr.json", "w") as f:  
        json.dump(tmp_1, f, indent=2)

#####################################################################################################################################################################################################


def json_to_csv():
    with open("output_test_coco_hr.json", "r") as alpha:
        data = json.load(alpha)
    #data_ = np.array(data)
    #print(data)
    #print(data[0]['keypoints'])
    print(len(data))
    x = []
    y = [[0 for col in range(49)] for row in range(1600)]
    #print(y)
    #point_24 = []
    #data reformation
    for f in range(1600):
        x.append(data[f]['keypoints'])
        #y.append(data[f]['keypoints'])
        del x[f][2:51:3]
        #print(x[f])
        #print(len(x[f]))
        #print(len(y[f]))
        #0~16 == Halpe
        y[f][0] = data[f]['name'] + '.jpg'
        y[f][1:35] = x[f][0:34]
        #17(neck) = (5+6)/2
        y[f][35] = (x[f][10] + x[f][12])/2 
        y[f][36] = (x[f][11] + x[f][13])/2
        #18(l palm) == 9(l wrist)
        y[f][37] = (x[f][18]*10 - x[f][14])/9
        y[f][38] = (x[f][19]*10 - x[f][15])/9
        #19(r palm) = 8(r elbow) 10(r wrist) 10:1 External Division
        y[f][39] = (x[f][20]*10 - x[f][16])/9
        y[f][40] = (x[f][21]*10 - x[f][17])/9
        #20(spine2) = (11+12)/4 + (5+6)/3
        y[f][41] = (x[f][22] + x[f][24])/6 + (x[f][10] + x[f][12])/3
        y[f][42] = (x[f][23] + x[f][25])/6 + (x[f][11] + x[f][13])/3
        #21(spine1) = (11+12)/3 + (5+6)/6
        y[f][43] = x[f][22]/3 + x[f][24]/3 + (x[f][10] + x[f][12])/6
        y[f][44] = x[f][23]/3 + x[f][25]/3 + (x[f][11] + x[f][13])/6
        #22(L instep) = 13, 15 10:1 External Division
        y[f][45] = (x[f][30]*10 - x[f][26])/9
        y[f][46] = (x[f][31]*10 - x[f][27])/9
        #23(R instep) = 14, 16 10:1 External Division
        y[f][47] = (x[f][32]*10 - x[f][28])/9
        y[f][48] = (x[f][33]*10 - x[f][29])/9
    #print(len(x))
    #print(len(y))
    return y

def csv_write(data):
    sample = pd.read_csv("sample_submission.csv")
    #print(sample.iloc[0][35:37])
    #print(sample['image'])
    for f in range(1600):
        image_name = data[f][0]
        print(image_name)
        #print(sample.loc[f]['image'])
        #print(sample.loc[sample['image'] == image_name])
        sample.loc[sample['image']==image_name] = y[f]
        
    sample.to_csv('baseline_submission_coco_hr.csv', index=False)

#######################################################################################################################################################################################

if __name__ == '__main__':
    new = glob("./data/Dacon/test_imgs/*")
    #run_alphapose(new)
    json_process()
    y = json_to_csv()
    csv_write(y)



from matplotlib import pyplot as plt
import pandas as pd
import json
import sys, time, os, pdb, argparse, pickle, subprocess
from glob import glob
import numpy as np
from shutil import rmtree
#pdb.set_trace()
new = glob("./result_dacon_test_coco_dcn/*")
for image_name in new:
    #print(image_name)
    image_n = os.path.basename(image_name)
    file_n = os.path.join(image_name,"vis/0.jpg")
    print("%s/vis/%s"%(image_name, image_n))
    #command = ("./scripts/inference.sh ./configs/halpe_26/resnet/256x192_res50_lr1e-3_1x.yaml pretrained_models/halpe26_fast_res50_256x192.pth %s ./result_dacon_test/%s "%(image_name,image_n))
    #COCO 17-Fast Pose (DUC) ResNet152
    #command = ("mv %s %s/vis/%s"%(file_n, image_name, image_n))
    command = ("mv %s/vis/%s ./reso "%(image_name, image_n))

    output = subprocess.call(command, shell=True, stdout=None)


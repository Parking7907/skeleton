# skeleton

Based on DACON Challenge : https://dacon.io/competitions/official/235701/overview/description/  
Datas can be downloaded on DACON Challenge webpage above as well  
to run the code, test datas must be at skeleton/data/Dacon/test_imgs  
code can be run in several versions of alphapose, based on COCO17, halpe27 keypoints.


### task : to find 24 points useful for exercise motion detection

used COCO17 as baselines, added new points with hard-coded rules
![image](https://user-images.githubusercontent.com/52812373/114645753-fe857d00-9d14-11eb-8e92-7962485c980c.png)

        #0~16 == Halpe
        y[f][0] = data[f]['name'] + '.jpg'
        y[f][1:35] = x[f][0:34]
        #17(neck) = (5+6)/2
        y[f][35] = (x[f][10] + x[f][12])/2 
        y[f][36] = (x[f][11] + x[f][13])/2
        #18(l palm) == 9(l wrist)
        y[f][37] = (x[f][18]*10 - x[f][14])/9
        y[f][38] = (x[f][19]*10 - x[f][15])/9
        #19(r palm) == 10(r wrist)
        y[f][39] = (x[f][20]*10 - x[f][16])/9
        y[f][40] = (x[f][21]*10 - x[f][17])/9
        #20(spine2) = (11+12)/4 + (5+6)/3
        y[f][41] = (x[f][22] + x[f][24])/6 + (x[f][10] + x[f][12])/3
        y[f][42] = (x[f][23] + x[f][25])/6 + (x[f][11] + x[f][13])/3
        #21(spine1) = (11+12)/3 + (5+6)/6
        y[f][43] = x[f][22]/3 + x[f][24]/3 + (x[f][10] + x[f][12])/6
        y[f][44] = x[f][23]/3 + x[f][25]/3 + (x[f][11] + x[f][13])/6
        #22(L instep) = 13, 15 10:1 외분
        y[f][45] = (x[f][30]*10 - x[f][26])/9
        y[f][46] = (x[f][31]*10 - x[f][27])/9
        #23(R instep) = 14, 16 10:1 외분
        y[f][47] = (x[f][32]*10 - x[f][28])/9
        y[f][48] = (x[f][33]*10 - x[f][29])/9


__ranked 16/156(public), 16/156(Private)__

used Alphapose : https://github.com/MVIG-SJTU/AlphaPose

the best value was with COCO17_duc.py

run by main_coco_dcn.py, baseline_submission_coco_dcn.csv would be result.



# Dependencies

Basically by Alphapose, some libraries added for results

libxcb                    1.14                 h7b6447c_0</br>
libxml2                   2.9.10               hb55368b_3</br>
lz4-c                     1.9.3                h2531618_0</br>
matplotlib                3.3.4                    pypi_0    pypi</br>
matplotlib-base           3.3.4            py37h62a2d02_0</br>
mkl                       2020.2                      256</br>
mkl-service               2.3.0            py37he8ac12f_0</br>
mkl_fft                   1.2.0            py37h23d657b_0</br>
mkl_random                1.1.1            py37h0573a6f_0</br>
munkres                   1.1.4                    pypi_0    pypi</br>
natsort                   7.1.1              pyhd3eb1b0_0</br>
ncurses                   6.2                  he6710b0_1</br>
ninja                     1.10.2           py37hff7bd54_0</br>
numpy                     1.19.2           py37h54aff64_0</br>
numpy-base                1.19.2           py37hfa32c7d_0</br>
olefile                   0.46                     py37_0</br>
opencv-python             4.5.1.48                 pypi_0    pypi</br>
openssl                   1.1.1j               h27cfd23_0</br>
pandas                    1.2.3            py37ha9443f7_0</br>
pcre                      8.44                 he6710b0_0</br>
pgpdump                   1.5                      pypi_0    pypi</br>
pillow                    8.1.0            py37he98fc37_0</br>
pip                       20.3.3           py37h06a4308_0</br>
protobuf                  4.0.0rc2                 pypi_0    pypi</br>
pycocotools               2.0.0                    pypi_0    pypi</br>
pycparser                 2.20                     pypi_0    pypi</br>
pyparsing                 3.0.0b2                  pypi_0    pypi</br>
pyqt                      5.9.2            py37h05f1152_2</br>
python                    3.7.9                h7579374_0</br>
python-dateutil           2.8.1              pyhd3eb1b0_0</br>
pytorch                   1.7.1           py3.7_cuda11.0.221_cudnn8.0.5_0    pytorch</br>
pytz                      2021.1             pyhd3eb1b0_0</br>
pyyaml                    5.4.1                    pypi_0    pypi</br>
pyzmq                     22.0.2                   pypi_0    pypi</br>
qt                        5.9.7                h5867ecd_1</br>
readline                  8.1                  h27cfd23_0</br>
requests                  2.25.1                   pypi_0    pypi</br>
scipy                     1.1.0                    pypi_0    pypi</br>
setuptools                52.0.0           py37h06a4308_0</br>
sip                       4.19.8           py37hf484d3e_0</br>
six                       1.15.0           py37h06a4308_0</br>
sqlite                    3.33.0               h62c20be_0</br>
tensorboardx              2.1                      pypi_0    pypi</br>
timm                      0.1.20                   pypi_0    pypi</br>
tk                        8.6.10               hbc83047_0</br>
torchaudio                0.7.2                      py37    pytorch</br>
torchvision               0.8.2                py37_cu110    pytorch</br>
tornado                   6.1                      pypi_0    pypi</br>
tqdm                      4.56.0             pyhd3eb1b0_0</br>
typing_extensions         3.7.4.3            pyh06a4308_0</br>
urllib3                   1.26.3                   pypi_0    pypi</br>
visdom                    0.1.8.9                  pypi_0    pypi</br>
websocket-client          0.57.0                   pypi_0    pypi</br>
wheel                     0.36.2             pyhd3eb1b0_0</br>
xz                        5.2.5                h7b6447c_0</br>
zlib                      1.2.11               h7b6447c_3</br>
zstd                      1.4.5                h9ceee32_0</br>

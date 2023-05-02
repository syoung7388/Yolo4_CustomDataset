# Training yolov4 with a custom dataset

## Downloads
```
git clone https://github.com/syoung7388/Yolo4_CustomDataset
```

## Requirements
```
conda create -n yolov4 python==3.6.9
```
```
conda activate yolov4
```

```
pip install -r requirements.txt
```

## Usage

**0. Data Preparation**
- save your custom dataset to "./data/custom_datas"
```
cd data
```
- make "data.txt"
```
python3 make_txt.py --dataset_path "absolute path" 
ex) python3 make_txt.py --dataset_path "/NasData/home/ksy/2023-1/PyTorch_YOLOv4/data/custom_datas"
```

**1. Edit config file (./cfg/yolov4-custom.cfg)**
```
cd cfg
```
- line 20: max_batches=(class_numx2000)
- line 22: steps=(class_numx2000x0.8), (class_numx2000x0.9)
- line 1022, 1131, 1240: filters=(class_num+5)*3
- line 1029, 1138, 1247: classes=class_num 

**2. Edit yaml file (./data/custom_data.yaml)**
```
# train and val datasets (image directory or *.txt file with image paths)
train: ./data/custom_datas/custom_train_data.txt  
val: ./data/custom_datas/custom_valid_data.txt  
test: ./data/custom_datas/custom_test_data.txt

# number of classes
nc: 3

# class names
names: ['car', 'autocycle', 'people']

```

**3. Download weights**
```
cd weights
```
```
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137
```

**4. Training**

```
python train.py --device 0 --batch-size 32 --img 640 640 --data ./data/custom_data.yaml --cfg cfg/yolov4-custom.cfg --hyp 'data/cusyom_data.yaml' --weights 'yolov4.conv.137' --name yolov4-custom
```

**5. Testing**

```
python test.py --img 640 --conf 0.001 --batch 8 --device 0 --data ./data/custom_data.yaml --cfg cfg/yolov4-custom.cfg --weights trained_weight_path
```

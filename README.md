# Training yolov4 with a custom dataset

## Downloads
```
git clone git@github.com:syoung7388/Yolo4_CustomDataset.git
```

## Requirements
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

 


1. Contrastive model 
```
python3 contrastive.py --classification_layer 1 
```

2. Ensemble model 
```
python3 ensemble.py --ensemble 1  
```

3. Single model 
```
python3 ensemble.py --ensemble 0 
```


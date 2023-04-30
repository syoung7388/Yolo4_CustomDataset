from glob import glob
import argparse

parser = argparse.ArgumentParser(description="make_txt")
parser.add_argument("--dataset_path", type=str, default="/NasData/home/ksy/2023-1/PyTorch_YOLOv4/data/custom_datas")
args = parser.parse_args() 

def make_txt(path, mode):

    all_paths = glob(path+'/*')
    with open(f'{args.dataset_path}/custom_{mode}_data.txt', 'w') as f:
        for path in all_paths:
            f.write(path+ '\n')

make_txt(f'{args.dataset_path}/images/train', 'train')
make_txt(f'{args.dataset_path}/images/valid', 'valid')
make_txt(f'{args.dataset_path}/images/test', 'test')
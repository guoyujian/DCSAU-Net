import argparse
import os
import logging

sub_dir_list = ['ISIC2018_Task1-2_Training_Input',
        'ISIC2018_Task1_Training_GroundTruth',
    ]

'''
检查是否有应该有的四个文件夹
'''
def check(pth: str):
    for sub_dir in sub_dir_list:
        full_path = os.path.join(pth, sub_dir)
        if not os.path.exists(full_path):
            logging.warning(f'{full_path} is noe exists, pls check.')
            return False
    return True


def process(pth: str):
    # 删除一些不需要的文件
    for sub_dir in sub_dir_list:
        to_be_delete = os.path.join(pth, sub_dir, 'ATTRIBUTION.txt')
        if os.path.exists(to_be_delete):
            os.remove(to_be_delete)
        to_be_delete = os.path.join(pth ,sub_dir, 'LICENSE.txt')
        if os.path.exists(to_be_delete):
            os.remove(to_be_delete)
    # 将groundtruth下的文件全部改名：'_segmentation.png' -> '.png', 'jpg' -> '.png'
    for sub_dir in sub_dir_list:
        full_path = os.path.join(pth, sub_dir)
        files = os.listdir(full_path)
        for file in files:
            if ('.jpg' not in file) and ('.png' not in file):
                os.remove(os.path.join(full_path, file))
                pass
            else:
                new_file_name = file.replace('_segmentation.png', '.png').replace('.jpg', '.png')
                os.rename(os.path.join(full_path, file), os.path.join(full_path, new_file_name))
                pass
            pass
        if 'GroundTruth' in sub_dir:
            os.rename(os.path.join(pth, sub_dir), os.path.join(pth, 'masks'))
            pass
        else :
            os.rename(os.path.join(pth, sub_dir), os.path.join(pth, 'images'))

    pass
def main():
    parser = argparse.ArgumentParser(description=
        '''下载ISIC2018_Task1-2_Training_Input、
        ISIC2018_Task1_Training_GroundTruth2个数据集，
        放到一个文件夹内，将这个文件夹作为参数传入''')
    parser.add_argument('-p', 
        '--pth', 
        type= str,
        required= True,
        help= "input a data path"
    )
    args = parser.parse_args()
    if not check(args.pth):
        return 

    process(args.pth)


    pass


if __name__ == '__main__':
    main()
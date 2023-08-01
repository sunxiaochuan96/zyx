# encoding: utf-8
import os
import numpy as np
import cv2
import mmcv
import argparse

parser = argparse.ArgumentParser(description='visualization')
parser.add_argument('--video_num', type=int, help='选择某个视频编号')
parser.add_argument('--imgpath', default='', help='测试集路径')
parser.add_argument('--respath', default='', help='需要可视化的结果路径')
parser.add_argument('--dstpath', default='', help='保存路径')
args = parser.parse_args()

# 选择第几个视频
video_num = args.video_num

# 数据集所在路径
src_pic_path = args.imgpath

all_pic = os.listdir(src_pic_path)  # os.listdir获取到的路径是乱序的，要用.sort函数排序
all_pic.sort()

each_video_path = [os.path.join(src_pic_path, video_path) for video_path in all_pic]

# 选择一个视频（OTB100中的一个文件夹）
one_video = each_video_path[video_num] # 
result = one_video.split('/')
video_name = result[len(result)-1]
print('choosed video_name: ({})--'.format(video_num), video_name)

# 算法评测结果所在路径
eval_result_path = args.respath
all_eval_trackers = os.listdir(eval_result_path)
all_eval_trackers.sort()
each_eval_tracker = [os.path.join(eval_result_path, eval_tracker) for eval_tracker in all_eval_trackers]
each_eval_tracker.sort()

#
one_tracker = each_eval_tracker[0]  #
each_eval_result = os.listdir(one_tracker)
each_eval_result.sort()  # ['Basketball.txt', 'Biker.txt', 'Bird1.txt', ... ,'Walking2.txt', 'Woman.txt']


all_trakcers_result = []
for tracker in each_eval_tracker:
    each_eval_result_path = [os.path.join(tracker, eval_result) for eval_result in each_eval_result]
    all_trakcers_result.append(each_eval_result_path)

all_list = []  # a video of one tracker
for num in range(0, len(all_trakcers_result)):
    with open(all_trakcers_result[num][video_num]) as eval_result:  # choose a video of one tracker
        dataset = []
        lines = eval_result.readlines()

        # read datas in txt file, transform to String formation
        for line in lines:
            temp1 = line.strip('\n')
            temp2 = temp1.split('\t')
            dataset.append(temp2)

        new_dataset = [new_line[0].split(',') for new_line in dataset]  # .split(',')按逗号分割字符串
        # print('new_dataset', new_dataset)
        # str转化成int型
        for i in range(0, len(new_dataset)):
            for j in range(len(new_dataset[i])):
                new_dataset[i][j] = int(float(new_dataset[i][j]))
        all_list.append(new_dataset)


# every frame in a video
frames_list = os.listdir(os.path.join(one_video, 'img'))
frames_list.sort()
frames_path = [os.path.join(os.path.join(one_video, 'img'), frame_path) for frame_path in frames_list]


dst_pic_path = args.dstpath
video_name = video_name.split('\\')[-1]
dst_pic_path = dst_pic_path + video_name

if os.path.exists(dst_pic_path):
    for file in os.listdir(dst_pic_path):
        os.remove(os.path.join(dst_pic_path, file))

color_list = [(255, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255),
                  (0, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0), (100, 100, 100)]
                # 白色 DasiamRPN 黄色 siamBAN 紫色 siamCAR 青色siamDWfc
                # 红色 siamDWrpn 蓝色 siamFC  绿色 siamRPN 黑色 siamRPN++  灰色 siammask
for index, path in enumerate(frames_path):
    img = cv2.imread(path)
    for idx in range(len(all_list)):
        track_gt = all_list[idx][index]
        cv2.rectangle(img, (track_gt[0], track_gt[1]), (track_gt[0] + track_gt[2], track_gt[1] + track_gt[3]),
                      color_list[idx], thickness=2)
        label = all_list[idx]

    cv2.putText(img, '#{}'.format(index), (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)
    cv2.putText(img, video_name, (10, int(img.shape[0] * 0.9)), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 255), 2)

    cv2.imwrite(dst_pic_path + '/' + video_name + '_img_{}.jpg'.format(index), img)
output = dst_pic_path + '/' + '{}.mp4'.format(video_name)
print(output)
mmcv.frames2video(dst_pic_path, output, start=0, fps=30, fourcc='mp4v', filename_tmpl=video_name + '_img_{}.jpg')
print('已成功导出视频 至 {}'.format(dst_pic_path))

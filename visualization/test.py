import os
import cv2

# # -----------------------
# # 文件重命名
# # -----------------------
# src_path = "E:\\0_OTB_benchmark\\Test\\Basketball\\img"
# dst_path = "E:\\0_OTB_benchmark\\Test\\dst"
# all_filename = os.listdir(src_path)
#
# print(all_filename)
#
# all_filename_path_old = [os.path.join(src_path, filename) for filename in all_filename if '.jpg' in filename]  # 把路径和图片名字组在一起
# print(all_filename_path_old)
# all_filename_new = []
# for i in range(len(all_filename_path_old)):
#     all_filename_new.append('{}.jpg'.format(i))
# print(all_filename_new)
# all_filename_path_new = [os.path.join(dst_path, filename) for filename in all_filename_new]
# print(all_filename_path_new)
# for (old_file, new_file) in zip(all_filename_path_old, all_filename_path_new):
#     os.renames(old_file, new_file)  # 好像把原来的文件夹覆盖掉了，先拷贝一份，以防万一

img = cv2.imread('D:\\work\\GitLoadWareHouse\\pysot\\testing_dataset\\OTB100\\Basketball\\img\\0001.jpg')
cv2.imshow("img",img)
cv2.waitKey(0)

bbox = [100, 100, 200, 200]  # [x1, y1, w, h]

# 在图像上绘制跟踪框和文字
color = (0, 255, 0)  # 框的颜色，这里用绿色
thickness = 2  # 框的线宽
font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
text = 'Target'  # 标注的文本内容
text_color = (0, 0, 255)  # 文本颜色，这里用红色

# 画框
cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[0]+bbox[2], bbox[1]+bbox[3]), color, thickness)

# 写文本
text_size = cv2.getTextSize(text, font, 1, thickness)[0]
text_origin = (img.shape[1]-text_size[0]-10, 10+text_size[1])
cv2.putText(img, text, text_origin, font, 1, text_color, thickness)

# 显示图像
cv2.imshow('image', img)
cv2.waitKey(0)
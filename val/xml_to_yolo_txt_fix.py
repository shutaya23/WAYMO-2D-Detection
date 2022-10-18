# xml_to_yolo_txt.py
# 此代碼和VOC_KITTI文件夾同目錄
import os
import glob
import xml.etree.ElementTree as ET
# 這裏的類名爲我們xml裏面的類名，順序現在不需要考慮
class_names = ['Car', 'Cyclist', 'Pedestrian']
# xml文件路徑
path = 'yololabel/'
# 轉換一個xml文件爲txt
def single_xml_to_txt(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # 保存的txt文件路徑
    txt_file = xml_file.split('.')[0]+'.txt'
    with open(txt_file, 'w') as txt_file:
        for member in root.findall('object'):
            #filename = root.find('filename').text
            picture_width = int(root.find('size')[0].text)
            picture_height = int(root.find('size')[1].text)
            class_name = member[0].text
            # 類名對應的index
            class_num = class_names.index(class_name)

            box_x_min = int(member[1][0].text) # 左上角橫座標
            box_y_min = int(member[1][1].text) # 左上角縱座標
            box_x_max = int(member[1][2].text) # 右下角橫座標
            box_y_max = int(member[1][3].text) # 右下角縱座標
            # 轉成相對位置和寬高
            x_center = (box_x_min+0.5*(box_x_max - box_x_min )) / (1.0 * picture_width)
            y_center = (box_y_min+0.5*(box_y_max - box_y_min )) / (1.0 * picture_height)
            width = (box_x_max - box_x_min) / (1.0 * picture_width)
            height = (box_y_max - box_y_min) / (1.0 * picture_height)
            print(class_num, x_center, y_center, width, height)
            txt_file.write(str(class_num) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(height) + '\n')
# 轉換文件夾下的所有xml文件爲txt
def dir_xml_to_txt(path):
    for xml_file in glob.glob(path + '*.xml'):
        single_xml_to_txt(xml_file)
        print("OK")
dir_xml_to_txt(path)


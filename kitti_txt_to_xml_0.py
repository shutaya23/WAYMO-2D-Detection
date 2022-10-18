# kitti_txt_to_xml.py
# encoding:utf-8
# 根據一個給定的XML Schema，使用DOM樹的形式從空白文件生成一個XML
from xml.dom.minidom import Document
import cv2
import os
filepath = 'image_0/'
def generate_xml(name,split_lines,img_size,class_ind):
    doc = Document() # 創建DOM文檔對象
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)
    title = doc.createElement('folder')
    title_text = doc.createTextNode('KITTI')
    title.appendChild(title_text)
    annotation.appendChild(title)
    img_name=name+'.png'
    title = doc.createElement('filename')
    title_text = doc.createTextNode(img_name)
    title.appendChild(title_text)
    annotation.appendChild(title)
    source = doc.createElement('source')
    annotation.appendChild(source)
    title = doc.createElement('database')
    title_text = doc.createTextNode('The KITTI Database')
    title.appendChild(title_text)
    source.appendChild(title)
    title = doc.createElement('annotation')
    title_text = doc.createTextNode('KITTI')
    title.appendChild(title_text)
    source.appendChild(title)
    size = doc.createElement('size')
    annotation.appendChild(size)
    title = doc.createElement('width')
    title_text = doc.createTextNode(str(img_size[1]))
    title.appendChild(title_text)
    size.appendChild(title)
    title = doc.createElement('height')
    title_text = doc.createTextNode(str(img_size[0]))
    title.appendChild(title_text)
    size.appendChild(title)
    title = doc.createElement('depth')
    title_text = doc.createTextNode(str(img_size[2]))
    title.appendChild(title_text)
    size.appendChild(title)
    for split_line in split_lines:
        line=split_line.strip().split()
        if line[0] in class_ind:
            object = doc.createElement('object')
            annotation.appendChild(object)
            title = doc.createElement('name')
            title_text = doc.createTextNode(line[0])
            title.appendChild(title_text)
            object.appendChild(title)
            bndbox = doc.createElement('bndbox')
            object.appendChild(bndbox)
            title = doc.createElement('xmin')
            title_text = doc.createTextNode(str(int(float(line[4]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymin')
            title_text = doc.createTextNode(str(int(float(line[5]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('xmax')
            title_text = doc.createTextNode(str(int(float(line[6]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymax')
            title_text = doc.createTextNode(str(int(float(line[7]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
    # 將DOM對象doc寫入文件
    f = open('Annotations/0/'+name+'.xml','w')
    f.write(doc.toprettyxml(indent = ''))
    f.close()
if __name__ == '__main__':
    class_ind=('Pedestrian', 'Car', 'Cyclist')
    cur_dir=os.getcwd()
    labels_dir=os.path.join(cur_dir,'label_0/')
    for parent, dirnames, filenames in os.walk(labels_dir): # 分別得到根目錄，子目錄和根目錄下文件   
        for file_name in filenames:
            full_path=os.path.join(parent, file_name) # 獲取文件全路徑
            f=open(full_path)
            split_lines = f.readlines()
            name= file_name[:-4] # 後四位是擴展名.txt，只取前面的文件名
            img_name=name+'.png' 
            img_path=os.path.join(filepath,img_name) # 路徑需要自行修改            
            img_size=cv2.imread(img_path).shape
            generate_xml(name,split_lines,img_size,class_ind)
print('all txts has converted into xmls')

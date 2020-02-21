#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# @Author: Xu Wang
# @Date: Monday, February 17th 2020
# @Email: wangxu.93@hotmail.com
# @Copyright (c) 2020 Institute of Trustworthy Network and System, Tsinghua University
'''
# convert test-dev to voc
from pathlib import Path
import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def write_xml(dst_file, json_content):
    anno = ET.Element('annotation')
    for obj in json_content:
        obj_ele = ET.SubElement(anno, 'object')
        track_id = ET.SubElement(obj_ele, 'trackid')
        track_id.text = str(obj['target_id'])
        name = ET.SubElement(obj_ele, 'name')
        name.text = str(obj['category'])
        bndbox = ET.SubElement(obj_ele, 'bndbox')
        xmin = ET.SubElement(bndbox, 'xmin')
        xmax = ET.SubElement(bndbox, 'xmax')
        ymin = ET.SubElement(bndbox, 'ymin')
        ymax = ET.SubElement(bndbox, 'ymax')
        xmin.text = str(obj['xmin'])
        ymin.text = str(obj['ymin'])
        xmax.text = str(obj['xmax'])
        ymax.text = str(obj['ymax'])

    mydata = ET.tostring(anno, 'utf-8')
    reparsed = minidom.parseString(mydata)
    mydata = reparsed.toprettyxml(indent="\t")
    myfile = open(dst_file, "w")
    myfile.write(mydata)

drone_root = Path("/Users/wangxu/Downloads/VisDrone2019-MOT-test-dev/")
data_root = Path('/Users/wangxu/Git/EdgeTile-Client/data')
for anno_file in drone_root.glob("**/*.txt"):
    frame_objects = {}
    with open(anno_file) as f:
        for l in f.readlines():
            item = [int(u) for u in l[:-1].split(',')]
            frame_id = item[0]
            target_id = item[1]
            left = item[2]
            top = item[3]
            width = item[4]
            height = item[5]
            category = item[7]
            if frame_id not in frame_objects:
                frame_objects[frame_id] = []

            frame_objects[frame_id].append({'target_id': target_id, 'xmin': left, 'ymin': top, 'xmax': left + width, 'ymax': top + height, 'category': category})
    seq_dir = data_root / 'drone' / 'anno' / anno_file.stem
    if not os.path.exists(seq_dir):
        os.mkdir(seq_dir)
    for frame_id, objs in frame_objects.items():
        dst_file = seq_dir / '{:06d}.xml'.format(frame_id)
        write_xml(dst_file, objs)
    




            




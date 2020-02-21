#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
# @Author: Xu Wang
# @Date: Tuesday, February 18th 2020
# @Email: wangxu.93@hotmail.com
# @Copyright (c) 2020 Institute of Trustworthy Network and System, Tsinghua University
'''
from pathlib import Path
import os

drone_root = Path("/Users/wangxu/Downloads/VisDrone2019-MOT-test-dev/")
video_root = Path('/Users/wangxu/Git/EdgeTile-Client/data/drone/video')

seq_dir = drone_root / "sequences"
seqs = [x for x in seq_dir.iterdir() if x.is_dir()]
for seq in seqs:
    cmd = "ffmpeg -r 30 -i " + str(seq) + "/%07d.jpg -c:v libx264 " + str(video_root / (seq.name + ".mp4"))
    os.system(cmd)
    print(seq)
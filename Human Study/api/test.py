from flask import jsonify
import json
import os
import random

IMG_PORT = 3030

#TODO change this to fid00.umiacs.umd.edu after port is exposed
base_url = 'localhost'

def merge_group_lists(gl1, gl2):
    try:
        l1_max_id = gl1[-1]['id']
        for img in gl2:
            img['id'] += l1_max_id + 1
        gl1.extend(gl2)
        return gl1
    except:
        return []


def fid_group_list(group_num, num_imgs):
    curr_dir = os.getcwd()
    ret = []
    base_img_dir = os.path.join(curr_dir, "image_server/public/images/")
    img_dirs = os.listdir(base_img_dir)
    if group_num > len(img_dirs) or group_num < 1:
        return ret
    else:
        img_dir = os.path.join(base_img_dir, img_dirs[group_num - 1])
    img_list = os.listdir(img_dir)[1:]
    try:
        sample_list = random.sample(img_list, k=num_imgs)
    except:
        return ret
    
    fid_score = float(json.load(open(os.path.join(img_dir,'desc.json')))["fid"])
    for x in range(len(sample_list)):
        url = base_url+":"+str(IMG_PORT)+"/images/"+img_dirs[group_num - 1]+"/"+sample_list[x]
        ret.append({"id": x, "fid":fid_score, "url":url})
    return ret

a = fid_group_list(1, 300)
b = fid_group_list(2, 3)
print(merge_group_lists(a,b))
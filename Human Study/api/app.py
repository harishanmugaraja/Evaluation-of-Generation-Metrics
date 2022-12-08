from flask import Flask, request, send_file
from flask_cors import *
from flask import jsonify
import json
import os
import random

IMG_PORT = 3030

#TODO change this to fid00.umiacs.umd.edu:3030 after port is exposed
base_url = 'http://127.0.0.1'

app = Flask(__name__)
@app.route('/')
def myapp():
    message = "Flask server is running!"
    return message

@app.route('/rankGroups')
@cross_origin()
def rankGroups():
    img_dirs = get_groups()
    try:
        index_list = random.sample(range(len(img_dirs)),k=4)
    except:
        return ({"status":400})
    imagearrs = []
    for x in range(len(index_list)):
        dict_val = grouped_by_fid_list(index_list[x]+1, 4)
        dict_val["id"] = x
        imagearrs.append(dict_val)
    return ({"status": 200, "imagearrs": imagearrs})

@app.route('/gridWhole')
@cross_origin()

def gridWhole():
    img_dirs = get_groups()
    try:
        # sample_list = random.sample(img_dirs, k=2)
        index_list = random.sample(range(len(img_dirs)),k=2)
    except:
        return ({"status":400})
    imagearrs = []
    for x in range(len(index_list)):
        imagearrs.append(fid_group_list(index_list[x]+1, 9))

    return ({"status": 200, "imagearrs": imagearrs})

@app.route('/gridSingle')
@cross_origin()
def gridSingle():
    img_dirs = get_groups()
    try:
        # sample_list = random.sample(img_dirs, k=2)
        index_list = random.sample(range(len(img_dirs)),k=2)
    except:
        return ({"status":400})
    ret = merge_group_lists(fid_group_list(index_list[0]+1, 8), fid_group_list(index_list[1]+1, 1))
    if len(ret) != 0:
        return ({"status": 200, "groups": ret})
    else:
        return ({"status": 400, "groups":[]})

@app.route('/binGroups')
@cross_origin()
def binGroups():
    img_dirs = get_groups()
    try:
        index_list = random.sample(range(len(img_dirs)),k=2)
    except:
        return ({"status":400})
    imagearrs = []
    for x in range(len(index_list)):
        dict_val = grouped_by_fid_list(index_list[x]+1, 4)
        dict_val["id"] = x
        imagearrs.append(dict_val)
    return ({"status": 200, "imagearrs": imagearrs})

def get_groups():
    curr_dir = os.getcwd()
    base_img_dir = os.path.join(curr_dir, "image_server/public/images/")
    img_dirs = os.listdir(base_img_dir)
    return img_dirs

def merge_group_lists(gl1, gl2):
    try:
        l1_max_id = gl1[-1]['id']
        for img in gl2:
            img['id'] += l1_max_id + 1
        gl1.extend(gl2)
        random.shuffle(gl1)
        return gl1
    except:
        return []



# of the format:
# [
#     {
#         "id": 5,
#         "fid": 2,
#         "url": "../assets/images/group1/p2.png"
#         //selected: false
#     },
#     {
#         "id": 4,
#         "fid": 2,
#         "url": "../assets/images/group1/p1.png"
#     },
#     {
#         "id": 6,
#         "fid": 2,
#         "url": "../assets/images/group1/p3.png"
#     },
# ]
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
    
    fid_score = float(json.load(open(os.path.join(img_dir,'desc.json')))["frechet_inception_distance"])
    for x in range(len(sample_list)):
        url = base_url+":"+str(IMG_PORT)+"/images/"+img_dirs[group_num - 1]+"/"+sample_list[x]
        ret.append({"id": x, "fid":fid_score, "url":url})
    return ret
    
# of the format:
#  [
#     {id: 0, fid: 1, imagelist: ['../assets/images/group1/p1.png','../assets/images/group1/p2.png','../assets/images/group1/p3.png','../assets/images/group1/p4.png']},
#     {id: 1, fid: 2, imagelist: ['../assets/images/group2/p1.png','../assets/images/group2/p2.png','../assets/images/group2/p3.png','../assets/images/group2/p4.png']},
#     {id: 2, fid: 3, imagelist: ['../assets/images/group3/p1.png','../assets/images/group3/p2.png','../assets/images/group3/p3.png','../assets/images/group3/p4.png']}
# ]

# this method returns just one element of that array so 

#     {fid: 2, imagelist: ['../assets/images/group2/p1.png','../assets/images/group2/p2.png','../assets/images/group2/p3.png','../assets/images/group2/p4.png']},
# for example, id field will be added by function calling this one

def grouped_by_fid_list(group_num, num_imgs):
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

    fid_score = float(json.load(open(os.path.join(img_dir,'desc.json')))["frechet_inception_distance"])
    for x in range(len(sample_list)):
        url = base_url+":"+str(IMG_PORT)+"/images/"+img_dirs[group_num - 1]+"/"+sample_list[x]
        ret.append(url)
    return {"fid": fid_score, "imagelist": ret}
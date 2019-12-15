""" generation of images interactively with ui control """

import os
from pathlib import Path
import glob
import sys
import PIL
from PIL import Image
import json
import numpy as np
import pickle
import tensorflow as tf

import src.tl_gan.feature_axis as feature_axis


""" location to save images """
path_gan_explore_interactive = './asset_results/pggan_celeba_feature_axis_explore_interactive/'
if not os.path.exists(path_gan_explore_interactive):
    os.mkdir(path_gan_explore_interactive)

##
""" load feature directions """
path_feature_direction = './asset_results/pg_gan_celeba_feature_direction_40'

pathfile_feature_direction = glob.glob(os.path.join(path_feature_direction, 'feature_direction_*.pkl'))[-1]

with open(pathfile_feature_direction, 'rb') as f:
    feature_direction_name = pickle.load(f)

feature_direction = feature_direction_name['direction']
feature_name = feature_direction_name['name']
num_feature = feature_direction.shape[1]

""" load gan model """

# path to model code and weight
path_pg_gan_code = './src/model/pggan'
path_model = './asset_model/karras2018iclr-celebahq-1024x1024.pkl'
sys.path.append(path_pg_gan_code)

""" create tf session """
yn_CPU_only = False

if yn_CPU_only:
    config = tf.ConfigProto(device_count = {'GPU': 0}, allow_soft_placement=True)
else:
    config = tf.ConfigProto(allow_soft_placement=True)

sess = tf.InteractiveSession(config=config)
print('1')
try:
    with open(path_model, 'rb') as file:
        G, D, Gs = pickle.load(file)
except FileNotFoundError:
    print('before running the code, download pre-trained model to project_root/asset_model/')
    raise

num_latent = Gs.input_shapes[0][1]

""" load base model into latents variable"""
filename='hispanic_man1.npy'
path=Path("baseline_models/" + str(filename))
f=open(path, encoding="utf-8")
latent = np.load(path, encoding="latin1")
f.close()

# Generate dummy labels
dummies = np.zeros([latent.shape[0]] + Gs.input_shapes[1][1:])

def gen_image(latents):
    """
    tool funciton to generate image from latent variables
    :param latents: latent variables
    :return:
    """
    images = Gs.run(latents, dummies)
    images = np.clip(np.rint((images + 1.0) / 2.0 * 255.0), 0.0, 255.0).astype(np.uint8)  # [-1,1] => [0,255]
    images = images.transpose(0, 2, 3, 1)  # NCHW => NHWC
    return images[0]

img_cur = gen_image(latent)
# image=Image.fromarray(img_cur)
# image.show()

idx = 16 #mustache

latent_copy=latent.copy()
feature_lock_status = np.zeros(num_feature).astype('bool')
feature_direction_disentangled = feature_axis.disentangle_feature_axis_by_idx(feature_direction, idx_base=np.flatnonzero(feature_lock_status))
latent_copy += feature_direction_disentangled[:, idx]

img_cur1 = gen_image(latent_copy)
img_cur1 = np.hstack((img_cur,img_cur1))
image1=Image.fromarray(img_cur1)
image1.show()



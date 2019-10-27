""" generation of images interactively with ui control """

import os
from pathlib import Path
import glob
import sys
from PIL import Image
import numpy as np
import time
import pickle
import tensorflow as tf
import PIL


import src.tl_gan.feature_axis as feature_axis

##
""" load feature directions """
path_feature_direction = './asset_results/pg_gan_celeba_feature_direction_40'

pathfile_feature_direction = glob.glob(os.path.join(path_feature_direction, 'feature_direction_*.pkl'))[-1]

with open(pathfile_feature_direction, 'rb') as f:
    feature_direction_name = pickle.load(f)

feature_direction = feature_direction_name['direction']
feature_name = feature_direction_name['name']
num_feature = feature_direction.shape[1]

##
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

try:
    with open(path_model, 'rb') as file:
        G, D, Gs = pickle.load(file)
except FileNotFoundError:
    print('before running the code, download pre-trained model to project_root/asset_model/')
    raise

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

directories = [f'asian_man{i}.npy' for i in range (1,4)] + [f'asian_woman{i}.npy' for i in range (1,4)] + [f'indian_man{i}.npy' for i in range (1,4)] + [f'indian_woman{i}.npy' for i in range (1,4)] + [f'caucasian_man{i}.npy' for i in range (1,4)] + [f'caucasian_woman{i}.npy' for i in range (1,4)] + [f'hispanic_man{i}.npy' for i in range (1,4)] + [f'hispanic_woman{i}.npy' for i in range (1,4)] + [f'black_man{i}.npy' for i in range (1,4)] + [f'black_woman{i}.npy' for i in range (1,4)]

for img in directories:
    # Load latents
    path=Path("baseline_models/" + str(img))
    f=open(path, encoding="utf-8")
    latents = np.load(path, encoding="latin1")
    f.close()

    # Generate dummy labels and generating image
    dummies = np.zeros([latents.shape[0]] + Gs.input_shapes[1][1:])
    img_cur = gen_image(latents)

    for i in range(10):
        print(i)
        if i==0: 
            img_cur3 = np.copy(img_cur)
            i+=1
            continue
        # Warp features starting with feature 2 (not implementing "5'o clock shadow")
        latents_copy=latents.copy()
        feature_lock_status = np.zeros(num_feature).astype('bool')
        feature_direction_disentangled = feature_axis.disentangle_feature_axis_by_idx(feature_direction, idx_base=np.flatnonzero(feature_lock_status))
        latents_copy += feature_direction_disentangled[:, i]
        i+=1

        img_cur2 = gen_image(latents_copy)
        img_cur3=np.hstack([img_cur3, img_cur2])
    image=Image.fromarray(img_cur3)
    image.show()






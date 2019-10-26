""" generation of images interactively with ui control """

import os
from pathlib import Path
import glob
import sys
import PIL
from PIL import Image
import numpy as np
import pickle
import tensorflow as tf

import src.tl_gan.feature_axis as feature_axis

""" location to save images """
path_gan_explore_interactive = './asset_results/pggan_celeba_feature_axis_explore_interactive/'
if not os.path.exists(path_gan_explore_interactive):
    os.mkdir(path_gan_explore_interactive)


""" load feature directions """
path_feature_direction = './asset_results/pg_gan_celeba_feature_direction_40'

pathfile_feature_direction = glob.glob(os.path.join(path_feature_direction, 'feature_direction_*.pkl'))[-1]

with open(pathfile_feature_direction, 'rb') as f:
    feature_direction_name = pickle.load(f)

feature_direction = feature_direction_name['direction']
feature_name = feature_direction_name['name']
num_feature = feature_direction.shape[1]
edit_feature_dict = {feature_name[i]:i for i in range(len(feature_name))}
change_feature_dict = {feature_name[i]:0 for i in range(len(feature_name))}


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

num_latent = Gs.input_shapes[0][1]


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

while True:
    """
    Generate random images
    Input "break" to end generation
    Input "no" to forget the image
    Otherwise input the name of the file to be saved.
    """
    # Generate random latents
    latents = np.random.randn(1, *Gs.input_shapes[0][1:])
    # Generate dummy labels
    dummies = np.zeros([latents.shape[0]] + Gs.input_shapes[1][1:])
    img_cur = gen_image(latents)
    image1=Image.fromarray(img_cur)
    image1.show()

    i=input()
    path=Path("baseline_models/" + str(i))

    if i=='break':
        break
    if i != 'no':
        if not os.path.isfile(path):
            open(path, 'w+').close()
        np.save(path, latents)
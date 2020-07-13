import numpy as np
from PIL import Image
import glob
import torch
from torch.utils.data.dataset import Dataset
import torchvision.transforms as transforms

class FairFaceDataset(Dataset):
    def __init__(self, folder_path, dimensions):
        """
        Args:
            folder_path (string): path to image folder
            dimensions  (tuple): a tuple of (width, height)
        """
        # Get image list
        self.image_list = glob.glob(folder_path+'*')
        # Calculate len
        self.data_len = len(self.image_list)
        #transforms
        self.convert_image = transforms.Compose([
            transforms.Resize(dimensions),
            transforms.ToTensor(), 
            #comment the normalize line if you don't need it
            transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))
        ])


    def __getitem__(self, index):
        # Get image name from the pandas df
        single_image_path = self.image_list[index]
        # Open image
        im_as_im = Image.open(single_image_path)
        # Do some operations on image
        # Convert to numpy, dim = 89x89
        im_as_ten = self.convert_image(im_as_im)
        return im_as_ten

    def __len__(self):
        return self.data_len

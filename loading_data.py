# Imports
import tensorflow as tf
from pathlib import Path

class Loading_data():
    def __init__(self, path_training_data, path_test_data): 
        print(Path.cwd()) # Current Directory
        self.path_training_data = Path(path_training_data) # Path to training data
        self.path_test_data = Path(path_test_data) # Path to test data
        self.training_img = None
        print("-----------------")
        self.training_img = list(self.path_training_data.glob("*/*")) # Listing folder contents
        print(self.training_img[725:736]) # View a sample list
        print("-----------------")
        self.training_img = list(map(lambda x: str(x), self.training_img)) # Lambda expression that extracts only the value with the path of each image
        print(self.training_img[725:736]) # View a sample list
        print("-----------------")
        print(len(self.training_img)) # Total training images
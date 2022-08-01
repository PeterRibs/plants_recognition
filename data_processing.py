# Imports
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from loading_data import Loading_data

class Data_processing(Loading_data):
    def __init__(self, path_training_data, path_test_data):
        super().__init__(path_training_data, path_test_data)
        self.img_training_labels = None
        self.encoder = LabelEncoder() # create the object
        self.X_training = None
        self.X_valid = None
        self.Y_training = None
        self.Y_valid = None

    def extract_label(img_path):
        return img_path.split("\\")[-2] # Function that gets the label of each image

    def extract_label_apply(self): # Apply the function
        self.imgs_training_labels = list(map(lambda x: self.extract_label(x), self.training_img))
        print(self.img_training_labels[740:745]) # View a sample list
        print("-----------------")

    def fit_transformation_apply(self):
        self.imgs_training_labels = self.encoder.fit_transform(self.imgs_training_labels) # Apply the fit_transform
        print(self.img_training_labels[740:745]) # View a sample list
        self.imgs_training_labels = tf.keras.utils.to_categorical(self.imgs_training_labels) # Apply One-Hot-Encoding on the labels
        print(self.img_training_labels[740:745]) # View a sample list
        print("-----------------")

    def split_data(self):
        self.X_training, self.X_valid, self.y_training, self.y_valid = train_test_split(self.training_img, self.imgs_training_labels) # Split the training data into two samples, training and validation
        print("\nX_training")
        print(self.X_training[10:13])
        print("\nY_training")
        print(self.Y_training[10:13])
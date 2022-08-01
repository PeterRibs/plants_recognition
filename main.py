# from loading_data import Loading_data

# path_training_data = "fruits/Training"
# path_test_data = "fruits/Test"

# a = Loading_data(path_training_data, path_test_data)

# a.imgs()


from data_processing import Data_processing

path_training_data = "fruits/Training"
path_test_data = "fruits/Test"

a = Data_processing(path_training_data, path_test_data)

a.extract_label()
a.extract_label_apply()
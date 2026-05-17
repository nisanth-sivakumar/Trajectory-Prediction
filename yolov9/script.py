import zipfile
with zipfile.ZipFile('object-tracking\\yolov9\\deep_sort_pytorch.zip', 'r') as zip_ref:
    zip_ref.extractall()

# import os
# print(os.getcwd())  # current directory
# print(os.listdir())  # all files here
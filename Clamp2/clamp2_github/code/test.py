import os
import numpy as np

# # Path to the folder containing .npy files
# folder_path = 'emb'

# # List all files in the folder
# files = os.listdir(folder_path)

# # Filter out .npy files
# npy_files = [file for file in files if file.endswith('.npy')]

# # Iterate over each .npy file and display its size, dimensions, and type
# for npy_file in npy_files:
#     file_path = os.path.join(folder_path, npy_file)
#     data = np.load(file_path)
#     print(f"File: {npy_file}")
#     print(f"Size: {data.size}")
#     print(f"Dimensions: {data.shape}")
#     print(f"Type: {data.dtype}")
#     print()

# Path to the folder containing .npz files
converted_folder_path = 'converted'

# List all files in the folder
converted_files = os.listdir(converted_folder_path)

# Filter out .npz files
npz_files = [file for file in converted_files if file.endswith('.npz')]

# Iterate over each .npz file and display its size, dimensions, and type
for npz_file in npz_files:
    file_path = os.path.join(converted_folder_path, npz_file)
    data = np.load(file_path)
    print(f"File: {npz_file}")
    for key in data:
        print(f"Array: {key}")
        print(f"Size: {data[key].size}")
        print(f"Dimensions: {data[key].shape}")
        print(f"Type: {data[key].dtype}")
        print()
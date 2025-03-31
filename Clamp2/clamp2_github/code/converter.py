import os
import numpy as np

# Directory containing .npy files
input_dir = 'emb'
# Directory to save .npz files
output_dir = 'converted'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.npy'):
        # Load the .npy file
        data = np.load(os.path.join(input_dir, filename))
        
        # Define the output file path
        output_file = os.path.join(output_dir, filename.replace('.npy', '.npz'))
        
        # Save the data as a .npz file
        np.savez(output_file, data=data)

        print(f"Converted {filename} to {output_file}")
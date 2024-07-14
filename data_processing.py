import cv2
import os
import numpy as np
from descriptor import glcm, bitdesc

# List of descriptors
descriptors = [glcm, bitdesc]

def process_datasets(root_folder, descriptors):
    all_features = {descriptor.__name__: [] for descriptor in descriptors}  # Dictionary to store features for each descriptor

    for descriptor in descriptors:
        for root, dirs, files in os.walk(root_folder):
            for file in files:
                if file.lower().endswith(('.jpg', '.png', '.jpeg')):
                    relative_path = os.path.relpath(os.path.join(root, file), root_folder)
                    file_name = f'{relative_path.split(os.sep)[0]}_{file}'  
                    image_rel_path = os.path.join(root, file)
                    folder_name = os.path.basename(os.path.dirname(image_rel_path))

                    print(f"Processing file: {image_rel_path}")

                    img = cv2.imread(image_rel_path, 0)
                    if img is not None:
                        features = descriptor(img)
                        if features is not None:
                            features = features + [folder_name, relative_path]
                            all_features[descriptor.__name__].append(features)
                    else:
                        print(f"Failed to read image: {image_rel_path}")

    # Convert lists to numpy arrays and save
    for descriptor in descriptors:
        descriptor_name = descriptor.__name__
        signatures = np.array(all_features[descriptor_name])
        np.save(f'signatures_{descriptor_name}.npy', signatures)

    print('Successfully stored!')

# Process datasets
process_datasets('./images', descriptors)

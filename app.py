import streamlit as st
from PIL import Image
import numpy as np
import cv2
from distances import manhattan, euclidean, chebyshev, canberra
from descriptor import glcm, bitdesc
import os

# Load precomputed signatures
signatures_glcm = np.load('signatures_glcm.npy', allow_pickle=True)
signatures_bitdesc = np.load('signatures_bitdesc.npy', allow_pickle=True)

# Define distance functions
distance_functions = {
    'Manhattan': manhattan,
    'Euclidean': euclidean,
    'Chebyshev': chebyshev,
    'Canberra': canberra
}

# Define descriptor functions
descriptor_functions = {
    'GLCM': glcm,
    'BIT': bitdesc
}

# Sidebar with options
st.sidebar.header("Descriptor")
descriptor_choice = st.sidebar.radio("", ("GLCM", "BIT"))

st.sidebar.header("Distances")
distance_choice = st.sidebar.radio("", ("Manhattan", "Euclidean", "Chebyshev", "Canberra"))

st.sidebar.header("Nombre d'Images")
image_count = st.sidebar.number_input("", min_value=1, value=1, step=1)

# Main area
st.title("Content-based Image Retrieval")

uploaded_file = st.file_uploader("Téléverser une image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Convert uploaded image to grayscale and resize
    img = img.convert('L')
    img_array = np.array(img.resize((256, 256)))  # Resize to a standard size for consistency
    
    # Extract features of uploaded image
    descriptor_func = descriptor_functions[descriptor_choice]
    uploaded_image_features = descriptor_func(img_array)
    
    # Select the appropriate signature dataset
    if descriptor_choice == 'GLCM':
        signatures = signatures_glcm
    else:
        signatures = signatures_bitdesc
    
    # Calculate distances between the uploaded image and dataset images
    distances = []
    dist_func = distance_functions[distance_choice]
    
    for signature in signatures:
        feature_vector = signature[:-2]  # Last two items are folder_name and relative_path
        dist = dist_func(uploaded_image_features, feature_vector)
        distances.append((dist, signature[-2], signature[-1]))  # distance, folder_name, relative_path
    
    # Sort distances
    distances.sort(key=lambda x: x[0])
    
    # Display top N similar images
    st.header(f"Top {image_count} images similaires")
    cols = st.columns(4)
    for i in range(image_count):
        dist, folder_name, relative_path = distances[i]
        img_path = os.path.join('images', relative_path)
        similar_img = Image.open(img_path)
        cols[i % 4].image(similar_img, caption=f"{folder_name}", use_column_width=True)
else:
    st.write("Veuillez téléverser une image pour commencer.")

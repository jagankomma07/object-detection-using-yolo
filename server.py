import streamlit as st
from detection.detection_image import detect_objects_in_image
from detection.detection_video import detect_objects_in_video
import os
import time

st.title("YOLO Object Detection App 🚀")

option = st.sidebar.radio("Choose Mode:", ("Image Detection", "Video Detection"))

if option == "Image Detection":
    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        file_path = f"temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.image(file_path, caption="Uploaded Image", width=500)

        if st.button("Submit"):
            # Display loading bar
            with st.spinner("Detecting objects..."):
                time.sleep(1)  # Simulate processing time
                output_path = detect_objects_in_image(file_path)

            st.image(output_path, caption="Detected Objects", width=500)
            os.remove(file_path)

elif option == "Video Detection":
    uploaded_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])
    if uploaded_file:
        file_path = f"temp_{uploaded_file.name}"

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        st.video(file_path)

        if st.button("Submit"):
            with st.spinner("Detecting objects..."):
                time.sleep(1)
                output_path = detect_objects_in_video(file_path)

            print(output_path)
            with open(output_path, "rb") as video_file:
                video_bytes = video_file.read()

                st.video(video_bytes)
                os.remove(file_path)

st.sidebar.write("Developed using YOLOv11 & Streamlit")

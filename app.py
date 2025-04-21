import streamlit as st
from main import main  # Import your main function

st.title("Video Processing App")
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

if uploaded_file:
    with open("input_videos/uploaded_video.mp4", "wb") as f:
        f.write(uploaded_file.read())
    st.write("Processing video...")
    main()  # Call your main function
    st.video("output_videos/output_video.avi")
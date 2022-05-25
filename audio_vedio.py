import streamlit as st
from PIL import Image
st.write('''
# Adding media files in streamlit app

''')
# add image
st.write("## Adding image")
image1 = Image.open("iris_setosa.jpg")
st.image(image1)

# Adding vedio
st.write("## Adding video")
video1 = open("big_buck_bunny_720p_2mb.mp4",'rb')
st.video(video1)
# adding auddio
st.write("## Audio")
audio = open("file_example_MP3_700KB.mp3",'rb')
st.video(audio)
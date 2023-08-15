import streamlit as st
import requests

st.title("Image Downloader")

st.subheader("! Please remove the link and paste your link ")

url = st.text_input("paste link below", "https://kinsta.com/wp-content/uploads/2020/08/tiger-jpg.jpg")
binary_file = requests.get(url)


with open("download.jpg", "wb")as file:
    file.write(binary_file.content)

with open("download.jpg","rb")as file:
    btn = st.download_button(
        label="download",
        mime="image/jpg",
        file_name="download.jpg",
        data=file
    )

st.info("! currently testing now only support jpg format 🙌 ")

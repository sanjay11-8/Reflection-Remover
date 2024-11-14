import streamlit as st
import os
import base64

# Set the path for the predefined images (2.png for display, 7.png for download)
initial_image_path = "2.png"
image_path = "edit.png"

# Check if the predefined images exist
if not os.path.exists(initial_image_path):
    st.error(f"File {initial_image_path} not found. Please make sure '2.png' exists in the directory.")
if not os.path.exists(image_path):
    st.error(f"File {image_path} not found. Please make sure '7.png' exists in the directory.")

# Page styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('https://wallpaperaccess.com/full/1586344.jpg');
        background-size: cover;
        background-position: center;
        height: 100vh;
    }}
    .title {{
        position: absolute;
        margin-top: -10px;
        margin-left: -570px;
        font-size: 45px;
        font-weight: bold;
        color: black;
    }}
    .content {{
        color: black;
        margin-left: 50px;
        margin-right: 10px;
        margin-top: 30px;
        font-size: 43px;
        letter-spacing: 1.5px;
        font-weight: 600;
    }}
    .body-content {{
        color: black;
        margin-left: -100px;
        margin-top: 20px;
        font-size: 24px;
        margin-right: -150px;
        font-weight: 300;
    }}
    .image-container {{
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;
        margin-right: 50px;
    }}
    .custom-image {{
        width: 60%;
        border-radius: 10px;
        margin-right: 150px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Display title and description
st.markdown('<div class="title">MirrorFix</div>', unsafe_allow_html=True)
st.markdown('<div class="content">Remove Reflection from Photos</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="body-content">Easily remove glare from photos online in seconds without affecting the original image quality. Ideal for eliminating sun, light, flash and lens, glass reflections, ensuring your pictures look stunning without any unwanted glare.</div>',
    unsafe_allow_html=True,
)

# Display the initial image (2.png)
if os.path.exists(initial_image_path):
    with open(initial_image_path, "rb") as img_file:
        base64_initial_image = base64.b64encode(img_file.read()).decode("utf-8")
        st.markdown(
            f"""
            <div class="image-container">
                <img src="data:image/png;base64,{base64_initial_image}" class="custom-image">
            </div>
            """,
            unsafe_allow_html=True,
        )

# File upload functionality
uploaded_file = st.file_uploader("Choose a file")

# After the user uploads a file, display the download button and text
if uploaded_file is not None:
    # You can process or display the uploaded file as needed
    st.markdown(
        """
        <div style="font-size:20px; color: black;">
            Click below to download the reflection removed image.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Provide a download button for the predefined '7.png' file
    if os.path.exists(image_path):
        with open(image_path, "rb") as file:
            file_data = file.read()

        st.download_button(
            label="Download image",  # Label for download
            data=file_data,          # The content of the file
            file_name="output.png",       # Name of the file when downloaded
            mime="image/png",        # MIME type for PNG image
        )

        # Provide instructions after the file upload
        st.markdown(
            """
            <div style="font-size:20px; color: black;">
               
            </div>
            """,
            unsafe_allow_html=True,
        )

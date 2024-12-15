import streamlit as st

st.title("Meme Chart Reader")
st.write("This is the beginning of your Meme Chart Reader project.")

# Add a file upload section
uploaded_file = st.file_uploader("Upload a chart image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Chart", use_column_width=True)
    st.write("Processing the chart image...")

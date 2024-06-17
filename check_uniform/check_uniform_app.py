import streamlit as st
import check_uniform.check_uniform_lib as glib

def check_uniform():

 st.title("Check uniform")

 col1, col2, col3 = st.columns(3)
 prompt_text =""

 with col1:
    st.subheader("Select an Image") 
    uploaded_file = st.file_uploader("Select an image", type=['png', 'jpeg'], label_visibility="collapsed")
    if uploaded_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_image_preview)
#  with col2:
    # st.subheader("Prompt")
        
    # prompt_text = st.text_area("Prompt",
    #     value="",
    #     height=100,
    #     help="PG is wearing uniform?",
    #     label_visibility="collapsed")
    
    # go_button = st.button("Go", type="primary")
    
    
 with col2:
    go_button = st.button("Go", type="primary")
    st.subheader("Result")

    if go_button:
        with st.spinner("Processing..."):
            image_bytes = uploaded_file.getvalue()
            response = glib.get_response_from_model(
                prompt_content=prompt_text, 
                image_bytes=image_bytes,
            )
        
        st.write(response)

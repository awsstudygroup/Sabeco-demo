import streamlit as st
import check_in_lib as glib


def check_in():

 st.title("Verify the check-in area")

 col1, col2, col3 = st.columns(3)

 with col1:
    st.subheader("Select an Image") 
    uploaded_file = st.file_uploader("Select an image", type=['png', 'jpg'], label_visibility="collapsed")
    if uploaded_file:
        uploaded_image_preview = glib.get_bytesio_from_bytes(uploaded_file.getvalue())
        st.image(uploaded_image_preview)
    else:
       st.write("Please upload an image to get started.")
#  with col2:
#     st.subheader("Prompt")
#     prompt_text = st.text_area("",
#         value="",
#         height=100,
#         help="What you want to know about the image.?",
#         label_visibility="hidden",
#         key="Đây có phải là quán nhậu, nhà hàng hay nơi tổ chức tiệc không? Ở đó có bán bia Sài Gòn hay không? Giải thích tại sao có và tại sao không?",
#         placeholder="What you want to know about the image.?"
#         )
#     go_button = st.button("Go", type="primary")
    

    
 with col2:
    go_button = st.button("Go", type="primary")
    st.subheader("Result")
    if go_button:
        with st.spinner("Processing..."):
            image_bytes = uploaded_file.getvalue()
            response = glib.get_response_from_model(
                prompt_content="Hãy trả lời câu hỏi sau: đây có phải là quán nhậu, nhà hàng tiệc cưới ? Trả lời có hoặc không? Giải thích tại sao không?",
                image_bytes=image_bytes
            )
        
        st.write(response)

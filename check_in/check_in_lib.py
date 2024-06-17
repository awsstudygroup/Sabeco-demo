import boto3
import json
import base64
from io import BytesIO


#get a BytesIO object from file bytes
def get_bytesio_from_bytes(image_bytes):
    image_io = BytesIO(image_bytes)
    return image_io


#get a base64-encoded string from file bytes
def get_base64_from_bytes(image_bytes):
    resized_io = get_bytesio_from_bytes(image_bytes)
    img_str = base64.b64encode(resized_io.getvalue()).decode("utf-8")
    return img_str


#load the bytes from a file on disk
def get_bytes_from_file(file_path):
    with open(file_path, "rb") as image_file:
        file_bytes = image_file.read()
    return file_bytes


#get the stringified request body for the InvokeModel API call
def get_image_understanding_request_body(prompt, image_bytes, mask_prompt=None, negative_prompt=None):
    input_image_base64 = get_base64_from_bytes(image_bytes)

    system_prompt ="""
        "You are a helpful assistant that helps people understand images. 
        You will answer questions about images and provide helpful information.
        Giải thích đúng với câu trả lời"

        Câu trả lời nếu đây là quán nhậu, nhà hàng hoặc cửa hàng tạp hóa bán bia Sài Gòn sẽ như sau:
        - vi:
            - isConfirm: có
            - isBeer: có 
            - explain:|
                    - ""
                    - "" 
        - en:
            - isConfirm: yes 
            - isBeer: yes
            - explain:|
                    - ""  
                    - "" 

        Câu trả lời nếu đây không phải là quán nhậu, nhà hàng hoặc cửa hàng tạp hóa bán bia Sài Gòn sẽ như sau:
        - vi:
            - isConfirm: không 
            - isBeer: không 
            - explain:|
                    - ""
                    - "" 
        - en:
            - isConfirm: no 
            - isBeer: no
            - explain:|
                    - ""  
                    - "" 
        """
    prompt = f"""{system_prompt}.
        "Quán nhậu, nhà hàng phải là những nơi phục vụ những món ăn, đồ uống có cồn như bia, rượu",
        "Phía trước quán nhậu/nhà hàng sẽ phải có bảng hiệu bao gồm thông tin quán, logo của các thương hiệu bia như bia Sài Gòn và một số thương hiệu bia khác...",
        "Tên quán thường là 'quán nhậu, 'quán nướng', 'nhà hàng tiệc cưới','quán hải sản', 'quán nhậu'",
        "Trong quán sẽ đặt những tủ lạnh, thùng, két bên trong chứa bia Sài Gòn",
        "Hình ảnh quán phải thể hiện rõ ràng, không mờ những thông tin phía trên",
        "Bảng hiệu của quán phải thể hiện rõ ràng thông tin của quán",
        "Trong quán thường đặt những chiếc bàn, ghế, không gian rộng rãi, thoáng mát",
        "Trên bàn phải có chai bia, ly, chén, dĩa, menu...",
    """

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 10000,
        "temperature": 0,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_image_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text":  prompt + "[\n\nisConfirm: 'có/không', is_SG_beer: 'có/không', explain:""]" + "Chỉ trả về định dạng chuẩn file .yml" + "Với 2 ngôn ngữ Việt và Anh" + "Xuống hàng sau mỗi dấu chấm và hiển thị đầy đủ ý nghĩa của câu trả lời, không quá 20 từ ",

                    }
                ],
            }
        ],
    }
    
    return json.dumps(body)



#generate a response using Anthropic Claude
def get_response_from_model(prompt_content=None, image_bytes=None, mask_prompt=None):
    session = boto3.Session()
    
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    body = get_image_understanding_request_body(prompt_content, image_bytes, mask_prompt=mask_prompt)
    
    response = bedrock.invoke_model(body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0", contentType="application/json", accept="application/json")
    
    response_body = json.loads(response.get('body').read()) # read the response
    
    output = response_body['content'][0]['text']
    return output


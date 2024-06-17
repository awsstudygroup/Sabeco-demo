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
def get_check_uniform_request_body(prompt, image_bytes=None, mask_prompt=None, negative_prompt=None):
    
    path_uniform_1 = "./check_uniform/images/uniform-1.jpeg"
    uniform_1_byte = get_bytes_from_file(path_uniform_1)
    input_uniform_1 = get_base64_from_bytes(uniform_1_byte)

    path_uniform_2 = "./check_uniform/images/uniform-2.jpeg"
    uniform_2_byte = get_bytes_from_file(path_uniform_2)
    input_uniform_2 = get_base64_from_bytes(uniform_2_byte)
    
    path_uniform_3 = "./check_uniform/images/uniform-3.jpeg"
    uniform_3_byte = get_bytes_from_file(path_uniform_3)
    input_uniform_3 = get_base64_from_bytes(uniform_3_byte)

    path_uniform_4 = "./check_uniform/images/uniform-4.jpeg"
    uniform_4_byte = get_bytes_from_file(path_uniform_4)
    input_uniform_4 = get_base64_from_bytes(uniform_4_byte)

    path_uniform_5 = "./check_uniform/images/uniform-5.jpeg"
    uniform_5_byte = get_bytes_from_file(path_uniform_5)
    input_uniform_5 = get_base64_from_bytes(uniform_5_byte)

    path_uniform_6 = "./check_uniform/images/uniform-6.jpeg"
    uniform_6_byte = get_bytes_from_file(path_uniform_6)
    input_uniform_6 = get_base64_from_bytes(uniform_6_byte)

    path_uniform_7 = "./check_uniform/images/uniform-7.jpeg"
    uniform_7_byte = get_bytes_from_file(path_uniform_7)
    input_uniform_7 = get_base64_from_bytes(uniform_7_byte)

    path_uniform_8 = "./check_uniform/images/uniform-8.jpeg"
    uniform_8_byte = get_bytes_from_file(path_uniform_8)
    input_uniform_8 = get_base64_from_bytes(uniform_8_byte)

    path_uniform_9 = "./check_uniform/images/uniform-9.jpeg"
    uniform_9_byte = get_bytes_from_file(path_uniform_9)
    input_uniform_9 = get_base64_from_bytes(uniform_9_byte)

    path_uniform_10 = "./check_uniform/images/uniform-10.jpeg"
    uniform_10_byte = get_bytes_from_file(path_uniform_10)
    input_uniform_10 = get_base64_from_bytes(uniform_10_byte)
    
    path_uniform_11 ="./check_uniform/images/uniform-11.jpeg"
    uniform_11_byte = get_bytes_from_file(path_uniform_11)
    input_uniform_11 = get_base64_from_bytes(uniform_11_byte)
    
    path_uniform_12 ="./check_uniform/images/uniform-12.jpeg"
    uniform_12_byte = get_bytes_from_file(path_uniform_12)
    input_uniform_12 = get_base64_from_bytes(uniform_12_byte)


    input_image_base64 = get_base64_from_bytes(image_bytes)
    system_prompt ="""
        "You are a helpful assistant that helps people understand images. 
        You will answer questions about images and provide helpful information.
        So sánh với các hình đồng phục của bia Sài Gòn, sau đó đưa ra câu trả lời chính xác nhất.
        Giải thích đúng với câu trả lời"

        Câu trả lời nếu đây là đồng phục của thương hiệu bia Sài Gòn sẽ như sau:
        - vi:
            - isConfirm: có
            - explain:|
                    - ""
                    - "" 
        - en:
            - isConfirm: yes 
            - explain:|
                    - ""  
                    - "" 

        Câu trả lời nếu đây không phải là đồng phục của thương hiệu bia Sài Gòn sẽ như sau:
        - vi:
            - isConfirm: không 
            - explain:|
                    - ""
                    - "" 
        - en:
            - isConfirm: no 
            - explain:|
                    - ""  
                    - "" 
        """
    prompt = f"""{system_prompt}"""
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 10000,
        "temperature": 0,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Đây là những hình ảnh về các bộ đồng phục của công ty Sabeco:"
                    },
                    {
                        "type": "text",
                        "text": "Hình 1:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_1,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 2:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_2,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 3:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_3,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 4:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_4,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 5:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_5,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 6:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_6,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 7:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_7,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 8:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_8,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 9:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_9,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 10:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_10,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 11:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_11,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Hình 12:"
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg", #this doesn't seem to matter?
                            "data": input_uniform_12,
                        },
                    },
                    {
                        "type": "text",
                        "text": " .Bạn là một người giám sát, hãy giúp tôi xác định: trong"
                    },
                    {
                        "type": "text",
                        "text": "Hình này:"
                    },
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
                        "text": "có sự hiện diện của gương mặt nào không, và nếu có thì người đó có đang mặc đồng phục của công ty Sabeco hay không."
                    },
                    {
                        "type": "text",
                        "text": "Để thực hiện việc này, bạn sẽ: 1.Xác định trong hình có gương mặt của người nào không 2.So sánh trang phục người đó đang mặc với các bộ đồng phục của công ty Sabeco ở trên, nếu giống với một trong các bộ đồng phục của công ty Sabeco ở trên thì kết luận người đó đang mặc đồng phục công ty Sabeco, nếu không giống với bộ đồng phục nào ở trên thì kết luận không phải đang mặc đồng phục công ty Sabeco 3.Trong trường hợp phát hiện trên trang phục của người đó đang mặc có từ 'BIA SAIGON' hoặc 'BIA LẠC VIỆT' thì kết luận người đó đang mặc đồng phục công ty Sabeco 4.Nếu trong hình ảnh chỉ có gương mặt của người, không xác định được trang phục họ đang mặc thì kết luận là không mặc đồng phục công ty Sabeco 5.Nếu hình bị mờ hoặc tối, không thấy rõ chi tiết để so sánh với các bộ đồng phục ở trên thì kết luận người này đang không mặc đồng phục của công ty Sabeco."
                    },
                    {
                        "type": "text",
                        "text": "Kết quả trả về chỉ bao gồm một câu kết luận có gương mặt người nào không và người đó có đang mặc đồng phục của công ty Sabeco hay không. Không trả lời, giải thích gì thêm."
                    },
                    {
                        "type":"text",
                        "text": prompt +"[\n\nisConfirm: 'có/không', explain:""]" + "Chỉ trả về định dạng file .yml" + "Với 2 ngôn ngữ Việt và Anh" + "Xuống hàng sau mỗi dấu chấm và hiển thị đầy đủ ý nghĩa của câu trả lời, không quá 20 từ ",
                    }
                ],
            }
        ],
    }
    return json.dumps(body)



#generate a response using Anthropic Claude
def get_response_from_model(prompt_content, image_bytes, mask_prompt=None):
    session = boto3.Session()
    
    bedrock = session.client(service_name='bedrock-runtime') #creates a Bedrock client
    
    body = get_check_uniform_request_body(prompt_content, image_bytes, mask_prompt=mask_prompt)
    
    response = bedrock.invoke_model(body=body, modelId="anthropic.claude-3-sonnet-20240229-v1:0", contentType="application/json", accept="application/json")
    
    response_body = json.loads(response.get('body').read()) # read the response
    
    output = response_body['content'][0]['text']
    
    return output


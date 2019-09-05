import requests
import json

subscription_key = "db453537d41a4a89b26ca9fba22a58e7"
assert subscription_key
    
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

def get_face_data(image_url):

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image_url})
    face_data_raw = response.json()
    return face_data_raw

def organize_data(face_data_raw):
    face_data_organized = {
        "face_top" : face_data_raw[0]["faceRectangle"]["top"],
        "face_left" : face_data_raw[0]["faceRectangle"]["left"],
        "face_w" : face_data_raw[0]["faceRectangle"]["width"],
        "face_h" : face_data_raw[0]["faceRectangle"]["height"]
    }
    print(face_data_organized)
    return face_data_organized

# organize_data(get_face_data(image_url)) 
# This returns a dictionary with face details
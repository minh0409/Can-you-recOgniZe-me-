import io
import os
import webbrowser

# Imports the Google Cloud client library  
from google.cloud import vision
from google.cloud.vision import types

from flask import Flask
app= Flask(__name__)



credential_path = r"C:\Users\Jasdeep\Downloads\swamphack2019-9f9ff1b7129f.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
def labels():
# Instantiates a client
    client = vision.ImageAnnotatorClient()
    
    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'beach.jpg')
    
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    image = types.Image(content=content)
    
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    
    print('Labels:')
    for label in labels:
        output=print(label.description)
    return labels
    
@app.route("/")
def hello():
    
            
    return str(labels())

if __name__ == '__main__' :
    app.run()
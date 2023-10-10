
from PIL import Image
from pytesseract import image_to_string
from gtts import gTTS

def sound_image(path_to_image):
    try :
        load_image =  image_to_string(Image.open(path_to_image))
        gTTS(load_image,lang='en',tld='co.in').save('result.mp3')
    except Exception as e:
        print("error : ", e)

if __name__== "__main__":
    sound_image("test.png")

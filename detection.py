from flask import Flask, render_template, request
from keras.preprocessing import image
from keras.models import load_model
# import uvicorn   
import numpy as np
import tensorflow as tf
# from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model
  
app = Flask(__name__)

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return render_template('index.html')
    


MODEL = tf.keras.models.load_model("models/4")






CLASS_NAMES = ['Amaltas',
 'False ashoka',
 'Mauritius hemp',
 'daisy',
 'dandelion',
 'paper flower',
 'rose',
 'sunflower',
 'thuja',
 'tulip']
    

        
        

def predict_image(img_path):
    test_image = image.load_img(img_path, target_size=(256,256) )
    test_image = image.img_to_array(test_image)

    test_image = np.expand_dims(test_image,axis=0)

    predictions = MODEL.predict(test_image)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    if predicted_class == CLASS_NAMES[0]:
        bio_name="Cassia fistula"
        area="South-East Asia"
        med="fruits are used in the treatment of diabetes."
    elif predicted_class == CLASS_NAMES[1]:
        bio_name="Polyalthia longifolia"
        area="southern India and Sri Lanka"
        med="used for treating fever, mouth ulcers, menorrhagia, scorpion sting, diabetes, and skin disease."
    elif predicted_class == CLASS_NAMES[2]:
        bio_name="Furcraea foetida"
        area="Caribbean, South America"
        med="An infusion with sweet oil is drunk as a treatment for syphilis."
    elif predicted_class == CLASS_NAMES[3]:
        bio_name="Bellis perennis"
        area="You Can Find Daisies Growing Everywhere"
        med="wild daisy tea for coughs, bronchitis, disorders of the liver and kidneys, and swelling."
    elif predicted_class == CLASS_NAMES[4]:
        bio_name="Taraxacum"
        area="areas with moist soils."
        med="used as a mild appetite stimulant, and to improve upset stomach."
    elif predicted_class == CLASS_NAMES[5]:
        bio_name="bougainvillea glabra"
        area="South America"
        med="anticancer, antidiabetic, anti-inflammatory, antimicrobial and antioxidant properties."
    elif predicted_class == CLASS_NAMES[6]:
        bio_name="Rosa"
        area="Asia"
        med="Anti-depressant, anti-spasmodic, aphrodisiac, astringent, increase bile production, cleansing, anti- bacterial and antiseptic."
    elif predicted_class == CLASS_NAMES[7]:
        bio_name="Helianthus"
        area="North and South America"
        med="Sunflower oil is used for constipation and lowering bad LDL cholesterol."
    elif predicted_class == CLASS_NAMES[8]:
        bio_name="thuja"
        area="North America and three native to eastern Asia."
        med="used for respiratory tract infections such as bronchitis, bacterial skin infections, and cold sores."
    elif predicted_class == CLASS_NAMES[9]:
        bio_name="Tulipa"
        area="Southern Europe to Central Asia"
        med="Have diuretic properties, It has anti-septic properties."

    confidence = np.max(predictions[0])
    return predicted_class, confidence, bio_name, area, med

    



   
 
   
@app.route('/', methods=['GET', 'POST'])
def getvalue():
    if request.method == 'POST':
       img = request.files['imgfile']
       img_path = "static/images/" + img.filename
       img.save(img_path)
       output, confidence, bio_name, area, med = predict_image(img_path)
       print(output)

    return render_template('result.html', o=output, confi=confidence, fimage=img.filename,bio=bio_name, ar=area, me=med)  


# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)

from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
# from PIL import Image

app = Flask(__name__)

dic = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
x = np.array(dic)
model = load_model('model.h5')

model.make_predict_function()

def predict_label(img_path):
	test_image = image.load_img(img_path, target_size=(64,64))
	test_image = image.img_to_array(test_image)
	test_image.reshape(1,64,64,3)
	test_image = np.expand_dims(test_image, axis = 0)
	test_image=test_image/255
	result =model.predict(test_image)
	# print("Hey dude")
	# print(x)
	# print("done dude")
	print(x[np.argmax(result)])
	return (x[np.argmax(result)])


# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/about")
def about_page():
	return "Please subscribe  Artificial Intelligence Hub..!!!"

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(port=8080, debug=True)
	# app.run(debug = True)
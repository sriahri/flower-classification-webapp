### Flower Classification

Flower classification is one of the most basic problem in the field of Computer Vision. The main objective of the algorithm is to recognize the flower category based on the image provided.
Classification problem of recognizing the flower types – rose, chamomile, dandelion, sunflower, & tulip.

## Dataset:
Download the dataset at this ![link](https://www.kaggle.com/datasets/alxmamaev/flowers-recognition/download?datasetVersionNumber=2)

## Model:
We build a CNN using tensorflow library as it contains all the functionalities that one may need to define the architecture of a Convolutional Neural Network and train it on the data.
The model consists of the following:
3 Convolutional layers
2 MaxPooling layers
1 Dropout layer
The optimizer used is adam and the loss function is categorical cross entropy.

## Callbacks
I have defined 1 callback
ModelCheckpoint — To save the best model during training

## Training and evaluation
The model is being trained for 200 epochs with steps per epoch as 135.
As we don’t have a large amount of data, we use Image Augmentation to synthesize more data and train our model with it.
The model reached a validation accuracy of 99.5% and accuracy of 99% which is very good.

## Web Application:
To create a web application with the Machine Learning model as back end, we use the flask frameowrk of python.
The static folder contains all the test samples and the templates folder contains all the html files.
The index.html file is the main page of the web application.
The app.py is run on gunicorn server with port 8080.
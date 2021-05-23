from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
import json
from tensorflow import Graph
import os

img_height, img_width=224,224
# Create your views here.
model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=load_model('./models/fine_model.h5')

def index(request):
    return render(request, 'disease/index.html')

def contact(request):
    return render(request, 'disease/contact.html')

def information(request):
    return render(request,'disease/information.html')

def help(request):
    return render(request,'disease/help.html')

def seedoctor(request):
    return render(request,'disease/seedoctor.html')    

def uploadskin(request):
    return render(request, 'disease/uploadskin.html')

def resultsskin(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['file']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x / 255
    x = x.reshape(1, img_height, img_width, 3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi = model.predict(x)

    import numpy as np

    if (predi > 0.5):
        predictedLabel = "Melanoma"
    else:
        predictedLabel = "Not Melanoma"
    context = {'filePathName': filePathName, 'predictedLabel': predictedLabel}
    return render(request, 'disease/results.html', context)


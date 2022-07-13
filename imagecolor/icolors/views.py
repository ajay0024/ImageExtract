from django.shortcuts import render
from PIL import Image
import numpy as np
from sklearn.cluster import MiniBatchKMeans
from django.conf import settings


def index(request):
    if request.method == 'POST':
        file_img = request.FILES['img']
        uploaded_file(file_img)
        img = Image.open(file_img)
        img_address = 'tempo.jpg'
    else:
        img = Image.open(settings.STATIC_ROOT+'/images/3604882.jpg')
        img_address = '3604882.jpg'
    array = np.asarray(img)
    array = array.reshape(-1, 3)
    # print(array, array.shape)
    clt = MiniBatchKMeans(n_clusters=10)
    clt.fit(array)
    result = clt.cluster_centers_
    print(result)
    newArray = []
    for x in result:
        newArray.append('#%02x%02x%02x' % (int(x[0]), int(x[1]), int(x[2])))
    print(clt.cluster_centers_)
    context_dict = {"img_address": img_address, "a": "Ajay", "colors": newArray}
    return render(request, 'icolors/index.html', context=context_dict)
    # return render(request, 'icolors/index.html')


def uploaded_file(f):
    with open('static/images/tempo.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

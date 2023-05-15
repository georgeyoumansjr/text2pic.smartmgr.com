import os
import io
import openai
from PIL import Image

from django.shortcuts import render

openai.api_key = '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'
# Create your views here.

def index(request):

    return render(request, 'index.html')

def generate(request):
    context = {}
    if request.method == 'POST':
        prompt = request.POST.get('prompt',None)
        size = request.POST.get('size', '256x256' )
        n = int(request.POST.get('n', '1' ))
        

        if prompt:
            response = openai.Image.create(
                prompt=prompt,
                n=n,
                size=size
            )
            data = response['data']
                
            context['data'] = data
        

    return render(request, 'generate.html', context)

def edit(request):
    context = {}
    if request.method == 'POST':
        image = request.FILES['image']
        prompt = request.POST.get('prompt',None)
        size = request.POST.get('size', '256x256' )
        n = int(request.POST.get('n', '1' ))

        # image = image.read()
        image = Image.open(image)
        png_rgba = io.BytesIO()
        image = image.convert('RGBA')
        image.save( png_rgba, format='PNG' )
        png_rgba.seek(0)
        # image = image.tobytes()

        if prompt and image:
            response = openai.Image.create_edit(
                image=png_rgba,  #open(image, "rb"),
                prompt=prompt,
                n=n,
                size=size
            )
            data = response['data']
                
            context['data'] = data
        

    return render(request, 'edit.html', context)


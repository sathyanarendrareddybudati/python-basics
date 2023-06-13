# from django.core.files.storage import default_storage
from django.http import HttpResponse
from PIL import Image
import io
# def convert_image(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         image_file = request.FILES['image']
#         try:
#             # Open the image using Pillow
#             image = Image.open(image_file)
#             # Resize the image to the specified dimensions
#             width = request.POST.get('width')
#             height = request.POST.get('height')
#             if width and height:
#                 image = image.resize((int(100), int(100)))
#             # Convert the image to the WebP format
#             output_file = default_storage.open('satya.jpeg', 'wb')
#             image.save(output_file, 'webp')
#             output_file.close()
#             # Return the output file as the API response
#             with default_storage.open('output.webp', 'rb') as f:
#                 response = HttpResponse(f.read(), content_type='image/webp')
#             return response
#         except Exception as e:
#             print('satya')
#             return HttpResponseBadRequest(str(e))
       
#     else:
#         return HttpResponseBadRequest('Image file not provided.')

def post(self, request):
        # if request.method == 'POST':
        image_file = request.FILES['static/images/satya.jpeg']
        # Get the image from the request
        img = Image.open(image_file)

        # Resize the image
        size = (100, 100)
        img.thumbnail(size)

        # Convert the image to webp format
        image_io = io.BytesIO()
        img.save(image_io, format='webp')

        # Return the converted image in response
        return HttpResponse(image_io.getvalue(), content_type='image/webp')

import traceback
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from .ai_model import predict_shape, classes


def home(request):
    return render(request, "recognition/home.html")



@csrf_exempt
def predict_shape_view(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if not image_file:
            return JsonResponse({'error': 'No image provided'}, status=400)

        try:

            img = Image.open(image_file).convert("RGB")


            preds = predict_shape(img)
            print("Prediction:", preds)


            if isinstance(preds, int):  # np.argmax output
                if preds >= len(classes):
                    return JsonResponse({'error': f'Predicted index {preds} out of range!'}, status=500)
                shape = classes[preds]
            else:
                shape = str(preds)  # fallback

            return JsonResponse({'shape': shape})

        except Exception as e:
            print(traceback.format_exc())  # كامل traceback
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

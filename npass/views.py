import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .ml import predict

def home(request):
    return render(request, "cybersickness/home.html")

@csrf_exempt
@require_POST
def cybersickness_predict_view(request):
    try:
        data = json.loads(request.body or "{}")
        gender = data.get("gender")
        gad_score = data.get("gad_score")
        task_condition = data.get("task_condition")

        if gender is None or gad_score is None or task_condition is None:
            return JsonResponse({"error": "Missing required fields."}, status=400)

        model_input = {
            "gender": gender,
            "gad_score": gad_score,
            "task_condition": task_condition
        }

        result = predict(model_input)

        return JsonResponse({
            "prediction": result,
            "message": "Cybersickness Risk Detected" if result == 1 else "Low Cybersickness Risk"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
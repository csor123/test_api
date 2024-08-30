from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


@csrf_exempt
@require_POST
def add(request):
    return calculate(request, lambda a, b: a + b)


@csrf_exempt
@require_POST
def subtract(request):
    return calculate(request, lambda a, b: a - b)


@csrf_exempt
@require_POST
def multiply(request):
    return calculate(request, lambda a, b: a * b)


@csrf_exempt
@require_POST
def divide(request):
    try:
        return calculate(request, lambda a, b: a / b)
    except ZeroDivisionError:
        return JsonResponse({"error": "Division by zero!"}, status=400)


def calculate(request, operation):
    try:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Inputs must be numbers")

        result = operation(a, b)
        return JsonResponse({"answer": result})

    except (ValueError, KeyError) as e:
        return JsonResponse({"error": str(e)}, status=400)


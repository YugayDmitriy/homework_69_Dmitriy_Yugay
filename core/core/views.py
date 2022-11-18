import json
from django.http.response import JsonResponse


def add(request, *args, **kwargs):
    answer = {}
    if request.body:
        number = json.loads(request.body)
        try:
            numb1 = int(number['A'])
            numb2 = int(number['B'])
            res = numb1 + numb2
            answer['res'] = res
        except ValueError as e:
            answer['error'] = 'There is a non-numeric value among the entered values'
            return JsonResponse(answer, status=400)
    return JsonResponse(answer)


def subtract(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            numb1 = int(numbers['A'])
            numb2 = int(numbers['B'])
            res = numb1 - numb2
        except ValueError as e:
            answer['error'] = 'There is a non-numeric value among the entered values'
            return JsonResponse(answer, status=400)
    answer['res'] = res
    return JsonResponse(answer)


def multiply(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            numb1 = int(numbers['A'])
            numb2 = int(numbers['B'])
            res = numb1 * numb2
        except ValueError as e:
            answer['error'] = 'There is a non-numeric value among the entered values'
            return JsonResponse(answer, status=400)
    answer['res'] = res
    return JsonResponse(answer)


def divide(request, *args, **kwargs):
    answer = {}
    if request.body:
        numbers = json.loads(request.body)
        try:
            numb1 = int(numbers['A'])
            numb2 = int(numbers['B'])
        except ValueError as e:
            answer['error'] = 'There is a non-numeric value among the entered values'
        try:
            res = numb1 / numb2
            answer['res'] = res
            return JsonResponse(answer)
        except ZeroDivisionError:
            answer['error'] = "На ноль делить нельзя"
            return JsonResponse(answer, status=400)

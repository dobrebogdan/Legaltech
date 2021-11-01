from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Legaltech.suggestions import get_top_suggestions_from_text
from Legaltech.portal_just import get_ids_and_solutions

def index(request):
    return render(request, 'app/index.html', {})

@csrf_exempt
def get_laws(request):
    text = request.POST.get("param")
    laws = get_top_suggestions_from_text(text)
    response = []
    for law in laws:
        response.append(law.text)
    return JsonResponse({"response": response})

@csrf_exempt
def get_cases(request):
    cases = get_ids_and_solutions(obiect_dosar='furt')
    return JsonResponse({'response': cases})


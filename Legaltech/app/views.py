from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Legaltech.suggestions import get_top_suggestions_from_text

def index(request):
    return render(request, 'app/index.html', {})

@csrf_exempt
def getevents(request):
    text = request.POST.get("param")
    articles = get_top_suggestions_from_text(text)
    response = []
    for article in articles:
        response.append(article.text)
    return JsonResponse({"response": response})

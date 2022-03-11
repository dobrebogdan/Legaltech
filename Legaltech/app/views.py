from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Legaltech.suggestions import get_top_suggestions_from_text, load_articles_for_language
from Legaltech.portal_just import get_ids_and_solutions, get_cases

def index(request):
    return render(request, 'app/index.html', {})

lang = 'ro'
load_articles_for_language(lang)

@csrf_exempt
def set_language(request):
    new_lang = request.POST.get('param')
    if new_lang in ['en', 'ro']:
        global lang
        lang = new_lang
        load_articles_for_language(lang)
    return JsonResponse({'response': 'ok'})

@csrf_exempt
def get_laws(request):
    text = request.POST.get('param')
    laws = get_top_suggestions_from_text(text, lang=lang)
    response = []
    for law in laws:
        response.append(law.text)
    return JsonResponse({'response': response})

@csrf_exempt
def get_cases(request):
    param = request.POST.get('param').split(',')
    obiect_dosar = ''
    institutie = ''
    if len(param) >= 1:
        obiect_dosar = param[0]
    if len(param) >= 2:
        institutie = param[1]
    cases = get_ids_and_solutions(obiect_dosar=obiect_dosar, institutie=institutie)
    return JsonResponse({'response': cases})

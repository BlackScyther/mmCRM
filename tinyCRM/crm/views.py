from django.shortcuts import render

crm_interactions = [
    {
        'title': 'Interaction 1',
        'content': 'contact per mail regarding meetiing',
        'date_created': 'Wednesday 03. 01. 2019'
    },
    {
        'title': 'Interaction 2',
        'content': 'contact per phone regarding presentation',
        'date_created': 'Wednesday 03. 01. 2019'
    }
]

indexHtml = 'crm/interactions.html'

def index(request):
    context = {
        'crm_interactions': crm_interactions
    }
    return render(request, indexHtml, context)

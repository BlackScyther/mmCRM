from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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


@login_required
def index(request):
    context = {
        'crm_interactions': crm_interactions
    }
    return render(request, 'crm/interactions.html', context)


@login_required
def cases(request):
    context = {
        'crm_interactions': crm_interactions
    }
    return render(request, 'crm/cases.html', context)

from django.shortcuts import render

# Create your views here.

all = [
    "main",
]

def main(request):
    project = {
        'name': 'SSite',
        'developer': {
            'name': 'Даниил',
            'last_name': 'Черняк',
            'email': 'chernyak.daniil.2010@gmail.com'
        },
        'description': 'У этого сайта нет описания',
        'created_at': '20.06.2023',
    }
    return render(request, 'main.html', context={"project": project, "title": "SSite project"})

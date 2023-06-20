from django.shortcuts import render


all = (
    "main",
)


def main(request):
    project = {
        'name': 'SSite',
        'description': 'У этого сайта нет описания',
        'developers': [
            {
                'name': 'Даниил',
                'last_name': 'Черняк',
                'email': 'chernyak.daniil.2010@gmail.com'
            }
        ],
        'created_at': '20.06.2023',
    }
    return render(request, 'SSite/main.html', context={"project": project, "title": "SSite project"})

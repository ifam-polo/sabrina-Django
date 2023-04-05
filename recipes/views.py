from django.shortcuts import render



def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name':'Sabrina'})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe_view.html', context={
        'name': 'Sabrina Frazão',
    })
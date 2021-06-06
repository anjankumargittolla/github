from django.shortcuts import render
from github import Github


# Create your views here.


def home(request):
    """For home page"""
    return render(request, 'rep_list/home.html', {})


def total_list(request):
    """To display all repositories in git"""
    if request.method == "POST":
        g = Github()
        name = request.POST['username']
        h = g.get_user(name)
        print(h)
        r = h.get_repos()
        total = []
        for i in r:
            total.append(i.name)
        return render(request, 'rep_list/list.html', {"list": total, "name" : name})

from django.shortcuts import render


def test(request):
    return render(request,"home_page/test.html")
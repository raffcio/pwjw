from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the <b>dbimport</b> index.")
	
def detail(request, book_id):
    return HttpResponse("You're looking at book %s." % book_id)
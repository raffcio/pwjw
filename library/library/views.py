from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from .models import Book, DBImport

def index(request):
	book_list = Book.objects.order_by('pId')
	#template = loader.get_template('library/index.html')
	context = {'book_list': book_list}
	return render(request,'library/index.html', context)
	
def szczegoly(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, 'library/szczegoly.html', {'book': book})
	
def imports(request):
	return render(request, 'library/DBimport.html')
	
def DBimport(request):
	DBImport()
	return HttpResponse("<meta http-equiv='Refresh' content='0; url=..' />")
	
def DBdelete(request):
	Book.objects.all().delete()
	return HttpResponse("<meta http-equiv='Refresh' content='0; url=../' />")
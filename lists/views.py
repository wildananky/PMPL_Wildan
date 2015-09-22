from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')
	
	items = Item.objects.all()

	count = items.count()
	
	if(count == 0):
		comment = 'yey, waktunya berlibur'
	elif(count < 5):
		comment = 'sibuk tapi santai'
	elif(count >= 5):
		comment = 'oh tidak'
	

	return render(request, 'home.html', {'items': items, 'comment' : comment})

def view_list(request):
	# Item.objects.create(text=request.POST['item_text'])
	# return render(request, 'home.html', {'items': items})
	pass
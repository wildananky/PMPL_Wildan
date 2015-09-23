from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text'])
		return redirect('/lists/the-only-list-in-the-world/')
	
	return render(request, 'home.html')
	# count = items.count()
	
	# if(count == 0):
	# 	comment = 'yey, waktunya berlibur'
	# elif(count < 5):
	# 	comment = 'sibuk tapi santai'
	# elif(count >= 5):
	# 	comment = 'oh tidak'
	
def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {'items': items})
	
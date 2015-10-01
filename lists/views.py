from django.shortcuts import redirect, render
from lists.models import Item, List

# Create your views here.
def home_page(request):
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['item_text'])
	# 	return redirect('/lists/the-only-list-in-the-world/')
	
	
	# count = items.count()
	
	# if(count == 0):
	comment = 'yey, waktunya berlibur'
	# elif(count < 5):
	# 	comment = 'sibuk tapi santai'
	# elif(count >= 5):
	# 	comment = 'oh tidak'
	return render(request, 'home.html', {'comment' : comment})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	# print(Item.objects.filter(list=list_).count())
	count = Item.objects.filter(list=list_).count()

	#count = items.count()
	
	if(count == 0):
		comment = 'yey, waktunya berlibur'
	elif(count < 5):
		comment = 'sibuk tapi santai'
	elif(count >= 5):
		comment = 'oh tidak'
	return render(request, 'list.html', {'list': list_,'comment': comment})
	
def new_list(request):
	list_ = List.objects.create()
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['item_text'], list=list_)
	return redirect('/lists/%d/' % (list_.id,))

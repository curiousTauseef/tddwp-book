# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import redirect, render
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		new_item_text = request.POST['item_text']
		Item.objects.create(text=new_item_text) #MN: Don't need to call save() with create.
		return redirect('/')

	items = Item.objects.all()
	return render(request, 'home.html', {'items': items})

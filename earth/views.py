from django.shortcuts import render
from django.views import generic
from django.http import Http404, HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

from .models import Winemag

def IndexView(request):
	text = request.GET.get('text')
	field = request.GET.get('field')

	if(text and field):
		if(field == 'country'):
			return render(request, 'earth/index.html', {
				'list_data': Winemag.objects.filter(country = text)
			})
		elif(field == 'province'):
			return render(request, 'earth/index.html', {
				'list_data': Winemag.objects.filter(province = text)
			})
		elif(field == 'region'):
			results = Winemag.objects.filter(Q(region_1 = text) | Q(region_2 = text))
			return render(request, 'earth/index.html', {
				'list_data': results
			})
	else:
		return render(request, 'earth/index.html', {
			'list_data': Winemag.objects.all()
		})

def OneWineList(request):

	wine_type = request.GET.get('wine_type')
	sort = request.GET.get('sort')
	grape = request.GET.get('grape')
	if(wine_type):
		try:
			results = Winemag.objects.filter(winery = wine_type)
		except (KeyError, Winemag.DoesNotExist):
			return render(request, 'earth/oneWine.html', {
				'wine_type': wine_type,
				'error_message': 'Wine Not Available'
			})
		else:
			if(sort == 'asc'):
				results = results.order_by('price')
			elif(sort == 'desc'):
				results = results.order_by('-price')
			return render(request, 'earth/oneWine.html', {
				'wine_type': wine_type,
				'results': results
			})
	else:
		if(grape):
			return render(request, 'earth/wineList.html', {
				'all_wines': Winemag.objects.filter(variety = grape).values('winery').distinct()
			})
		return render(request, 'earth/wineList.html', {
			'all_wines': Winemag.objects.values('winery').distinct()
		})
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')

	context = {}
	return render(request, {})

def about(request):
	return render(request, 'about.html')

	context = {}
	return render(request, {})

def causes(request):
	return render(request, 'causes.html')

	context = {}
	return render(request, {})


def contact(request):
	return render(request, 'contact.html')

	context = {}
	return render(request, {})


def portfolio(request):
	return render(request, 'portfolio.html')

	context = {}
	return render(request, {})


def single_causes(request):
	return render(request, 'single-causes.html')

	context = {}
	return render(request, {})

def news(request):
	return render(request, 'news.html')

	context = {}
	return render(request, {})
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse

class GrandpaView(View):
	template = 'deafgrandpa/index.html'
	def get(self, request):
		return render(request, self.template)

	def post(self, request):
		said = request.POST['said']
		if said.isupper():
			said = 'You said: ' + said
		else: 
			said = 'SPEAK UP BEFORE I WACK YOU WITH MY CANE'
		return JsonResponse({'said': said})

	
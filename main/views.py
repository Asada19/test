from django.shortcuts import render, redirect
from django.views import View
from .models import ValueForInput


class InputValueView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        input_value = request.POST.get('input_value')
        ValueForInput.objects.create(value=input_value,)
        return render(request, self.template_name, {'message': 'success'})


class OutputValueView(View):
    template_name = 'last_input.html'

    def get(self, request):
        value = ValueForInput.objects.all()
        return render(request, self.template_name, context={'values': value})

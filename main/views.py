from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import ValueForInput


class InputValueView(View):
    template_name = 'index.html'

    def get(self, request):
        latest_value_id = request.session.get('latest_value_id', 0)
        value = get_object_or_404(ValueForInput, id=latest_value_id + 1)
        request.session['latest_value_id'] = value.id
        return render(request, self.template_name, context={'value': value})

    def post(self, request):
        input_value = request.POST.get('input_value')
        ValueForInput.objects.create(value=input_value,)
        return render(request, self.template_name, {'message': 'success'})

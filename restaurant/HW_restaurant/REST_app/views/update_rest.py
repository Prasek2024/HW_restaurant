from django.urls import reverse_lazy
from django.views.generic import UpdateView
from ..models import Rest_list
from ..forms import Restaurant_list


class RestUpdateView(UpdateView):
    model = Rest_list
    form_class = Restaurant_list
    template_name = 'rest_form.html'
    success_url = reverse_lazy('rest_list')
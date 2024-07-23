from django.urls import reverse_lazy
from django.views.generic import DeleteView
from ..models import Rest_list


class RestDeleteView(DeleteView):
    model = Rest_list
    template_name = 'rest_confirm_delete.html'
    success_url = reverse_lazy('rest_list')
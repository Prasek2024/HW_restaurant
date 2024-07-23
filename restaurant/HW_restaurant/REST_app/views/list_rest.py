from django.views.generic import ListView
from ..models import Rest_list


class RestListView(ListView):
    model = Rest_list
    template_name = 'rest_list.html'
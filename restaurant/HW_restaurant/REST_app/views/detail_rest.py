from django.views.generic import DetailView
from ..models import Rest_list


class RestDetailView(DetailView):
    model = Rest_list
    template_name = 'rest_detail.html'
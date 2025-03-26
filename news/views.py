from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['content'] = self.object.content
        return context 
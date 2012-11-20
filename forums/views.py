from django.views.generic import ListView, DetailView, FormView

from forms import TopicCreateForm
from models import Category, Topic, Forum


class CategoryListView(ListView):
    model = Category

class ForumDetailView(DetailView):
    model = Forum

class TopicDetailView(DetailView):
    model = Topic

class TopicCreateView(FormView):
    template_name = 'forums/topic_create.html'
    form_class = TopicCreateForm

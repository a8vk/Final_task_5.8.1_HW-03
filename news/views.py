from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import New
from .filters import NewFilter


class NewsListView(ListView):
    model = New
    template_name = 'default.html'
    context_object_name = 'news'
    ordering = ['-data_pub']
    paginate_by = 10


class NewDetailView(DetailView):
    model = New
    template_name = 'detail.html'
    context_object_name = 'new'


class UncosNewsListView(ListView):
    model = New
    template_name = 'uncos.html'
    context_object_name = 'news'
    ordering = ['-data_pub']
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(category='uncos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        current_page = context['page_obj']
        start_index = max(current_page.number - 2, 1)
        end_index = min(current_page.number + 2, paginator.num_pages)
        page_range = range(start_index, end_index + 1)
        context['page_range'] = page_range
        return context


class ArticlesNewsListView(ListView):
    model = New
    template_name = 'articles.html'
    context_object_name = 'news'
    ordering = ['-data_pub']
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(category='articles')


class NewsSearchView(ListView):
    model = New
    template_name = 'news_search.html'
    context_object_name = 'news'
    ordering = ['-data_pub']
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return New.objects.filter(title__icontains=query)
        return New.objects.all()


def news_search(request):
    news_list = New.objects.all()
    news_filter = NewFilter(request.GET, queryset=news_list)
    return render(request, 'news_search.html', {'filter': news_filter, 'news_list': news_filter.qs})


class UncosCreateView(CreateView):
    model = New
    fields = ['title', 'text', 'category']
    template_name = 'news_form.html'


class UncosUpdateView(UpdateView):
    model = New
    fields = ['title', 'text', 'category']
    template_name = 'news_edit.html'


class UncosDeleteView(DeleteView):
    model = New
    success_url = reverse_lazy('index')
    template_name = 'news_confirm_delete.html'


class ArticlesCreateView(CreateView):
    model = New
    fields = ['title', 'text', 'category']
    template_name = 'articles_form.html'


class ArticlesUpdateView(UpdateView):
    model = New
    fields = ['title', 'text', 'category']
    template_name = 'articles_edit.html'


class ArticlesDeleteView(DeleteView):
    model = New
    success_url = reverse_lazy('articles')
    template_name = 'articles_confirm_delete.html'

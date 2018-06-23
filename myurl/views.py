from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import MyURL
from django.urls import reverse_lazy

class MyUrlList(ListView):
    def get_queryset(self):
        return MyURL.objects.filter(owner= self.request.user, active= True)

class MyUrlAdd(CreateView):
    model = MyURL
    fields = ['name','text']
    success_url = reverse_lazy('myurl-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
class MyURLUpdate(UpdateView):
    model = MyURL
    fields = ['name','text']
    success_url = reverse_lazy('myurl-list')

class MyURLDelete(DeleteView):
    model = MyURL
    success_url = reverse_lazy('myurl-list')


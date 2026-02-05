from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from . import models, forms

# Create your views here.
class ProjectistView(ListView):
    model = models.Project
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('project_list')

class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'

    def get_success_url(self):
        return reverse('project_update', args=[self.object.id])

class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy('project_list')
    template_name = 'project/delete.html'




class TaskCreateView(CreateView):
    model = models.Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])

class TaskUpdateView(UpdateView):
    model = models.Task
    fields = ['is_complete']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])

class TaskDeleteView(DeleteView):
    model = models.Task


    def get_success_url(self):
        return reverse('project_update', args=[self.object.project.id])


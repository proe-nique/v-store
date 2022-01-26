#from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.contrib import messages
from users.forms import ProfileForm
from .models import Profile
# Create your views here.


class UserDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'Timeline'
        return context
    

class UserListView(ListView):
    model = Profile
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'people'
        return context


class UserUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "update_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'update profile'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.user} has been successfully updated.")
        return super(UserUpdateView, self).form_valid(form)


class UserDeleteView(DeleteView):
    model = Profile
    template_name = "confirm_delete_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = 'delete profile'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f"{form.instance.name} has been successfully deleted.")
        return super(UserDeleteView, self).form_valid(form)
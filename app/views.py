from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
from django.urls import reverse
from django.views.generic import UpdateView
 
def index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/master.html', page)
 
def edit(request, edit_id):
    item = Todo.objects.get(e=edit_id)
    template = loader.get_template('master.html')
    context = {
        "edit":item
    }
    return redirect(edit)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

# class ItemUpdate(UpdateView):
#     model = Todo
#     fields = [
#         "title",
#         "details",
#         "date"
#     ]

#     def get_context_data(self,edit):
#         context = super(ItemUpdate, self).get_context_data()
#         context["todo_list"] = self.object.master
#         context["title"] = "Edit item"
#         return context

#     def get_success_url(self):
#         return reverse("list", args=[self.object.todo_list_id])
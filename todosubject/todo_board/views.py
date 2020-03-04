from django.shortcuts import render

# Create your views here.
from django.views import generic

from todo_board.models import TodoList


class todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_list.html'
        todo_list = TodoList.objects.all()
        return render(request, template_name,{'todo_list':todo_list})

from django import forms

from todo_board.models import TodoList


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = {'title', 'content', 'end_date'}

from django import forms
from tasks.models import TodoItem

class AddTaskForm(forms.Form):
	description = forms.CharField(max_length=64, label='')

class TodoItemForm(forms.ModelForm):
	class Meta:
		model = TodoItem
		fields = ('description','priority')
		labels = {"description": "Описание", "priority": ""}

class TodoItemExportForm(forms.Form):
	prio_high = forms.BooleanField(label="Высокая важность", initial=True, required=False)
	prio_med = forms.BooleanField(label="Средней важности", initial=True, required=False)
	prio_low = forms.BooleanField(label="Низкой важности", initial=False, required=False) 


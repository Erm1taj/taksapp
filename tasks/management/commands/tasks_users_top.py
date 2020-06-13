from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import TodoItem
from collections import Counter

class Command(BaseCommand):
	help = u"Display not yet completed tasks' dates"

	def add_arguments(self, parser):
		parser.add_argument('--user', dest='user', type=str, default='test_user')

	def handle(self, *args, **options):
		s={}
		for u in User.objects.all():
			count_completed=0
			count_notcompleted=0
			for t in u.tasks.all():
				if t.is_completed==True:
					count_completed+=1
				if t.is_completed==False:
					count_notcompleted+=1
			s[str(u).replace("<User: ",'').replace(">",'')]=(count_completed,count_notcompleted)
		print("~~~Топ 25 пользоваетлей по количеству тасок~~~\n")
		for t in Counter(s).most_common(25):
			print("Пользователь: "+str(t[0])+" | Количество выполненных: "+str(t[1][0])+", невыполненных: "+str(t[1][1]))

from django.urls import path
from .views import poll_list, get_one, poll_agree, poll_disagree

urlpatterns =[
    path('poll', poll_list, name='poll_list'),
    path('poll/<int:id>', get_one, name='poll'),
    path('poll/<int:id>/agree', poll_agree, name='poll'),
    path('poll/<int:id>/disagree', poll_disagree, name='poll')
]
from django.urls import path
from .views import Create,List,Update
urlpatterns=[
    path('create/',Create.as_view()),
    path('all/',List.as_view()),
    path('update_status/<int:car_id>/',Update.as_view())
]
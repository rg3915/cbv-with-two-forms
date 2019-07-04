from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.Index.as_view(), name='index'),
    path('add/', v.BookCreate.as_view(), name='add'),
]

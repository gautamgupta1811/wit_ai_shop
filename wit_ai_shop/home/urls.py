from django.urls import path
from home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('mic',views.mic,name='mic'),
    # path(str(views.section_id())+'^', views.home, name='#deal-href')
]
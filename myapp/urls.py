from django.conf.urls import url
from myapp import views

app_name = 'myapp'

urlpatterns = [
   url(r'^school_list/',views.SchoolListView.as_view(),name='list'),
   url(r'^(?P<pk>[-\w]+)/$',views.SchoolDetailView.as_view(),name='details'),
]
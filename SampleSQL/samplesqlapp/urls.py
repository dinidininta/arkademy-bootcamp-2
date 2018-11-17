from django.conf.urls import url
import views
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    # url(r'^$', views.callback, name='callback'),
    # url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^$', views.index, name='index')
]

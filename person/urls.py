from django.urls import path
from . import views

urlpatterns = [
    path('', views.PersonList.as_view(), name='person-list'),
    path('<int:pk>', views.PersonDetail.as_view(), name='person-detail'),
    path('', views.PersonCreate.as_view(), name='person-create'),
    path('<int:pk>', views.PersonUpdate.as_view(), name='person-update'),
    path('<int:pk>', views.PersonDelete.as_view(), name='person-delete'),
]

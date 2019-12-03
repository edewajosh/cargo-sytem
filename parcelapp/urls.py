from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from parcelapp import views

urlpatterns = [
    path('branch/', views.BranchList.as_view()),
    path('branch/<int:pk>/', views.BranchDetail.as_view()),
    path('agent/', views.AgentList.as_view()),
    path('agent/<int:pk>', views.AgentDetail.as_view()),
    path('parcel/', views.ParcelList.as_view()),
    path('parcel/<int:pk>', views.ParcelDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)

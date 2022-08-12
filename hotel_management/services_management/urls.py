#--------Django Import--------#
from django.urls import path

#-------- Services Management View Import--------#
from .views import ComplainRegister

#-------- URL Pattern--------#
urlpatterns = [

    path('complain_register/',ComplainRegister.as_view(),name='complain-register'),

]
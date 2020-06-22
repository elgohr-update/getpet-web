from django.urls import path

from management import views

app_name = 'management'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),

    path('pets/', views.PetsListView.as_view(), name="pets_list"),
    path('pets/<int:pk>/', views.PetUpdateView.as_view(), name="pets_update"),
    path('pets/create/', views.PetCreateView.as_view(), name="pets_create"),

    path('shelters/', views.SheltersListView.as_view(), name="shelters_list"),
    path('shelters/<int:pk>/', views.ShelterInfoUpdateView.as_view(), name="shelters_update"),
    path('shelters/<int:pk>/switch/', views.ShelterSwitchView.as_view(), name="shelters_switch"),
    path('shelters/no-associated-shelter/', views.no_associated_shelter, name="shelters_no_associated_shelter"),

    path('instruction/', views.PlatformInstructionsDocumentView.as_view(), name="instruction"),
]

from django.urls import path
from .views.PaintingsViews import *
from .views.ExpertisesViews import *

urlpatterns = [
    path('api/paintings/', get_expertises),  # GET
    path('api/paintings/<int:p_id>/', get_painting_by_id),  # GET
    path('api/paintings/create/', create_painting),  # POST
    path('api/paintings/<int:p_id>/update/', update_painting),  # PUT
    path('api/paintings/<int:p_id>/delete/', delete_painting),  # DELETE
    path('api/paintings/<int:p_id>/add_to_request/', add_painting_to_expertise),  # POST

    path('api/expertises/', get_expertises),  # GET
    path('api/expertises/<int:e_id>/', get_expertise_by_id),  # GET
    path('api/expertises/<int:e_id>/update/', update_expertise),  # PUT
    path('api/expertises/<int:e_id>/update_status_user/', update_expertise_user),  # PUT
    path('api/expertises/<int:e_id>/update_status_admin/', update_expertise_admin),  # PUT
    path('api/expertises/<int:e_id>/delete/', delete_expertise),  # DELETE
    path('api/expertises/<int:e_id>/delete_painting/<int:p_id>/', delete_painting_from_expertise),  # DELETE
]
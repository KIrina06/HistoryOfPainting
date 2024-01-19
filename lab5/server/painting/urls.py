from django.urls import path
from painting.views.ExpertisesViews import *
from painting.views.RequestsViews import *
from painting.views.UsersViews import *

urlpatterns = [
    path('api/pictures/', get_expertises),  # GET
    path('api/pictures/<int:expertise_id>/', get_expertise_by_id),  # GET
    path('api/pictures/create/', create_expertise),  # POST
    path('api/pictures/<int:expertise_id>/update/', update_expertise),  # PUT
    path('api/pictures/<int:expertise_id>/delete/', delete_expertise),  # DELETE
    path('api/pictures/<int:expertise_id>/add_to_request/', add_expertise_to_request),  # POST

    
    path('api/expertises/', get_requests),  # GET
    path('api/expertises/<int:request_id>/', get_request_by_id),  # GET
    path('api/expertises/<int:request_id>/update/', update_request),  # PUT
    path('api/expertises/<int:request_id>/update_status_user/', update_request_user),  # PUT
    path('api/expertises/<int:request_id>/update_status_admin/', update_request_admin),  # PUT
    path('api/expertises/<int:request_id>/delete/', delete_request),  # DELETE
    path('api/expertises/<int:request_id>/delete_expertise/<int:expertise_id>/', delete_expertise_from_request),  # DELETE
    path('api/expertises/draft/', get_draft_request),

    
    path("api/register/", register, name="register"),
    path("api/login/", login, name="login"),
    path("api/check/", check, name="check_access_token"),
    path("api/logout/", logout, name="logout"),
]
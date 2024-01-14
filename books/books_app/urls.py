from django.urls import path
from .views import *

urlpatterns = [
    # Набор методов для услуг
    path('api/services/search/', search_services),  # GET
    path('api/services/<int:service_id>/', get_service_by_id),  # GET
    path('api/services/<int:service_id>/update/', update_service),  # PUT
    path('api/services/<int:service_id>/delete/', delete_service),  # DELETE
    path('api/services/create/', create_service),  # POST
    path('api/services/<int:service_id>/add_to_order/', add_service_to_order),  # POST
    path('api/services/<int:service_id>/image/', get_service_image),  # GET
    path('api/services/<int:service_id>/image/', update_service_image),  # PUT

    # Набор методов для заявок
    path('api/orders/', get_orders),  # GET
    path('api/orders/<int:order_id>/', get_order_by_id),  # GET
    path('api/orders/<int:order_id>/update/', update_order),  # PUT
    path('api/orders/<int:order_id>/update_status_user/', update_status_user),  # PUT
    path('api/orders/<int:order_id>/update_status_admin/', update_status_admin),  # PUT
    path('api/orders/<int:order_id>/delete/', delete_order),  # DELETE
    path('api/orders/<int:order_id>/delete_service/<int:service_id>/', delete_service_from_order),  # DELETE

    # Аутентификация
    path("api/register/", register, name="register"),
    path("api/login/", login, name="login"),
    path("api/check/", check, name="check_access_token"),
    path("api/logout/", logout, name="logout"),
]

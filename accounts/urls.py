from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views
from accounts.views import CustomerViews, StoreAdminViews

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),

    path('SignUp/', views.SignUpView.as_view(), name='signup'),



    path('Customer/Profile', CustomerViews.Customer_Profile_View, name='CustomerProfileView'),
    path('Customer/Edit/Profile', CustomerViews.Customer_Edit_Profile_View,
         name='Customer_Edit_Profile_View'),
    # path('Customer/FavoriteList', CustomerViews.get_FavoriteList,
    #      name='FavoriteList'),







    path('StoreAdmin/Profile', StoreAdminViews.StoreAdmin_Profile_View,
         name='StoreAdminProfileView'),
    path('StoreAdmin/Edit/Profile', StoreAdminViews.StoreAdmin_Edit_Profile_View,
         name='StoreAdminEditProfileView'),





]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''



    path('shopping_list', views.shoppinglist, name='Shopping list'),
    path('favorite', views.favorite, name='Favorite'),
    path('Offer', views.Offer, name='Offer'),
    path('reward', views.Reward, name='Reward'),
    path('ProvideReview', views.ProvideReview, name='Provide Review'),
    # Store Admin view
    path('ManageOffer', views.ManageOffer, name='Manage Offer'),
    path('ManagerProduct', views.ManagerProduct, name='Manager Product'),
#System Admin view
    path('ManageOffer', views.ManageOffer, name='Manage Advertisement'),
    path('Manage Reward', views.ManageReward, name='Manage Reward'),
    path('Manage Accounts', views.ManageAccounts, name='Manage Accounts'),

'''

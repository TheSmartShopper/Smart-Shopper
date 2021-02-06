from unittest import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from accounts.views import SignUpView, CustomerViews, StoreAdminViews


class TestUrls(TestCase):
    def testLoginView(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def testLogoutView(self):
        url = reverse('accounts:logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def testPasswordChangeView(self):
        url = reverse('accounts:password_change')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeView)

    def testPasswordChangeDoneView(self):
        url = reverse('accounts:password_change_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordChangeDoneView)

    def testPasswordResetView(self):
        url = reverse('accounts:password_reset')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetView)

    def testPasswordResetDoneView(self):
        url = reverse('accounts:password_reset_done')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetDoneView)

    def testPasswordResetConfirm(self):
        url = reverse('accounts:password_reset_confirm', args=[1, 2])
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetConfirmView)

    def testPasswordResetCompleteView(self):
        url = reverse('accounts:password_reset_complete')
        self.assertEqual(resolve(url).func.view_class, auth_views.PasswordResetCompleteView)

    def testSignupView(self):
        url = reverse('accounts:signup')
        self.assertEqual(resolve(url).func.view_class, SignUpView)

    def testCustomerProfileView(self):
        url = reverse('accounts:CustomerProfileView')
        self.assertEqual(resolve(url).func, CustomerViews.Customer_Profile_View)

    def testCustomerEditProfileView(self):
        url = reverse('accounts:Customer_Edit_Profile_View')
        self.assertEqual(resolve(url).func, CustomerViews.Customer_Edit_Profile_View)

    def testStoreAdminProfileView(self):
        url = reverse('accounts:StoreAdminProfileView')
        self.assertEqual(resolve(url).func, StoreAdminViews.StoreAdmin_Profile_View)

    def testStoreAdminEditProfileView(self):
        url = reverse('accounts:StoreAdminEditProfileView')
        self.assertEqual(resolve(url).func, StoreAdminViews.StoreAdmin_Edit_Profile_View)

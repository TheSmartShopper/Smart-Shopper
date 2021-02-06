from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView

from ManageStore.forms import ADForm
from accounts.forms import CustomerForm, StoreAdminEditForm, UserEditForm
from .CustomerProfilemodel import CustomerProfile
from .forms import SignupForm
from .models import StoreAdminProfile


class SignUpView(CreateView):
    template_name = 'signup.html'
    model = User
    form_class = SignupForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            if form.cleaned_data['typee'] == 'Customer':
                user = authenticate(username=username, password=password)
                Profile = CustomerProfile.objects.create(user=user)
                login(self.request, user)
                return redirect('accounts:CustomerProfileView')

            elif form.cleaned_data['typee'] == 'StoreAdmin':
                user = authenticate(username=username, password=password)
                Profile = StoreAdminProfile.objects.create(user=user)
                login(self.request, user)
                return redirect('accounts:StoreAdminProfileView')

            else:
                raise Http404

    def get(self, request, *args, **kwargs):
        form = SignupForm()

        return render(request, self.template_name, {'form': form})


class CustomerViews():

    def Customer_Profile_View(request):
        user = get_object_or_404(CustomerProfile, user=request.user)
        favorites = user.favorite.all()

        return render(request, 'CustomerProfile.html', {'Profile': user, 'favorites': favorites})

    def Customer_Edit_Profile_View(request):
        user = get_object_or_404(CustomerProfile, user=request.user)
        if request.method == 'POST':
            user_form = UserEditForm(request.POST or None, request.FILES or None, instance=user)
            form = CustomerForm(request.POST or None, request.FILES or None, instance=user)
            if form.is_valid():
                edit = form.save(commit=False)
                edit.save()
            return redirect('accounts:CustomerProfileView')
        else:
            user_form = UserEditForm(instance=user)
            form = CustomerForm(instance=user)
        return render(request, 'CustomerEditInfo.html', {'form': form, 'user_form': user_form})



class StoreAdminViews():
    def StoreAdmin_Profile_View(request):
        user = get_object_or_404(StoreAdminProfile, user=request.user)
        form = ADForm()
        return render(request, 'StoreAdminProfile.html', {'Profile': user , 'form':form})

    def StoreAdmin_Edit_Profile_View(request):
        user = get_object_or_404(StoreAdminProfile, user=request.user)

        if request.method == 'POST':
            user_form = UserEditForm(request.POST or None, request.FILES or None, instance=request.user)
            form = StoreAdminEditForm(request.POST or None, request.FILES or None, instance=user)
            if form.is_valid() and user_form.is_valid():
                user_form.save()
                form.save()
            return redirect('accounts:StoreAdminProfileView')
        else:
            user_form = UserEditForm(instance=request.user)
            form = StoreAdminEditForm(instance=user)
        return render(request, 'StoreAdminEditInfo.html', {'form': form, 'user_form': user_form})

from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Shopping_Cart/', include('ShoppingCart.urls', namespace='ShoppingCart')),
    path('', include('Dashboard.urls', namespace='Dashboard')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ManageProduct/', include('ManageProduct.urls', namespace='ManageProduct')),
    path('ManageStore/', include('ManageStore.urls', namespace='ManageStore')),
    path('ManageOffer/', include('ManageOffer.urls', namespace='ManageOffer')),
    path('ManageReview/', include('ManageReview.urls', namespace='ManageReview')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'Dashboard.views.error_404'

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Eshop.views import (
    videogame_profile, company_profile, home, signuppage, loginpage, logoutPage, profile,
    videogamepage, companypage, digitalcodepage, orderpage, payment_add, mypayments
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signuppage, name="signup"),
    path('login/', loginpage, name="login"),
    path('home/', home, name='home'),
    path('logout/', logoutPage, name='logout'),
    path('profile/', profile, name='profile'),
    path('videogame/<int:videogame_id>/', videogame_profile, name='videogame_profile'),
    path('company/<int:company_id>/', company_profile, name='company_profile'),
    path('videogames/', videogamepage, name='videogamepage'),
    path('companies/', companypage, name='companypage'),
    path('digitalcodes/', digitalcodepage, name='digitalcodepage'),
    path('orders/', orderpage, name='orderpage'),
    path('payment/add/', payment_add, name='payment_add'),
    path('payments/', mypayments, name='mypayments'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

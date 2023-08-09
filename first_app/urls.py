from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('signup/',views.signup, name="signup"),
    path('profile/',views.profile, name="profile"),
    path('login/',views.userlogin, name="login"),
    path('logout/',views.userlogout, name="logout"),
    path('passchange/',views.passchange, name="passchange"),
    path('passchangewithoutold/',views.passchangewithoutold, name="passchangewithoutold")
]

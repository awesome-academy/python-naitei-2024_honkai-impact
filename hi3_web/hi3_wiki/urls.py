from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('introduction/', views.introduction, name='Introduction'),
    path('overall-guide/', views.overall_guide, name='Overall'),
    path('team-build/', views.team_build, name='Team Buildings'),

    path('valkyries/', views.valkyrie, name='Valkyrie'),
    path('weapons/', views.weapon, name='Weapons'),
    path('stigmatas/', views.stigmata, name='Stigmatas'),

    path('elyrealm/', views.elyrealm, name='Elysian Realm'),
    path('abyss/', views.abyss, name='Abyss'),
    path('ma/', views.ma, name='Memorial Arena'),

    path('valkyrie/details/<int:id>', views.details, name='details'),
    path('valkyrie/<str:valkyrie_name>/<str:battlesuit_name>/', views.battlesuit_detail, name='battlesuit_detail'),

    path('test-static/', views.test_static, name='test_static'),
]


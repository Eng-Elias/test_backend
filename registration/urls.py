from django.urls import path
from .views import (
    UserSignupView, UserLoginView,
    FamilyListCreateView, FamilyDetailView,
    MemberListCreateView, MemberDetailView,
    ChurchListCreateView, ChurchDetailView,
    EmirateListCreateView, EmirateDetailView,
    SubAreaListCreateView, SubAreaDetailView,
    FatherConfListCreateView, FatherConfDetailView,
    ProfessionCategoryListCreateView, ProfessionCategoryDetailView
)

urlpatterns = [
    # Auth
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),

    # Family
    path('families/', FamilyListCreateView.as_view(), name='family-list-create'),
    path('families/<int:pk>/', FamilyDetailView.as_view(), name='family-detail'),

    # Member
    path('members/', MemberListCreateView.as_view(), name='member-list-create'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),

    # Church
    path('churches/', ChurchListCreateView.as_view(), name='church-list-create'),
    path('churches/<int:pk>/', ChurchDetailView.as_view(), name='church-detail'),

    # Emirate
    path('emirates/', EmirateListCreateView.as_view(), name='emirate-list-create'),
    path('emirates/<int:pk>/', EmirateDetailView.as_view(), name='emirate-detail'),

    # SubArea
    path('subareas/', SubAreaListCreateView.as_view(), name='subarea-list-create'),
    path('subareas/<int:pk>/', SubAreaDetailView.as_view(), name='subarea-detail'),

    # FatherConf
    path('fatherconfs/', FatherConfListCreateView.as_view(), name='fatherconf-list-create'),
    path('fatherconfs/<int:pk>/', FatherConfDetailView.as_view(), name='fatherconf-detail'),

    # ProfessionCategory
    path('professioncategories/', ProfessionCategoryListCreateView.as_view(), name='professioncategory-list-create'),
    path('professioncategories/<int:pk>/', ProfessionCategoryDetailView.as_view(), name='professioncategory-detail'),
]

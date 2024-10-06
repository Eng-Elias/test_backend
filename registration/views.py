from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import User, Family, Member, Church, Emirate, SubArea, FatherConf, ProfessionCategory
from .serializers import UserSerializer, FamilySerializer, MemberSerializer, ChurchSerializer, EmirateSerializer, SubAreaSerializer, FatherConfSerializer, ProfessionCategorySerializer


# User Signup (Register)
class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# User Login (Obtain Auth Token)
class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(UserLoginView, self).post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=response.data['user_id'])
        return Response({
            'token': token.key,
            'user_id': response.data['user_id'],
        })


# Family CRUD Views
class FamilyListCreateView(generics.ListCreateAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]


class FamilyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer
    permission_classes = [permissions.IsAuthenticated]


# Member CRUD Views
class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class MemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [permissions.IsAuthenticated]


# Lookups CRUD Views
class ChurchListCreateView(generics.ListCreateAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChurchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmirateListCreateView(generics.ListCreateAPIView):
    queryset = Emirate.objects.all()
    serializer_class = EmirateSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmirateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emirate.objects.all()
    serializer_class = EmirateSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubAreaListCreateView(generics.ListCreateAPIView):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubAreaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer
    permission_classes = [permissions.IsAuthenticated]


class FatherConfListCreateView(generics.ListCreateAPIView):
    queryset = FatherConf.objects.all()
    serializer_class = FatherConfSerializer
    permission_classes = [permissions.IsAuthenticated]


class FatherConfDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FatherConf.objects.all()
    serializer_class = FatherConfSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfessionCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProfessionCategory.objects.all()
    serializer_class = ProfessionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfessionCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfessionCategory.objects.all()
    serializer_class = ProfessionCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

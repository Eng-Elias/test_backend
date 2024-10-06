from django.contrib import admin

from registration.models import User, Church, Emirate, MainArea, SubArea, Family, FatherConf, ProfessionCategory, Member


# Register your models here.
admin.site.register(User)
admin.site.register(Church)
admin.site.register(Emirate)
admin.site.register(MainArea)
admin.site.register(SubArea)
admin.site.register(Family)
admin.site.register(FatherConf)
admin.site.register(ProfessionCategory)
admin.site.register(Member)

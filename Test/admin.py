# from Test.models import userProfile
from Test.models import User
from django.contrib import admin

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password']
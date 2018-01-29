from django.contrib import admin
from  .models import UserProfile
from  .models import UserInfo

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone')
    list_filter = ("phone",)
admin.site.register(UserProfile,UserProfileAdmin)

class UserInfoAdim(admin.ModelAdmin):
    list_display = ("user",'school','profession','address','aboutme','photo')
    list_filter = ("school","company","profession")
admin.site.register(UserInfo,UserInfoAdim)



# Register your models here.

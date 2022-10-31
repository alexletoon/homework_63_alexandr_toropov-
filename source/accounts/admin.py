from django.contrib import admin
from accounts.models import Account
from posts.models import Post

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'avatar')
    list_filter =  ('id', 'email', 'username', 'avatar')
    search_field = ('id', 'status')
    fields =  ('email', 'username', 'avatar')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'image')
    list_filter =  ('id', 'author', 'image')
    search_field = ('id', 'author')
    fields =  ('author', 'description','image')

admin.site.register(Account, AccountAdmin)
admin.site.register(Post, PostAdmin)
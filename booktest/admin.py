from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['btitle', 'bpub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['hname', 'hgender']
    list_per_page = 10
    list_display_links = ['hname', 'hgender']
    # list_editable = ['hname', 'hgender']


admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(BookInfo, BookInfoAdmin)

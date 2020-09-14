from django.contrib import admin
from .models import House, OrderBrick


class OrderBrickInline(admin.TabularInline):
    model = OrderBrick
    raw_id_fields = ['house']


class HouseAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'address',
                    'release_date',
                    ]

    inlines = [OrderBrickInline]


admin.site.register(House, HouseAdmin)


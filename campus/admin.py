from django.contrib import admin

from campus.models import Student


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "email",
        "phone",
        "address",
        "created_at",
        "updated_at",
    )
    search_fields = (
        "name",
        "age",
        "email",
        "phone",
        "address",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "name",
        "age",
        "email",
        "phone",
        "address",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Student, StudentAdmin)

from django.contrib import admin

from issue_tracker.models import Task, Status, Type, Project


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'summary',
        'created_at',
        'updated_at',
        'is_deleted',
        'deleted_at'
    )
    list_editable = ('summary', 'is_deleted')


admin.site.register(Task, TaskAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


admin.site.register(Type, TypeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ['name']


admin.site.register(Project, ProjectAdmin)

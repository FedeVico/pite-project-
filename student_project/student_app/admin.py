from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staffs, Courses, Subjects, Students, NotificationStudent, NotificationStaffs, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaffs 
from import_export.admin import ImportExportMixin
from .models import Task

class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['id_number', 'name', 'surname','second_surname', 'registration_num', 'email', 'movil', 'provincia', 'score', 'credits', 'year']


admin.site.register(Task, TaskAdmin)

# Register your models here.
class UserModel(UserAdmin):
    pass
 
 
admin.site.register(CustomUser, UserModel)
 
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Students)
'''admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)'''
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
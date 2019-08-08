from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.register(Staff, UserAdmin)


@admin.register(Product)
class PRODUCT_INFO_admin(admin.ModelAdmin):
    list_display = ('sid', 'status', 'MKT_CHNL_NAME', 'MKT_GRID_NAME', 'receive_org', 'PRODUCT_NAME',
                    'main_set', 'add_set', 'CRM', 'product_quality', 'client', 'staff')
    search_fields = ('sid', 'status', 'receive_org')
    list_per_page = 10
    actions_on_top = True


@admin.register(Client)
class CLIENT_INFO_admin(admin.ModelAdmin):
    list_display = ('cid', 'client_name', 'user_name', 'standard_address', 'client_address')
    search_fields = ('cid', 'client_name', 'user_name')
    list_per_page = 10
    actions_on_top = True


@admin.register(Staff)
class STAFF_INFO_admin(admin.ModelAdmin):
    list_display = ('staff_id', 'department', 'position', 'username')
    search_fields = ('staff_id', 'department', 'position', 'username')
    list_per_page = 10
    actions_on_top = True


@admin.register(Contract)
class CONTRACT_INFO_admin(admin.ModelAdmin):
    list_display = ('contract_amount', 'contract_id', 'contract_date', 'contract_expire',
                    'allowance', 'product')
    search_fields = ('contract_id', 'contract_date', 'contract_expire', 'product')
    list_per_page = 10
    actions_on_top = True


@admin.register(Resource)
class RESOURCE_INFO_admin(admin.ModelAdmin):
    list_display = ('bandwidth', 'true_bandwidth', 'net_management', 'product')
    search_fields = ('bandwidth', 'true_bandwidth', 'net_management', 'product')
    list_per_page = 10
    actions_on_top = True

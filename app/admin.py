from django.contrib import admin

# Register your models here.
from app.models.Category import Category
from app.models.CategoryDataField import CategoryDataField
from app.models.DataField import DataField
from app.models.DataFieldValue import DataFieldValue
from app.models.Product import Product
from app.models.CustomUser import CustomUser
from django import forms
from django.contrib.auth.admin import UserAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name',)


@admin.register(DataField)
class DataFieldAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DataFieldValue)
class DataFieldValueAdmin(admin.ModelAdmin):
    list_display = ('datafield', 'product', 'value',)


@admin.register(CategoryDataField)
class CategoryDataFieldAdmin(admin.ModelAdmin):
    list_display = ('datafield', 'category',)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'role_users', 'username', 'phone_number', 'is_superuser')

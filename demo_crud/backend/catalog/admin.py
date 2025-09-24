from django.contrib import admin
from .models import Product, ExchangeRate

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'sales_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'description', 'price', 'stock')
        }),
        ('Sales Data', {
            'fields': ('sales_count',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['base', 'target', 'rate', 'fetched_at']
    list_filter = ['base', 'target', 'fetched_at']
    search_fields = ['base', 'target']
    readonly_fields = ['fetched_at']
    
    fieldsets = (
        ('Currency Information', {
            'fields': ('base', 'target', 'rate')
        }),
        ('Timestamps', {
            'fields': ('fetched_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # If editing existing object
            return self.readonly_fields + ('base', 'target')
        return self.readonly_fields
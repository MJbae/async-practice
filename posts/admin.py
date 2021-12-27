from django.contrib import admin
from .models import *

admin.site.register(Owner)
admin.site.register(Customer)
admin.site.register(Currency)
admin.site.register(Transaction)

from django.contrib import admin
from .models import student,product,teacher,StudentProfile1,services,Category,user,passport,Seller,product_auction,buyer,bid

admin.site.register(student)
admin.site.register(product)
admin.site.register(teacher)
admin.site.register(StudentProfile1)
admin.site.register(Seller)
admin.site.register(product_auction)
admin.site.register(services)
admin.site.register(Category)
admin.site.register(user)
admin.site.register(passport)
admin.site.register(buyer)
admin.site.register(bid)


from django.contrib import admin
from.models import User,seller,Buyer,Admin,category,Items,Auction,Bid,Payment,WatchList,Notification,Review,Dispute,ActivityLog
# Register your models here.
admin.site.register(User)
admin.site.register(seller)
admin.site.register(Buyer)
admin.site.register(Admin)
admin.site.register(category)
admin.site.register(Items)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Payment)
admin.site.register(WatchList)
admin.site.register(Notification)
admin.site.register(Review)
admin.site.register(Dispute)
admin.site.register(ActivityLog)
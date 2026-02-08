from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    
    UserName = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=15)
    Address  = models.TextField()
    RegistrationDate = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)


    class Meta:
        db_table = "User"

    def __str__(self):
        return self.UserName
    


class seller(models.Model):
    Name = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    SellerRating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00)
    TotalItemsSold = models.IntegerField(default = 0) 

    class Meta:
        db_table = "seller"  

    def __str__(self):
        return self.Name.UserName 


class Buyer(models.Model):
    Name = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    BuyerRating = models.DecimalField(max_digits=3,decimal_places=2,default=0.00) 

    class Meta:
        db_table = "Buyer"

    def __str__ (self):
        return self.Name.UserName        



class Admin(models.Model):
    ROLE_CHOICES = [
        ('SUPER', 'Super Admin'),
        ('MOD', 'Moderator'),
        ('SUB', 'Sub Admin'),
    ]
    Name = models.OneToOneField(User, on_delete=models.CASCADE,null = True)
    Role = models.CharField(max_length=50,choices=ROLE_CHOICES,default="MOD")

    class Meta:
        db_table = "Admin"

    def __str__(self):
        return f"{self.Name.UserName} ({self.Role})"
   


class category(models.Model):
    
    CategoryName = models.CharField(max_length=100)
    Description = models.TextField()  

    class Meta:
        db_table = "category"

    def __str__ (self):
        return self. CategoryName
    

class Items(models.Model):
        CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('REFURB', 'Refurbished'),
    ]
        category = models.ForeignKey(category,on_delete=models.CASCADE,related_name='items')
        name = models.CharField(max_length=200)
        description = models.TextField()
        condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
        shipping_cost = models.DecimalField(max_digits=10, decimal_places=2) 

        class Meta:
            db_table = "Items"

        def __str__(self):
            return self.name  


class Auction(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('ENDED', 'Ended'),
        ('CANCELLED', 'Cancelled'),
    ]
    Title = models.CharField(max_length=200)
    Description = models.TextField()  
    Starting_Price = models.DecimalField(max_digits=10,decimal_places=2)
    Reserve_Price = models.DecimalField(max_digits=10,decimal_places=2)

    Start_time = models.DateTimeField()
    End_time = models.DateTimeField()

    Status = models.CharField(max_length=20,choices=STATUS_CHOICES)

    CategoryId = models.ForeignKey(category,on_delete=models.CASCADE)
    SellerId = models.ForeignKey(seller,on_delete=models.CASCADE)
    ItemId = models.ForeignKey(Items,on_delete=models.CASCADE)
    winner = models.ForeignKey(Buyer,on_delete=models.SET_NULL,null=True,blank=True)
    current_price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    class Meta:
        db_table = "Auction"
    
    def __str__(self):
        return self.Title
    

class Bid(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('OUTBID', 'Outbid'),
        ('WINNING', 'Winning'),
        ('LOST', 'Lost'),
    ]
    BidAmount = models.DecimalField(max_digits=10,decimal_places=2) 
    BidTime = models.DateTimeField()
    Status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    AuctionId = models.ForeignKey(Auction,on_delete=models.CASCADE,related_name='bids')
    BuyerId = models.ForeignKey(Buyer,on_delete=models.CASCADE,related_name='bids')

    class Meta:
        db_table = "Bid"

    def __str__(self):
        return f"Bid {self.id} - {self.BidAmount}" 


class Payment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded'),
    ]

    METHOD_CHOICES = [
        ('CARD', 'Credit Card'),
        ('PAYPAL', 'PayPal'),
        ('UPI', 'UPI'),
        ('NETBANK', 'Net Banking'),
    ]

    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50,choices=METHOD_CHOICES)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='PENDING')

    auction = models.ForeignKey(Auction,on_delete=models.CASCADE,related_name='payments')
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE,related_name='payments')

    class Meta:
        db_table = "Payment"

    def __str__(self):
        return f"Payment {self.id} - {self.amount}"


class WatchList(models.Model):
    AddedDate = models.DateTimeField()       
    BuyerId = models.ForeignKey(Buyer,on_delete=models.CASCADE,related_name='watchlists')
    AuctionId = models.ForeignKey(Auction,on_delete=models.CASCADE,related_name='watchlists')

    class Meta:
        db_table = "WatchList"

    def __str__(self):
        return f"{self.BuyerId} → {self.AuctionId}"
    

class Notification(models.Model):

    NOTIFICATION_TYPE_CHOICES = [
        ('BID_PLACED', 'Bid Placed'),
        ('OUTBID', 'Outbid'),
        ('AUCTION_ENDED', 'Auction Ended'),
        ('PAYMENT', 'Payment'),
        ('GENERAL', 'General'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=50,
        choices=NOTIFICATION_TYPE_CHOICES,
        default='GENERAL'
    )

    auction = models.ForeignKey(
        'Auction',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    bid = models.ForeignKey(
        'Bid',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Notification for {self.user.UserName}"



class Review(models.Model):
    Rating = models.IntegerField()
    Comment = models.TextField()
    ReviewDate = models.DateTimeField()
    ReviewerId = models.ForeignKey(User,on_delete=models.CASCADE, related_name="reviews_given")
    RevieweeId = models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews_received",null = True)
    AuctionId = models.ForeignKey(Auction,on_delete=models.CASCADE)

    class Meta:
        db_table = "Review"

    def __str__(self):
        return f"Review by {self.ReviewerId.UserName}"
    


class Dispute(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    raised_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reason = models.TextField()
    status = models.CharField(max_length=20, default="OPEN")

    class Meta:
        db_table = "Dispute"

    def __str__(self):    
        return f"Dispute on Auction {self.auction.id} by {self.raised_by.UserName} ({self.status})"




class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "ActivityLog"

    def __str__(self):
        return f"{self.user.UserName} - {self.action}"
    


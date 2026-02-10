from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField(null=True)


    class Meta:
        db_table  = "student"
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name    


class product(models.Model):
    name  = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    stock = models.IntegerField()
    color = models.CharField(null =True, max_length=50) 
    status = models.CharField(default = True)


    class Meta:
        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products" 



class teacher(models.Model):
    Name = models.CharField(max_length= 200)        
    Age = models.IntegerField()
    Subject = models.CharField(max_length=50) 
    salary = models.PositiveBigIntegerField(null = True)
    Email = models.EmailField(null = True) 


    class Meta:
        db_table = "Teacher"
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"      

# one to one relationship
class StudentProfile1(models.Model):
    hobbies = (
        ("Reading","Reading"),
        ("Sports","Sports"),
        ("Music","Music"),
        ("Traveling","Traveling"),
        ("Cooking","Cooking"),
        ("Gaming","Gaming"),
        ("Art","Art"),
        ("Dancing","Dancing"),
        ("Photography","Photography"),
        ("Writing","Writing"),
    )

    StudentId = models.OneToOneField(student, on_delete=models.CASCADE)
    Hobbies = models.CharField(max_length=200, choices=hobbies)
    Address = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=15)
    Gender = models.CharField(max_length=10)
    DOB = models.DateField()

    class Meta:
        db_table = "StudentProfile1"
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles" 

    def __str__(self):
        return self.StudentId.name
    

    # many to many relationship

class Category(models.Model):    
    Name = models.CharField(max_length=100)
    description  = models.CharField(max_length=200)
    status = models.BooleanField(default=True)


    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories" 

    def __str__(self):
        return self.Name    


class services(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    Categoryid = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = "services"
        verbose_name = "Service"
        verbose_name_plural = "Services" 
    
    def __str__(self):
        return self.name
    


    # task 
# one to one relationship between user and passport
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users" 

    def __str__(self):
        return self.name    



class passport(models.Model):
    passport_number = models.CharField(max_length=20)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    user_id = models.OneToOneField(user, on_delete=models.CASCADE)

    class Meta:
        db_table = "passport"
        verbose_name = "Passport"
        verbose_name_plural = "Passport" 


    def __str__(self):
        return self.user_id.name  



# task 2 
# one to many relationship between seller and product

class Seller(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=15)
    Address = models.CharField(max_length=200)


    class Meta:
        db_table = "Seller"
        verbose_name = "Seller"
        verbose_name_plural = "Seller" 

    def __str__(self):
        return self.Name     
    


class product_auction(models.Model):
    name  = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    stock = models.IntegerField()
    color = models.CharField(null =True, max_length=50) 
    status = models.CharField(default = True)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)

    class Meta:
        db_table = "product_auction"
        verbose_name = "Product Auction"
        verbose_name_plural = "Product Auction" 

    def __str__(self):
        return self.seller_id.Name


class buyer(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=15)
    Address = models.CharField(max_length=200)


    class Meta:
        db_table = "buyer"
        verbose_name = "Buyer"
        verbose_name_plural = "Buyer"

    def __str__(self):
        return self.Name

class bid(models.Model): 
    product_id = models.ForeignKey(product_auction, on_delete=models.CASCADE,null=True)
    buyer_id = models.ForeignKey(buyer, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()
    bid_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bid"
        verbose_name = "Bid"
        verbose_name_plural = "Bid"

    def __str__(self):
        return self.buyer_id.Name           
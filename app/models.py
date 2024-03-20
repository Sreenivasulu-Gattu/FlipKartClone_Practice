from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    email = models.EmailField(primary_key = True)
    mobile = models.PositiveBigIntegerField(unique = True)
    dis_pic = models.ImageField()
    address = models.TextField()
    address_pin = models.PositiveSmallIntegerField()

    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),('O', 'Other'))
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    pan_id = models.CharField(max_length = 100,unique = True)
    pan_pic = models.ImageField()

    def __str__(self):
        return self.username
    
class ProductCat(models.Model):
    pro_cat_name = models.CharField(max_length = 100,primary_key = 100)

    def __str__(self):
        return self.pro_cat_name

class ProductBrand(models.Model):
    pro_cat_name = models.ForeignKey(ProductCat,on_delete = models.CASCADE)
    pro_brand_name = models.CharField(max_length = 100,unique = True)

class Product(models.Model):
    pro_brand_name = models.ForeignKey(ProductBrand,on_delete = models.CASCADE)
    pro_name = models.CharField(max_length = 100)
    pro_img = models.ImageField()
    pro_price = models.DecimalField(max_digits=10, decimal_places=2)
    pro_rating = models.DecimalField(max_digits=3, decimal_places=1)
    pro_dis = models.DecimalField(max_digits=5, decimal_places=2)
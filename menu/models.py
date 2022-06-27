from django.db import models
from django.utils.translation import gettext_lazy as _T

# Create your models here.


class Menu(models.Model):
    class TypeChoices(models.IntegerChoices):
        WEIGHT = 1, _T("体重")
        CALORIE = 2, _T("卡路里")

    class PetTypeChoices(models.IntegerChoices):
        CAT = 1, _T("猫")
        DOG = 2, _T("狗")
    name = models.CharField(max_length=32)
    pet_type = models.IntegerField(db_index=True, choices=PetTypeChoices.choices, default=PetTypeChoices.CAT)
    mtype = models.IntegerField(db_index=True, choices=TypeChoices.choices, default=TypeChoices.WEIGHT)


class Food(models.Model):
    class TypeChoices(models.IntegerChoices):
        DEFAULT = 0, _T("默认")
        BONE = 1, _T("骨骼")
        LIVER = 2, _T("肝脏")
        OTHER_VISCUS = 3, _T("其他内脏（分泌功能）")
        POULTRY = 4, _T("禽肉")
        RED_MEAT = 5, _T("红肉")
        FISH = 6, _T("鱼")
        LIVER_MUSCLE = 7, _T("内脏（肌肉组织）")
        SHELLFISH = 8, _T("贝类")
        VEGETABLES = 9, _T("蔬菜")
        FRUITS = 10, _T("水果")
        CARBOHYDRATES = 11, _T("碳水化物")
    name = models.CharField(max_length=32)
    ftype = models.IntegerField(db_index=True, choices=TypeChoices.choices, default=TypeChoices.DEFAULT)
    delete_flat = models.BooleanField(default=False, db_index=True)


class MenuFoodRef(models.Model):
    menu_id = models.IntegerField(db_index=True)
    food_id = models.IntegerField(db_index=True)
    percentage = models.IntegerField(db_index=True)


class TraceElement(models.Model):
    class TypeChoices(models.IntegerChoices):
        DEFAULT = 0, _T("默认")
        CALCIUM = 1, _T("钙质")
        VITAMIN = 2, _T("维生素")
        IODINE = 3, _T("碘")
        POTASSIUM = 4, _T("钾")
        TAURINE = 5, _T("牛磺酸")
        FISH_OIL = 6, _T("鱼油")
    name = models.CharField(max_length=32)
    mtype = models.IntegerField(db_index=True, choices=TypeChoices.choices, default=TypeChoices.DEFAULT)
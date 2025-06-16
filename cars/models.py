from django.db import models

class Equipment(models.Model):
    equipment = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.equipment

class Car(models.Model):
    ENGINE_TYPES = [
        ("bezyna", "Bęzynowy"),
        ("diesel", "Diesel"),
        ("elektryk", "Elektryczny"),
        ("hybryda", "Hybrydowy")
    ]
    GEARBOX_TYPES = [
        ("manual", "manualna"),
        ("automat", "automatyczna")
    ]
    BODY_TYPES = [
        ("hatchback", "hatchback"),
        ("sedan", "sedan"),
        ("combi", "combi"),
        ("suv", "SUV"),
    ]
    CAR_CLASSES = [
        ("a", "małe i mini"),
        ("b", "miejskie"),
        ("c", "kompaktowe"),
        ("d", "rodzinne"),
        ("e", "limuzyny"),
        ("f", "luksusowe"),
        ("g", "sportowe"),
        ("h", "kabriolety"),
        ("i", "terenowe"),
        ("m", "van"),
    ]
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=50, choices=ENGINE_TYPES)
    gearbox_type = models.CharField(max_length=50, choices=GEARBOX_TYPES)
    engine_power = models.PositiveSmallIntegerField()
    engine_capacity = models.PositiveSmallIntegerField()
    seats_count = models.PositiveSmallIntegerField()
    dors_count = models.PositiveSmallIntegerField()
    trunk_capacity = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50, choices=BODY_TYPES)
    category = models.CharField(max_length=50, choices=CAR_CLASSES)
    fuel_usage = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage_limit = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    availability = models.BooleanField()
    insurance_expiry_date = models.DateField()
    equipment = models.ManyToManyField(Equipment)
    image = models.ImageField(upload_to="images")

    def __str__(self) -> str:
        return self.brand + " " + self.model
    
    @staticmethod
    def get_car_category(category):
        return dict(Car.CAR_CLASSES)[category]
    
    @staticmethod
    def get_all_categories():
        return dict(Car.CAR_CLASSES)


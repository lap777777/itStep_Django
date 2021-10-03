from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Branch(models.Model):
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=200, null=True)
    origin = models.DateField()
    email = models.EmailField(max_length=30)
    employees_no = models.IntegerField()
    def __str__(self):
        return self.city

class Meta:
    verbose_name_plural = "Branches"

class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    birth = models.DateField()
    def __str__(self):
        return f"{self.name} {self.surname}, email: {self.email}" 
    active = models.BooleanField(default=False)


class Course(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()  
    end = models.DateTimeField()
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    # ForeignKey odkaz na jiny model
    # on_delete - parametr, ktery rika, co se stane, kdyz ho smazu
    # SET_NULL - kdyz kategorii smazu, tak pole nastaveno na prazdne
    # null=True / uz mam v databazi kurzy, pole category je povinne, tak to osetruji, aby mi to nedelalo problem u kurzu, ktere uz mam v databazi a je tam policko kategorie prazdne
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    lecturer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="course_lecturer")
    event_coordinator = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="course_coordinator")
    def __str__(self):
        return self.name

class Application(models.Model):
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    phone_number = models.TextField(max_length=15, blank=True, null=True)

class Registration(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    birth = models.DateField()
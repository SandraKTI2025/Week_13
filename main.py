from animal import Animal, Cat, Dog

my_cat = Cat("Nora")
my_dog = Dog("Loore")
neighbours_dog = Dog("Mia")

my_dog.dog_sees(neighbours_dog)
my_dog.dog_sees(my_cat)

my_cat.cat_sees(my_dog)

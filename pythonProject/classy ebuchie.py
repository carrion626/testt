class Pers():
    def __init__(self, race, damage = 10, armor = 20):
        self.race = race
        self.damage = damage
        self.armor = armor

t = Pers('elf', 20, 40)
print(t.damage)
print(t.race)
print(t.armor)

##############################################
class Pers():
    MAX_SPEED = 100
    DEAD_HEALTH = 0 #кароч константы пишутся капсом, чтоб другие додиксы их не меняли, такое соглашение типа

    def __init__(self, race, damage = 10, armor = 20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == Pers.DEAD_HEALTH


t = Pers('elf', 20, 40)
print(t.damage)
print(t.race)
print(t.armor)

t.hit(20)
print(t.health)
print(t.is_dead())

#еще приколямба, защищенные атрибуты пишем с _впереди, а приватные с __впереди
#нахуя? вот так договорились просто, щас будет пример

class Pers():
    def __init__(self, race, damage = 10, armor = 20):
        self.__race = race
        self.damage = damage
        self.armor = armor
        self._health = 100

# a теперь ВНИМАНИЕ! если атрибут приватный или защищенный, чтобы его можно было читать, его нужно прописать через @property
    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

t = Pers('elf', 20, 40)
print(t.damage)
print(t._Pers__race) #вот эта залупань, типа ты уже не можешь напрямую вызывать расу если она приватная, и менять точно так же нужно
t._Pers_health = 10 #вот тут уже защищенный хелз, его по-другому вызывать и менять:
print(t._Pers_health)
print(t.armor)

print(t.health)
print(t.race)

############################################
#teper' static i class metod

class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def disp(self):
        return f"{self.day}-{self.month}-{self.year}"

    @classmethod
    def mill_c(cls, day, month):
        return cls(day, month, 2002)

    @staticmethod
    def mill_s(day, month):
        return Date(day, month, 2002)

d1 = Date.mill_c(20, 2)
d2 = Date.mill_s(20, 2)
print(d1.disp())
print(d2.disp())

#vot oni, vyvodyat odnu i tu ze huinyu, no v chem prikol:
class DateTime(Date):
    def display(self):
        return f"{self.day}-{self.month}-{self.year} - 00:00:00PM"

dt1 = DateTime

#taaaaaaaaaaaaaak, poshlo ono nahui
#NASLEDOVANIE I POLIMORFIZM

class Shape():

    def __init__(self):
        print('Shape created')

    def draw(self):
        print('Drawing a Shape')

    def area(self):
        print('calc area')

    def perimeter(self):
        print('calc perimeter')

shape = Shape()
class Rectangle(Shape):

    def __init__(self, width, height):
        Shape.__init__(self)

        self.width = width
        self.height = height

        print('rectangle created')

        Shape.area(self)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

rect = Rectangle(10,15)
print(rect.area())
#eto bilo nasledovanie


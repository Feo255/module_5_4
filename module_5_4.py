class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        return super().__new__(cls)

    def __init__ (self, name, number_of_floors):
        new_floor = 0

        self.name = name
        self.number_of_floors =number_of_floors

    def __len__(self):

        return (self.number_of_floors)

    def __str__(self):
        str1 = None
        str2 = None
        str_summ = None
        str1 = 'Название: ' + str(self.name)
        str2 = ', кол-во этажей: ' + str(self.number_of_floors)
        str_summ = str1 + str2

        return (str_summ)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
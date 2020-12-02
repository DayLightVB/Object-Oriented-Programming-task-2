class FirstClass(object):
    engine = 'V8'


# 2.Stwórz klasę, która dziedzicząc przysłania pola
class SecondClass(FirstClass):
    engine = 'V10'
    original_engine = FirstClass.engine


class ThirdClass:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine


class FourthClass(ThirdClass):
    # 3.W klasie stwórz konstruktor, który wywołuje inny konstruktor z tej samej klasy.
    def __init__(self, name, model, engine):
        super().__init__(name, model, engine)

    def check(self):
        print('FourthClass:', self.name, self.model, self.engine)


print(FirstClass().engine)
print(SecondClass().engine)
print(SecondClass().original_engine)
x = FourthClass('Mercedes', 'AMG F1 W10 EQ Power+', '1,6 V6T')
x.check()

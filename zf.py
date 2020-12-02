class Engine:
    def __init__(self, engine_name, engine_model, engine_power, engine_fuel):
        self.engine_name = engine_name
        self.engine_model = engine_model
        self.engine_power = engine_power
        self.engine_fuel = engine_fuel

    def check(self):
        return self.engine_name, self.engine_model, self.engine_power, self.engine_fuel


class CarSize:
    def __init__(self, car_length, car_width, car_height):
        self.car_length = car_length
        self.car_width = car_width
        self.car_height = car_height

    def check(self):
        return self.car_length, self.car_width, self.car_height


# 4.Stwórz klasę na wybrany przez siebie temat, która korzysta z elementów kompozycji.
class Fone:
    def __init__(self, car_name, engine_name,
                 engine_model, engine_power, engine_fuel,
                 car_length, car_width, car_height):
        self.car_name = car_name
        self.obj_engine = Engine(engine_name, engine_model, engine_power, engine_fuel)
        self.obj_carSize = CarSize(car_length, car_width, car_height)

    def check(self):
        return self.car_name, self.obj_engine.check(), self.obj_carSize.check()


fone = Fone('Mercedes', 'Mercedes', 'M10 EQ Power+', '1,6 V6T', 'Petronas Primax', '5000mm', '2000mm', '950mm')
print(fone.check())

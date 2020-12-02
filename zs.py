# 7. Kompozycja jako przykladowy element Programowania obiektowego dla zadania numer siedem.


class Engine:
    def __init__(self, engine_name, engine_model, engine_power, engine_fuel):
        self.engine_name = engine_name
        self.engine_model = engine_model
        self.engine_power = engine_power
        self.engine_fuel = engine_fuel

    def info(self):
        return f'Car Engine: {self.engine_name}, {self.engine_model}, {self.engine_power}, {self.engine_fuel}'


class Size:
    def __init__(self, car_length, car_width, car_height):
        self.car_length = car_length
        self.car_width = car_width
        self.car_height = car_height

    def info(self):
        return f'Car Size: {self.car_length}, {self.car_width}, {self.car_height}'


class Brakes:
    def __init__(self, disks, overlays):
        self.disks = disks
        self.overlays = overlays

    def info(self):
        return f'Brakes: {self.disks}, {self.overlays}'


class FormulaOne:
    def __init__(self, name, model, engine_name,
                 engine_model, engine_power, engine_fuel,
                 car_length, car_width, car_height, disks, overlays):
        self.name = name
        self.model = model
        self.obj_engine = Engine(engine_name, engine_model, engine_power, engine_fuel)
        self.obj_size = Size(car_length, car_width, car_height)
        self.obj_brakes = Brakes(disks, overlays)

    def info(self):
        print(f'Car Information: {self.name}, {self.model}', '\n', self.obj_engine.info(),
              '\n', self.obj_size.info(), '\n', self.obj_brakes.info())


mercedes = FormulaOne('Mercedes', 'AMG F1 W10 EQ Power+', 'Mercedes',
                      'M10 EQ Power+', '1,6 V6T', 'Petronas Primax',
                      '5000 мм', '2000 мм', '950 мм',
                      'Carbon', 'Carbone Industries')

redBull = FormulaOne('Red Bull', 'RB15', 'TAG Heuer',
                     'Honda R.A.619H', '1,6 L V6', 'Esso / Mobil 1',
                     '5000 мм', '2000 мм', '950 мм',
                     'Carbon fiber discs', 'Brembo')


def comparison():
    return mercedes.info(), '\n', redBull.info()


comparison()

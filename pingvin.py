"""Программа, которая будет выводить информацию о размере разных птиц."""
# Место для вашего кода.

class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size        

    
    def describe(self):
    # должен возвращать описание птицы в формате строки — Размер птицы {name} — {size}.    
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
    
    
    # Переопределите метод describe().
    def describe(self, full=False):
        if not full:
            return super().describe()
        return(f'Попугай {self.name} — заметная птица, окрас её перьев —'
               f'{self.color}, а размер — {self.size}. Интересный факт: попугаи'
               f'чувствуют ритм, а вовсе не бездумно двигаются под музыку. '
               f'Если сменить композицию, то и темп движений птицы изменится.')

    # Добавьте метод repeat().
    def repeat(self, phrase):
        return f'Попугай {self.name} говорит: {phrase}.'


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
    
    
    # Переопределите метод describe().    
    def describe(self, full=False):
        if not full:
            return super().describe()
        return(f'Размер пингвина {self.name} из рода {self.genus} — {self.size}. '
               f'Интересный факт: однажды группа геологов-разведчиков похитила пингвинье яйцо,'
               f' и их принялась преследовать вся стая, не пытаясь, '
               f'впрочем, при этом нападать. Посовещавшись, похитители вернули'
               f' птицам яйцо, и те отстали.')

    # Добавьте метод swimming().
    def swimming(self):
        return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч.'

kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
print(kesha.describe())
print(kowalski.describe(True))
print(kesha.repeat('Кеша хороший!'))
print(kowalski.swimming())

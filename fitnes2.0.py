from typing import Any
from typing import Dict, Type


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,  # Тип тренеровки
                 duration: float,     # Длительность тренеровки в часах
                 distance: float,     # Дистанция в км
                 speed: float,        # Средняя скорость
                 calories: float) -> None:     # Потраченные калории
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type};'
                f' Длительность: {self.duration:.3f} ч.;'
                f' Дистанция: {self.distance:.3f} км;'
                f' Ср. скорость: {self.speed:.3f} км/ч;'
                f' Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: float = 1000
    LEN_STEP: float = 0.65
    MIN_IN_H: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        # в базовом классе не нужно описывать поведение метода
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.__class__.__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79

    def __init__(self, action, duration, weight):
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                          * self.get_mean_speed()
                          + self.CALORIES_MEAN_SPEED_SHIFT)
                          * self.weight / self.M_IN_KM
                          * self.duration * self.MIN_IN_H)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_WEIGHT_MULTIPLIER: float = 0.035
    CALORIES_SPEED_HEIGHT_MULTIPLIER: float = 0.029
    KMH_IN_MSEC: float = 0.278
    MULTIPLIER_SQUARED = 2
    CM_IN_M = 100

    def __init__(self, action, duration, weight, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height / self.CM_IN_M

    def get_mean_speed(self) -> float:
        mean_speed = (self.get_distance() / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        spent_calories = (
            (self.CALORIES_WEIGHT_MULTIPLIER * self.weight
             + ((self.get_mean_speed() * self.KMH_IN_MSEC)
                ** self.MULTIPLIER_SQUARED / self.height)
             * self.CALORIES_SPEED_HEIGHT_MULTIPLIER * self.weight)
            * self.duration * self.MIN_IN_H)
        return spent_calories


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    CALORIES_MEAN_SPEED_SHIFT = 1.1
    CALORIES_WEIGHT_MULTIPLIER = 2

    def __init__(self, action, duration, weight,
                 length_pool: int, count_pool: int):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool  # длина бассейна в метрах
        self.count_pool = count_pool    # сколько раз переплыл бассейн

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = (self.length_pool
                      * self.count_pool
                      / self.M_IN_KM
                      / self.duration)
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        spent_calories = (
            (self.get_mean_speed() + self.CALORIES_MEAN_SPEED_SHIFT)
            * self.CALORIES_WEIGHT_MULTIPLIER
            * self.weight
            * self.duration)
        return spent_calories


def read_package(workout_type: str, data: list[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    trainings: dict[str, type[Training]] = {'RUN': Running,
                                            'SWM': Swimming,
                                        'WLK': SportsWalking}
    if workout_type not in trainings:
        return trainings[workout_type](*data)
    return f'непредвиденные данные'


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

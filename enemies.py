# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


# FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.

class RedDragon(Dragon):
    def __init__(self):
        self._health = 75
        self._attack = randint(10, 20)
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = randint(10, 20)
        self._color = 'черный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest


class TrollGuess(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = randint(10, 20)
        self._color = 'Тролль - угадай'

    def question(self):
        x = randint(1, 5)
        self.__quest = 'Угадай число от 1 до 5'
        self.set_answer(x)
        return self.__quest


class TrollIsPrime(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = randint(10, 20)
        self._color = 'Тролль - простое число'

    def question(self):
        x = randint(1, 1000)
        cnt = 0
        for i in range(2, x // 2 + 5):
            if x % i == 0:
                self.set_answer(0)
                cnt = 1
                break
        if cnt == 0:
            self.set_answer(1)
        self.__quest = "Простое ли число: " + str(x) + " " + ("(Пишите 1, если да, или 0, если нет)")
        return self.__quest


class TrollDels(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = randint(10, 20)
        self._color = 'Тролль - делители'

    def question(self):
        x = randint(1, 1000)
        ans = ""
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                ans = ans + str(i)
        self.set_answer(int(ans))
        self.__quest = "Перечислите делители числа " + str(x) + " " + "без пробелов"
        return self.__quest


enemy_types = [GreenDragon, RedDragon, BlackDragon, TrollGuess, TrollIsPrime, TrollDels]

from __future__ import annotations
from abc import ABC, abstractmethod


class Skill(ABC):
    """
    Базовый класс умения
    """
    def __init__(self):
        self.user = None
        self.target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def stamina(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def skill_effect(self) -> str:
        pass

    def _is_stamina_enough(self):
        return self.user.stamina >= self.stamina

    def use(self, user, target) -> str:
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла везде используем просто use
        """
        self.user = user
        self.target = target
        if self._is_stamina_enough:
            return self.skill_effect()
        return f"{self.user.name} попытался использовать {self.name} но у него не хватило выносливости."


class FuryPunch(Skill):
    name = 'Свирепый пинок'
    stamina = 6
    damage = 12

    def skill_effect(self):
        # TODO логика использования скилла -> return str
        # TODO в классе нам доступны экземпляры user и target - можно использовать любые их методы
        # TODO именно здесь происходит уменшение стамины у игрока применяющего умение и
        # TODO уменьшение здоровья цели.
        # TODO результат применения возвращаем строкой
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f'{self.user.name} используют {self.name} и наносит {self.damage} урона сопернику.'


class HardShot(Skill):
    name = 'Мощный укол'
    stamina = 5
    damage = 15

    def skill_effect(self):
        self.user.stamina -= self.stamina
        self.target.hp -= self.damage

        return f'{self.user.name} используют {self.name} и наносит {self.damage} урона сопернику.'

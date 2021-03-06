﻿from GameLogic.Character import *


class Player:

    def __init__(self, name, character, money=500, moves=0):
        self.Name = name
        if type(character) is int:
            if character == 0:
                self.Character = ForestCharacter()
            elif character == 1:
                self.Character = IceCharacter()
            elif character == 2:
                self.Character = DesertCharacter()
            elif character == 3:
                self.Character = SwampCharacter()
            else:
                raise Exception("%i is not a valid id for a character" % character)
        else:
            self.Character = character

        self.Money = money
        self.Moves = moves

        self._units = []

    @property
    def Units(self):
        return self._units

    def AddUnit(self, unit):
        self._units.append(unit)


'''
You need to create the class Warrior, the instances of
which will have 2 parameters - health (equal to 50
points) and attack (equal to 5 points), and 1 property
- is_alive, which can be True (if warrior's health is
> 0) or False (in the other case). In addition you have
to create the second unit type - Knight, which should
be the subclass of the Warrior but have the increased
attack - 7. Also you have to create a function fight(),
which will initiate the duel between 2 warriors and
define the strongest of them. The duel occurs according
to the following principle:

Every turn one of the warriors will hit another one and
the last will lose his health in the same value as the
attack of the first warrior. After that, the second
warrior will do the same to the first one.
If in the end of the turn the first warrior has > 0
health and the other one doesn’t, the function should
return True, in the other case it should return False.

Input: The warriors.

Output: The result of the duel (True or False).
'''

# methods invoked with (), eg. .time()
# @property turns a method into a "getter" read only
# now we access method as attribute without brackets  eg. .time
# https://www.machinelearningplus.com/python/python-property/

class Warrior:
    def __init__(self, attack=5, health=50):
        self.health = health
        self.attack = attack
    @property
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Knight(Warrior):
    def __init__(self, attack=7, **kwargs):
        super().__init__(attack, **kwargs)
    @property
    def is_alive(self):
        return super(Knight, self).is_alive

def fight(unit_1, unit_2):
    health_1 = unit_1.health
    attack_1 = unit_1.attack
    health_2 = unit_2.health
    attack_2 = unit_2.attack
    round_num = 1
    # print(round_num)
    # print('W:', health_1, 'K:', health_2)
    while True:
        if round_num % 2 != 0:
            round_num += 1
            health_2 -= attack_1
            # print(round_num)
            # print('W:', health_1, 'K:', health_2)
            if health_2 <= 0:
                unit_2.health = health_2
                unit_1.health = health_1
                return True
        else:
            round_num += 1
            health_1 -= attack_2
            # print(round_num)
            # print('W:', health_1, 'K:', health_2)
            if health_1 <= 0:
                unit_2.health = health_2
                unit_1.health = health_1
                return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        return "A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        if isinstance(viking, Viking): # For handling errors if try to add something different of a Viking
          self.vikingArmy.append(viking)  
    
    def addSaxon(self, saxon): # For handling errors if try to add something different of a Saxon
        if isinstance(saxon, Saxon):
          self.saxonArmy.append(saxon)  
    
    def vikingAttack(self):
        response = "War is over"
        if self.vikingArmy and self.saxonArmy:
            # Select random viking and saxon
            rand_viking = random.choice(self.vikingArmy)
            rand_saxon = random.choice(self.saxonArmy)

            # Call Saxon receiveDamage() method using the strenght of viking
            response = rand_saxon.receiveDamage(rand_viking.strength)

            # Check if the saxon dies, then remove it from the army
            if rand_saxon.health<=0: self.saxonArmy.remove(rand_saxon)

            # Return the response of calling saxon.receiveDamage()
        return response
    
    def saxonAttack(self):
        response = "War is over"
        if self.vikingArmy and self.saxonArmy:
            # Select random viking and saxon
            rand_viking = random.choice(self.vikingArmy)
            rand_saxon = random.choice(self.saxonArmy)

            # Call Viking receiveDamage() method using the strenght of Saxon
            response = rand_viking.receiveDamage(rand_saxon.strength)

            # Check if the Viking dies, then remove it from the army
            if rand_viking.health<=0: self.vikingArmy.remove(rand_viking)

            # Return the response of calling viking.receiveDamage()
        return response

    def showStatus(self):
        # Check if still are at least 1 viking and 1 saxon
        if self.vikingArmy and self.saxonArmy: return "Vikings and Saxons are still in the thick of battle."
        # Check if still are at least 1 saxon
        elif not self.vikingArmy and self.saxonArmy: return "Saxons have fought for their lives and survive another day..."
        # Check if still are at least 1 viking
        elif self.vikingArmy and not self.saxonArmy: return "Vikings have won the war of the century!"
        # Check if both armys are dead
        else: return "Everyone died and no one won the war"


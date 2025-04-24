from abc import ABC, abstractmethod

class Superhero(ABC):
    def __init__(self, name, power, secret_identity, health=100):
        self._name = name                # Encapsulated attribute
        self.power = power
        self.secret_identity = secret_identity
        self.health = health

    @abstractmethod
    def use_power(self):
        pass

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"💥 {self._name} took {damage} damage! Health: {self.health}")

    def __str__(self):
        return f"🦸 {self._name} | Power: {self.power} | Health: {self.health}"

class HumanHero(Superhero):  # Fixed indentation
    def use_power(self):
        print(f"🕸️ {self._name} shoots webs: {self.power}!")
        self.take_damage(3)

class MutantHero(Superhero):
    def __init__(self, name, power, secret_identity, mutation_level):
        super().__init__(name, power, secret_identity)
        self.mutation_level = mutation_level
        self._sidekick = None  # Encapsulated attribute

    def use_power(self):
        print(f"🧬 {self._name} unleashes {self.power} at level {self.mutation_level}!")
        self.take_damage(5)

    @property
    def sidekick(self):
        return self._sidekick

    @sidekick.setter
    def sidekick(self, value):
        self._sidekick = value
        print(f"🦸♂️➡️🦸♀️ {self._name} gained a new sidekick: {value}!")

# Create superhero instances
storm = MutantHero("Storm", "Weather Control", "Ororo Munroe", 85)
spidey = HumanHero("Spider-Man", "Web Slinging", "Peter Parker")  # Now using correct class

# Test the functionality
storm.use_power()
storm.sidekick = "Nightcrawler"
print(storm)
spidey.use_power()
print(spidey)
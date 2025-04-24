from abc import ABC, abstractmethod  # ADD THIS IMPORT

class MovementSystem:
    class Moveable(ABC):  # Now correctly inherits from ABC
        @abstractmethod
        def move(self):
            pass

    class Flyer(Moveable):
        def move(self):
            print("🚀 Soaring through the clouds!")

    class Swinger(Moveable):
        def move(self):
            print("🕸️ Swinging between skyscrapers!")

    class Teleporter(Moveable):
        def move(self):
            print("🌀 BAMF! Instant teleportation!")

# Create movement instances
jetpack_move = MovementSystem.Flyer()
webs_move = MovementSystem.Swinger()
portal_move = MovementSystem.Teleporter()

# Polymorphism in action
movement_styles = [jetpack_move, webs_move, portal_move]
for style in movement_styles:
    style.move()
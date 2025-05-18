class Animal:
    alive = []

    def __init__(self, name: str,
                 health: int = 100, hidden: bool = False) -> None:
        self.health = health
        self.name = name
        self.hidden = hidden
        if self.health > 0:
            Animal.alive.append(self)
        else:
            Animal.alive.remove(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, animal: Herbivore) -> None:
        if not animal.hidden and isinstance(animal, Herbivore):
            animal.health -= 50
            if animal.health <= 0:
                Animal.alive.remove(animal)

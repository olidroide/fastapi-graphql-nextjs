from typing import List, Dict

from .models.person import Person, Fruit


class DataProvider:
    def __init__(self) -> None:
        pass

    async def get_persons(self) -> List[Person]:
        pass

    async def get_person(self, by_id: str) -> Person:
        pass

    async def create_person(self, name: str
                            ) -> Person:
        pass

    async def delete_person(self, by_id: str
                            ) -> Person:
        pass

    async def get_fruits(self) -> List[Fruit]:
        pass

    async def create_fruit(self, name: str, eaten_by: Person = None) -> Fruit:
        pass

    async def eat_fruit(self, person: Person, fruit: Fruit):
        pass


class FakeData(DataProvider):
    _persons: Dict[str, Person]
    _fruits: Dict[str, Fruit]

    def __init__(self) -> None:
        super().__init__()

        jim = Person(name="Jim")
        michael = Person(name="Michael")
        self._persons = {jim.id: jim, michael.id: michael}

        apple = Fruit(name="Apple", eaten_by=jim)
        pear = Fruit(name="Pear")
        self._fruits = {apple.id: apple, pear.id: pear}

    async def delete_person(self, by_id: str) -> Person:
        return self._persons.pop(by_id, None)

    async def get_persons(self) -> List[Person]:
        return list(self._persons.values())

    async def get_person(self, by_id: str) -> Person:
        return self._persons[by_id]

    async def create_person(self, name: str) -> Person:
        new_person = Person(name=name)
        self._persons[str(new_person.id)] = new_person
        return new_person

    async def get_fruits(self) -> List[Fruit]:
        return list(self._fruits.values())

    async def create_fruit(self, name: str, eaten_by: Person = None) -> Fruit:
        new_fruit = Fruit(name=name, eaten_by=eaten_by)
        self._fruits[str(new_fruit.id)] = new_fruit
        return new_fruit

    async def eat_fruit(self, person: Person, fruit: Fruit):
        fruit_found = next(filter(lambda fruit_element: fruit_element == fruit, self._fruits), None)
        person_found = next(filter(lambda person_element: person_element == person, self._persons), None)
        fruit_found.eaten_by = person_found

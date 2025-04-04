class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for human in people:
        hum = Person(name=human["name"], age=human["age"])
        persons_list.append(hum)

    for human in people:
        person = Person.people[human["name"]]

        if "wife" in human and human["wife"] is not None:
            person.wife = Person.people[human["wife"]]

        if "husband" in human and human["husband"] is not None:
            person.husband = Person.people[human["husband"]]

    return persons_list

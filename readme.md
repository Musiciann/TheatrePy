# Classes and Program Realization Documentation

## Overview

The classes `Actor`, `Auditorium`,`Costume`,
`CostumeDepartment`,`Decoration`,`Director`,
`Director`,`Performance`,`Scene`,`Theatre`,
`Ticket`, `Visitor` is classes that represents
theatrical entities (abstractions). 
Classes `Actor`, `Director`, `Visitor`
extends the `Person` class,
inheriting its properties and methods, 
while adding additional attributes relevant to specific
entities.

## Classes Definitions

### `Person`
```python
class Person:

    def __init__(self, *, person_name: str = "Undefined", person_age: int = 0) -> None:
        self.__person_name = person_name
        self.__person_age = person_age

    @property
    def person_name(self) -> str:
        return self.__person_name

    @property
    def person_age(self) -> int:
        return self.__person_age

```

### `Actor`
```python
from Source.ClassPerson import Person
from Source.ClassCostume import Costume

class Actor(Person):

    def __init__(self, *, actor_name: str = "Undefined", actor_age: int = 0, actor_costume: Costume, actor_role: str) -> None:
        super().__init__(person_name = actor_name, person_age = actor_age)
        self.__actor_costume = actor_costume
        self.__actor_role = actor_role

    def __str__(self) -> str:
        return f"{self.person_name=}, {self.person_age}, {self.actor_role}"

    @property
    def actor_costume(self) -> Costume:
        return self.__actor_costume

    @property
    def actor_role(self) -> str:
        return self.__actor_role

    @actor_role.setter
    def actor_role(self, *, actor_role: str) -> None:
        self.__actor_role = actor_role

    @actor_costume.setter
    def actor_costume(self, *, actor_costume: Costume) -> None:
        self.__actor_costume = actor_costume

    def change_theatrical_character(self, *, new_actor_costume: Costume, new_actor_role: str) -> None:
        self.__actor_costume = new_actor_costume
        self.__actor_role = new_actor_role
```

### `Costume`
```python
class Costume:

    def __init__(self, *, costume_main_color: str, costume_material: str, costume_name: str) -> None:
        self.__costume_main_color = costume_main_color
        self.__costume_material = costume_material
        self.__costume_name = costume_name

    @property
    def costume_main_color(self) -> str:
        return self.__costume_main_color

    @property
    def costume_material(self) -> str:
        return self.__costume_material

    @property
    def costume_name(self) -> str:
        return self.__costume_name
```

### `CostumeDepartment`
```python
from Source.ClassCostume import Costume

class CostumeDepartment:

    def __init__(self, *, size: int = 20, costumes: list[Costume]) -> None:
        self.__size = size
        self.__costumes = costumes

    @property
    def size(self) -> int:
        return self.__size

    @property
    def costumes(self) -> list[Costume]:
        return self.__costumes

    @costumes.setter
    def costumes(self, *, costumes: list[Costume]) -> None:
        self.__costumes = costumes

    def create_costume(self, *, costume_main_color: str, costume_material: str, costume_name: str) -> None:
        new_costume = Costume(costume_main_color = costume_main_color,
                              costume_material = costume_material,
                              costume_name = costume_name)
        self.costumes.append(new_costume)

    def costume_amount(self) -> int:
        return len(self.costumes)

    def is_costume_for_role(self, *, necessary_costume_name: str) -> bool:
        is_costume = False
        for costume in self.costumes:
            if costume.costume_name == necessary_costume_name:
                is_costume = True
                return is_costume
        return is_costume

    def costumes_for_performance(self, *, costume_names: list[str]) -> list[Costume]:
        necessary_costumes = []
        for costume in self.costumes:
            if costume.costume_name in costume_names:
                necessary_costumes.append(costume)
        return necessary_costumes
```

### `Ticket`
```python
class Ticket:

    def __init__(self, *, ticket_price: int, sit_in_auditorium: int, performance_name: str) -> None:
        self.__ticket_price = ticket_price
        self.__sit_in_auditorium = sit_in_auditorium
        self.__performance_name = performance_name

    def __str__(self) -> str:
        return f"{self.__ticket_price=}, {self.__sit_in_auditorium=}, {self.__performance_name}"

    @property
    def ticket_price(self) -> int:
        return self.__ticket_price

    @property
    def sit_in_auditorium(self) -> int:
        return self.__sit_in_auditorium

    @property
    def performance_name(self) -> str:
        return self.__performance_name

    @ticket_price.setter
    def ticket_price(self, *, ticket_price: int):
        self.__ticket_price = ticket_price
```

### `Decoration`
```python
class Decoration:

    def __init__(self, *, decoration_name: str, decoration_kind: str) -> None:
        self.__decoration_kind = decoration_kind
        self.__decoration_name = decoration_name

    def __str__(self) -> str:
        return f"{self.decoration_name}, {self.decoration_kind}"

    @property
    def decoration_name(self) -> str:
        return self.__decoration_name

    @property
    def decoration_kind(self) -> str:
        return self.__decoration_kind
```

### `Theatre`
```python
from Source.ClassTicket import Ticket

class Theatre:

    def __init__(self, *, theatre_name: str, tickets: list[Ticket]) -> None:
        self.__theatre_name = theatre_name
        self.__tickets = tickets

    @property
    def theatre_name(self) -> str:
        return self.__theatre_name

    @property
    def tickets(self) -> list[Ticket]:
        return self.__tickets

    @tickets.setter
    def tickets(self, *, tickets: list[Ticket]):
        self.tickets = tickets
```

### `Performance`
```python
from Source.ClassActor import Actor
from Source.ClassDecoration import Decoration

class Performance:

    def __init__(self, *, performance_name: str, necessary_actors: list[Actor],
                 necessary_decorations: list[Decoration]) -> None:
        self.__performance_name = performance_name
        self.__necessary_actors = necessary_actors
        self.__necessary_decorations = necessary_decorations

    @property
    def necessary_decorations(self) -> list[Decoration]:
        return self.__necessary_decorations

    @property
    def necessary_actors(self) -> list[Actor]:
        return self.__necessary_actors

    @property
    def performance_name(self) -> str:
        return self.__performance_name
```
### `Visitor`
```python
from Source.ClassTheatre import Theatre
from Source.ClassPerson import Person
from Source.ClassTicket import Ticket

class Visitor(Person):

    def __init__(self, *, name: str, age: int, have_tickets: list[Ticket]) -> None:
        super().__init__(person_name=name, person_age=age)
        self.__have_tickets = have_tickets

    @property
    def have_tickets(self) -> list[Ticket]:
        return self.__have_tickets

    def buy_ticket(self, *, theatre: Theatre, performance_name: str, ticket_sit_number: int) -> None:
        for ticket in theatre.tickets:
            if ticket.sit_in_auditorium == ticket_sit_number:
                theatre.tickets.remove(ticket)
                self.have_tickets.append(ticket)
            else:
                print(f"Ticket for {performance_name} and {ticket_sit_number} sit number wasn't found")

```

### `Scene`
```python
from Source.ClassDecoration import Decoration
from Source.ClassVisitor import Visitor

class Scene:

    def __init__(self, *, decorations: list[Decoration], invited_visitors: list[Visitor]) -> None:
        self.__decorations = decorations
        self.invited_visitors = []

    @property
    def decorations(self) -> list[Decoration]:
        return self.__decorations

    def add_decoration(self, *, new_decoration: Decoration):
        self.__decorations.append(new_decoration)

    def invite_visitor_to_stage(self, *, visitor: Visitor):
        self.invited_visitors.append(visitor)
```

### `Auditorium`
```python
from Source.ClassVisitor import Visitor

class Auditorium:

    def __init__(self, *, visitors: list[Visitor], sits: set[int]) -> None:
        self.__visitors = visitors
        self.__sits = {}

    @property
    def visitors(self) -> list[Visitor]:
        return self.__visitors

    def take_sit(self, *, visitor: Visitor, sit_number: int) -> bool:
        could_sit = True
        if sit_number not in self.__sits.keys():
            self.__visitors.append(visitor)
            self.__sits[sit_number] = visitor
            return could_sit
        could_sit = False
        return could_sit
```

### `Director`
```python
from Source.ClassPerson import Person
from Source.ClassPerformance import Performance
from Source.ClassActor import Actor
from Source.ClassTicket import Ticket
from Source.ClassDecoration import Decoration

class Director(Person):

    def __init__(self, *, name: str, age: int, experience_year: int, performances: list[Performance]) -> None:
        super().__init__(person_name=name, person_age=age)
        self.__experience_year = experience_year
        self.__performances = performances

    @property
    def experience_year(self) -> int:
        return self.__experience_year

    @property
    def performances(self) -> list[Performance]:
        return self.__performances

    def make_performance(self, *, necessary_actor: list[Actor], necessary_decorations: list[Decoration],
                         new_performance_name: str) -> None:
        new_performance = Performance(performance_name = new_performance_name,
                                      necessary_actors = necessary_actor,
                                      necessary_decorations = necessary_decorations)
        self.__performances.append(new_performance)
```

## Module Imports

The demonstration program imports 12 modules (12 necesarry classes):


```python
from Source.ClassPerson import Person
from Source.ClassCostume import Costume
from Source.ClassActor import Actor
from Source.ClassDecoration import Decoration
from Source.ClassPerformance import Performance
from Source.ClassTicket import Ticket
from Source.ClassTheatre import Theatre
from Source.ClassScene import Scene
from Source.ClassVisitor import Visitor
from Source.ClassAuditorium import Auditorium
from Source.ClassCostumeDepartment import CostumeDepartment
from Source.ClassDirector import Director
```

1. `Person` from `Source.ClassPerson` - Represents a person with basic attributes such as name and age.
2. `Costume` from `Source.ClassCostume` - Represents a costume that an actor can wear.
3. `CostumeDepartment` from `Source.ClassCostumeDepartment` - Represents a costume department, where costumes for actors are made and store.
4. `Ticket` from `Source.ClassTicket` - Represents a ticket that a visitor could buy in a theatre.
5. `Theatre` from `Source.ClassTheatre` - Represents a theatre, where visitors could buy tickets for performances and watch them.
6. `Visitor` from `Source.ClassVisitor` - Represents a visitor that could buy tickets in a theatre and enjoy performances.
7. `Decoration` from `Source.ClassDecoration` - Represents a decoration that can be used on a scene.
8. `Scene` from `Source.ClassScene` - Represents a scene, where performances are made with interactions with visitors from auditorium.
9. `Auditorium` from `Source.ClassAuditorium` - Represents an auditorium, where visitors could take a sits and watch performances.
10. `Performance` from `Source.ClassPerformance` - Represents a performance which was made by a director in a theatre.
11. `Actor` from `Source.ClassActor` - Represents an actor, which could take part in performances.
12. `Director` from `Source.ClassDirector` - Represents a director of a theatre, which could make new performances.

## Demonstration program description
### Demonstration program overview

This code represents a program system which is related to a theatre.
Main part of this code is a continuous loop that prompts 
the user to choose from various menu options related to subject area of theatral performances.
Based on the user input, it displays 
relevant details regarding the selected menu option.

### Creation of all necessary entities
```python
person = Person(person_name="Alex", person_age=22)

first_costume = Costume(costume_name="Bad guy", costume_material="cotton",
                           costume_main_color="gray")

second_costume = Costume(costume_name="Chill guy", costume_material="cotton",
                           costume_main_color="yellow")

actor = Actor(actor_name="Alex", actor_age=23, actor_costume=first_costume, actor_role="main role")

actors = [actor]

ticket = Ticket(ticket_price=100, sit_in_auditorium=12, performance_name="Christmas")

theatre = Theatre(theatre_name="Great Theatre", tickets=[])

decoration = Decoration(decoration_name="Tree", decoration_kind="Forest")

new_decoration = Decoration(decoration_name="Bush", decoration_kind="Forest")

tickets = [ticket]

visitor = Visitor(name="Alex", age=23, have_tickets=tickets)

visitors = [visitor]

decorations = [decoration]

scene = Scene(decorations=decorations, invited_visitors=[])

performance = Performance(performance_name="Romeo and Julietta", necessary_actors=actors,
                              necessary_decorations=decorations)

sits = {1, 2, 3}

auditorium = Auditorium(visitors=visitors, sits=sits)

costume_department = CostumeDepartment(size=25, costumes=[])

performances = [performance]

director = Director(name = "Victoria", age = 43, experience_year = 6, performances = performances)
```
In this part of the program all necessary entities from all classes are made for faster and better experience.

### Main menu view
```python
print("""<<< Choose menu option >>>:
 ___________________________________________________________________________________
//+=============================================================|+=+=+=+=+=+=+=+=+=||
| 1 - Print actor's name and age                                | Actor info       (|
| 2 - Print actor's role                                        | Actor role       [|
| 3 - Print actor's costume info                                | Costume info     (|
| 4 - Change actor's theatrical character                       | Change role      [|
| 5 - Print ticket information                                  | Ticket info      (|
| 6 - Print decoration information                              | Decoration info  [|
| 7 - Print theatre info                                        | Theatre info     (|
| 8 - Add new ticket in theatre                                 | Add ticket       [|
| 9 - Create new costume in costume department                  | Make costume     (|
| 10 - Check if exist costume for role                          | Costume exist    [|
| 11 - Print performance info                                   | Performance info (|
| 12 - Visitor buy's a new ticket                               | Buy ticket       [|
| 13 - Check if visitor could take a sit                        | Check sit        (|
| 14 - Add decoration to stage                                  | Add decoration   [|
| 15 - Invite visitor to scene                                  | Invite           (|
| 16 - Make new performance                                     | Performance      [|
| 17 - End program demonstration                                | Exit            //|
|                                                               |                ///
(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)(*)//
""")
```
That's how main menu of the program looks like.

### Infinite Loop

The loop uses `while True:` to create an infinite loop
allowing the user to make choices repeatedly
until the program is terminated externally.

### Menu options

```python
menu = input('Enter menu option here >>> ')
    if menu == 'Actor info':
        print(f"Actor: {actor.person_name=}, {actor.person_age=}")
        print()
```
1. **Actor info**:
   - Displays the actor's name and age by accessing the `actor` object's `person_name` and `person_age` attributes.
   - Example output: `Actor: actor.person_name=<Name>, actor.person_age=<Age>`

```python
    elif menu == 'Actor role':
        print(f"Actor: {actor.actor_role=}")
        print()
```
**Actor role**:
   - Prints the current role of the actor by accessing the `actor` object's `actor_role` attribute.
   - Example output: `Actor: actor.actor_role=<Role>`

```python
    elif menu == 'Costume info':
        print(f"Actor's costume: {actor.actor_costume.costume_name=}, {actor.actor_costume.costume_material=},"
              f"{actor.actor_costume.costume_main_color=}")
        print()
```
**Costume info**:
   - Provides information about the actor's costume, including the costume name, material, and main color by accessing respective attributes of the `actor.actor_costume` object.
   - Example output: `Actor's costume: actor.actor_costume.costume_name=<Name>, actor.actor_costume.costume_material=<Material>, actor.actor_costume.costume_main_color=<Color>`

```python
 elif menu == 'Change role':
        new_role = input("Enter new actor's role >>> ")
        actor.change_theatrical_character(new_actor_costume=second_costume, new_actor_role=new_role)
        print(f"Actor: {actor.actor_role=}, {actor.actor_costume.costume_name}")
        print()
```
**Change role**:
   - Allows the user to change the actor's role. It prompts for a new role input and calls the `change_theatrical_character` method of the `actor` object, passing in a new costume (presumably `second_costume`) and the new role.
   - Displays the updated actor role and costume name.
   - Example output: `Actor: actor.actor_role=<New Role>, actor.actor_costume.costume_name=<Costume Name>`

```python
 elif menu == 'Ticket info':
        print(f"Ticket: {ticket.ticket_price=}, {ticket.sit_in_auditorium}, {ticket.performance_name}")
        print()
```
**Ticket info**:
   - Outputs ticket details such as price and seating information by accessing the `ticket` object's attributes.
   - Example output: `Ticket: ticket.ticket_price=<Price>, ticket.sit_in_auditorium=<Seat>, ticket.performance_name=<Performance>`

```python
    elif menu == 'Decoration info':
        print(f"Decoration: {decoration.decoration_name=}, {decoration.decoration_kind}")
        print()
```
**Decoration info**:
   - Displays the decoration's details by accessing the `decoration` object’s attributes.
   - Example output: `Decoration: decoration.decoration_name=<Name>, decoration.decoration_kind=<Kind>`

```python
 elif menu == 'Theatre info':
        print(f"Theatre: {theatre.theatre_name=}, {theatre.tickets=}")
        print()
```
**Theatre info**:
   - Provides information about the theatre, including its name and the number of tickets available.
   - Example output: `Theatre: theatre.theatre_name=<Name>, theatre.tickets=<Ticket Count>`

```python
    elif menu == 'Add ticket':
        ticket_price = int(input("Input new ticket price >>> "))
        performance_name = input("Input performance name >>> ")
        sit_number = int(input("Input new ticket sit number >>> "))
        second_ticket = Ticket(ticket_price = ticket_price, sit_in_auditorium = sit_number,
                               performance_name = performance_name)
        theatre.tickets.append(second_ticket)
        print(f"Theatre: tickets amount: {len(theatre.tickets)}")
        print()
```
When the user selects the option 'Add ticket', the following steps occur:

- **User Inputs**: The program requests the user to input the new ticket price, performance name, and seat number.

- **Ticket Creation**: A new `Ticket` instance is created using the input values. This ticket is associated with a specific performance and seat number.

- **Appending to Ticket List**: The newly created ticket is added to the `theatre.tickets` list, which keeps track of all tickets available for performances.

- **Output**: The program outputs the total number of tickets in the theatre after the addition of the new ticket.

```python
    elif menu == 'Make costume':
        print(f"Costume department (new costume): costumes at start: {costume_department.costume_amount()}")
        color = input("Input new costume color >>> ")
        material = input("Input new costume material >>> ")
        name = input("Input new costume name >>> ")
        costume_department.create_costume(costume_name = name, costume_material = material,
                                          costume_main_color = color)
        print(f"Costume department (new costume): {costume_department.costume_amount()}")
        print()
```
When the user chooses 'Make costume', the following actions take place:

- **Initial Count Display**: The program first displays the current number of costumes in the costume department.

- **User Inputs**: The user is prompted to enter the details for the new costume, including color, material, and name.

- **Costume Creation**: A new costume is created using the `create_costume` method of the `costume_department` object, incorporating the provided details.

- **Updated Count Display**: After creating the costume, the updated total number of costumes in the department is displayed.

```python
    elif menu == 'Costume exist':
        necessary_costume = input("Input necessary costume name >> ")
        print(f"Costume exist: {costume_department.is_costume_for_role(necessary_costume_name=necessary_costume)}")
        print()
```
In the case of the 'Costume exist' option:

- **User Input**: The program asks for the name of the costume that needs to be checked.

- **Existence Verification**: The method `is_costume_for_role` is called on the `costume_department` object to determine if the specified costume exists.

- **Output**: The result of the check is printed, indicating whether the necessary costume exists or not.

```python
 elif menu == 'Performance info':
        print(f"Performance: {performance.performance_name=}, {performance.necessary_actors=},"
              f"{performance.necessary_decorations}")
        print()
```
**Performance info**:
   - Displays the performance's details by accessing the `performance` object’s attributes.
   - Example output: `performance: performance.performance_name=<Name>, performance.necessary_actors=<Actors>, performance.necessary_decorations=<Decorations>`

```python
    elif menu == 'Buy ticket':
        print(f"Visitor's tickets: {len(visitor.have_tickets)}")
        print(f"Theatre tickets: {len(theatre.tickets)}")
        second_ticket = Ticket(ticket_price=20, sit_in_auditorium=1,
                               performance_name="Good")
        theatre.tickets.append(second_ticket)
        print("Ticket appeared in theatre.")
        print(f"Theatre tickets: {len(theatre.tickets)}")
        print("Visitor buys ticket in theatre.")
        visitor.buy_ticket(theatre = theatre, performance_name = "Good", ticket_sit_number=1)
        print(f"Visitor's tickets: {len(visitor.have_tickets)}")
        print(f"Theatre tickets: {len(theatre.tickets)}")
        print()
```
In the case of the 'Buy ticket' option:

- **Start output**: The program shows how many tickets a visitor already have and how
much ticket in a theatre.

- **Processing**: The program creates new ticket `second_ticket` and add it to `theatre.tickets` list.

- **Call function**: The program calls function `visitor.buy_ticket(...)` with necessary attributes
and represent process of buying a ticket by a visitor from a theatre. 
(Add ticket to `visitor.have_tickets` list from `theatre.tickets` list)

- **Output**: The result of the process is printed, indicating amount of tickets has visitor and theatre.

```python
    elif menu == 'Check sit':
        print(f"Auditorium visitors: {len(auditorium.visitors)}")
        necessary_sit = input("Insert sit number >>> ")
        if auditorium.take_sit(visitor=visitor, sit_number=2):
            print(f"Auditorium visitors (True): {len(auditorium.visitors)}")
            print()
        else:
            print(f"Auditorium visitors (False): {len(auditorium.visitors)}")
            print()
```
In the case of the 'Check sit' option:

- **Start output**: The program shows how many visitors already sitting in an auditorium.

- **User input**: The program asks user to insert necessary sit number.

- **Processing**: The program calls function `auditorium.take_sit(...)` with necessary attributes
which checks if a visitor could take a sit there.

- **Output**: The result of the process is printed (True or False), indicating amount of visitors now in
auditorium and could a visitor take a sit or not.


```python
    elif menu == 'Add decoration':
        print(f"Scene decor amount: {len(scene.decorations)}")
        scene.add_decoration(new_decoration = new_decoration)
        print("New decoration was added.")
        print(f"Scene decor amount: {len(scene.decorations)}")
        print()
```
In the case of the 'Add decoration' option:

- **Start output**: The program shows how many decorations is on a scene.

- **Processing**: The program calls function `scene.add_decoration(new_decoration = new_decoration)`
which adds new decoration to the scene.

- **Output**: The result of the process is printed, indicating amount of decorations now on the scene.

```python
 elif menu == 'Invite':
        print(f"Scene visitors: {len(scene.invited_visitors)}")
        scene.invite_visitor_to_stage(visitor = visitor)
        print("New visitor was invited to the scene. ")
        print(f"Scene visitors: {len(scene.invited_visitors)}")
        print()
```
In the case of the 'Invite' option:

- **Start output**: The program shows how many visitors is on a scene.

- **Processing**: The program calls function `scene.invite_visitor_to_stage(visitor = visitor)`
which adds new visitor to the scene.

- **Output**: The result of the process is printed, indicating amount of visitors now on the scene.


```python
    elif menu == 'Performance':
        print(f"Director's performances: {len(director.performances)}")
        new_performance_name = input("Input new performance name >>> ")
        director.make_performance(necessary_actor = actors, necessary_decorations = decorations,
                                  new_performance_name = new_performance_name)
        print(f"Director's performances: {len(director.performances)}")
        print()
```
In the case of the 'Performance' option:

- **Start output**: The program shows how many performances has a director.

- **Processing**: The program calls function `director.make_performance(necessary_actor = actors, necessary_decorations = decorations,
                                  new_performance_name = new_performance_name)`
which creates a new performance and adds it to the `director.performances`.

- **Output**: The result of the process is printed, indicating amount performances has a director.

```python
    elif menu == 'Exit':
        raise SystemExit
```
**Exit option**: With this option the program will be finished (exit with code 0)

```python
        else: print('Such option is not exist')
```
**Wrong option**: If wrong option was entered, show message, that suggests 'Such option is not exist'

## Conclusion

This demonstration program enhances the theatre's functionality by allowing 
users to manage different theatre entities effectively. 
By adding features for ticket management and costume handling (and others),
it supports the operational needs of the theatre, thus contributing 
to a better organized and more efficient system. This interactivity 
promotes user engagement, ensuring that users 
can easily access and modify elements related to performances.
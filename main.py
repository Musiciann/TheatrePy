from Source.ClassPerson import 
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

while True:

    menu = input('Enter menu option here >>> ')
    if menu == 'Actor info':
        print(f"Actor: {actor.person_name=}, {actor.person_age=}")
        print()

    elif menu == 'Actor role':
        print(f"Actor: {actor.actor_role=}")
        print()

    elif menu == 'Costume info':
        print(f"Actor's costume: {actor.actor_costume.costume_name=}, {actor.actor_costume.costume_material=},"
              f"{actor.actor_costume.costume_main_color=}")
        print()

    elif menu == 'Change role':
        new_role = input("Enter new actor's role >>> ")
        actor.change_theatrical_character(new_actor_costume=second_costume, new_actor_role=new_role)
        print(f"Actor: {actor.actor_role=}, {actor.actor_costume.costume_name}")
        print()

    elif menu == 'Ticket info':
        print(f"Ticket: {ticket.ticket_price=}, {ticket.sit_in_auditorium}, {ticket.performance_name}")
        print()

    elif menu == 'Decoration info':
        print(f"Decoration: {decoration.decoration_name=}, {decoration.decoration_kind}")
        print()

    elif menu == 'Theatre info':
        print(f"Theatre: {theatre.theatre_name=}, {theatre.tickets=}")
        print()

    elif menu == 'Add ticket':
        ticket_price = int(input("Input new ticket price >>> "))
        performance_name = input("Input performance name >>> ")
        sit_number = int(input("Input new ticket sit number >>> "))
        second_ticket = Ticket(ticket_price = ticket_price, sit_in_auditorium = sit_number,
                               performance_name = performance_name)
        theatre.tickets.append(second_ticket)
        print(f"Theatre: tickets amount: {len(theatre.tickets)}")
        print()

    elif menu == 'Make costume':
        print(f"Costume department (new costume): costumes at start: {costume_department.costume_amount()}")
        color = input("Input new costume color >>> ")
        material = input("Input new costume material >>> ")
        name = input("Input new costume name >>> ")
        costume_department.create_costume(costume_name = name, costume_material = material,
                                          costume_main_color = color)
        print(f"Costume department (new costume): {costume_department.costume_amount()}")
        print()

    elif menu == 'Costume exist':
        necessary_costume = input("Input necessary costume name >> ")
        print(f"Costume exist: {costume_department.is_costume_for_role(necessary_costume_name=necessary_costume)}")
        print()

    elif menu == 'Performance info':
        print(f"Performance: {performance.performance_name=}, {performance.necessary_actors=},"
              f"{performance.necessary_decorations}")
        print()

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

    elif menu == 'Check sit':
        print(f"Auditorium visitors: {len(auditorium.visitors)}")
        necessary_sit = input("Insert sit number >>> ")
        if auditorium.take_sit(visitor=visitor, sit_number=2):
            print(f"Auditorium visitors (True): {len(auditorium.visitors)}")
            print()
        else:
            print(f"Auditorium visitors (False): {len(auditorium.visitors)}")
            print()

    elif menu == 'Add decoration':
        print(f"Scene decor amount: {len(scene.decorations)}")
        scene.add_decoration(new_decoration = new_decoration)
        print("New decoration was added.")
        print(f"Scene decor amount: {len(scene.decorations)}")
        print()

    elif menu == 'Invite':
        print(f"Scene visitors: {len(scene.invited_visitors)}")
        scene.invite_visitor_to_stage(visitor = visitor)
        print("New visitor was invited to the scene. ")
        print(f"Scene visitors: {len(scene.invited_visitors)}")
        print()

    elif menu == 'Performance':
        print(f"Director's performances: {len(director.performances)}")
        new_performance_name = input("Input new performance name >>> ")
        director.make_performance(necessary_actor = actors, necessary_decorations = decorations,
                                  new_performance_name = new_performance_name)
        print(f"Director's performances: {len(director.performances)}")
        print()

    elif menu == 'Exit':
        raise SystemExit

    else: print('Such option is not exist')






















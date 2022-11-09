from datetime import datetime
import json


class Customer:

    def __init__(self, name: str, surname: str, type: str):
        self.name = name
        self.surname = surname
        self.type = type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer_type error")
        self.__type = value


class Event:

    def __init__(self, event_id: int):
        with open("Events.json", "r", encoding="utf-8") as file:
            events_info = json.load(file)["events"]
        for event in events_info:
            if event == str(event_id):
                self.id = str(event_id)
                self.date = datetime.strptime(events_info[self.id]["eventDate"], "%d.%m.%Y")
                break
        else:
            raise ValueError("No event with such id")

    def find_already_bought_ticket(self, id: int):
        with open("Events.json", "r", encoding="utf-8") as file:
            bought_tickets = json.load(file)["events"][self.id]["boughtTickets"]
        if str(id) in bought_tickets:
            ticket = bought_tickets[str(id)]
            print(ticket)
        else:
            raise ValueError("No such ticket")

    def create_new_ticket(self, customer: Customer):
        date_difference = (self.date - datetime.now()).days
        if not date_difference > 0:
            raise ValueError("Events has already passed")
        with open("Events.json", "r", encoding="utf-8") as file:
            event_info = json.load(file)
        if event_info["events"][self.id]["ticketsAmount"] <= 0:
            raise ValueError("No tickets for this event left")
        event_info["events"][self.id]["ticketsAmount"] -= 1
        with open("Events.json", "w", encoding="utf-8") as file:
            json.dump(event_info, file)
        if customer.type == "Student":
            return StudentTicket(self.id)
        elif date_difference >= 60:
            return AdvanceTicket(self.id)
        elif date_difference <= 10:
            return LateTicket(self.id)
        else:
            return RegularTicket(self.id)


class Ticket:

    def __init__(self, event_id):
        with open("Events.json", "r", encoding="utf-8") as file:
            event_info = json.load(file)
        event_info["events"][event_id]["boughtTickets"]["amount"] += 1
        self.id = event_info["events"][event_id]["boughtTickets"]["amount"]
        with open("Events.json", "w", encoding="utf-8") as file:
            json.dump(event_info, file)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError("Wrong ticket_id type")
        self.__id = value


class StudentTicket(Ticket):

    def __init__(self, event_id):
        super().__init__(event_id)
        with open("Events.json", "r", encoding="utf-8") as file:
            event = json.load(file)["events"][event_id]
        self.price = event["ticketPrice"]*event["discounts"]["studentTicket"]

    def __str__(self):
        return f"Ticket: {self.id} \nPrice: {self.price}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Wrong ticket_price type")
        if not value > 0:
            raise ValueError("Wrong ticker_price value")
        self.__price = value


class AdvanceTicket(Ticket):

    def __init__(self, event_id):
        super().__init__(event_id)
        with open("Events.json", "r", encoding="utf-8") as file:
            event = json.load(file)["events"][event_id]
        self.price = event["ticketPrice"] * event["discounts"]["advanceTicket"]

    def __str__(self):
        return f"Ticket: {self.id} \nPrice: {self.price}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Wrong ticket_price type")
        if not value > 0:
            raise ValueError("Wrong ticker_price value")
        self.__price = value


class LateTicket(Ticket):

    def __init__(self, event_id):
        super().__init__(event_id)
        with open("Events.json", "r", encoding="utf-8") as file:
            event = json.load(file)["events"][event_id]
        self.price = event["ticketPrice"] * event["discounts"]["lateTicket"]

    def __str__(self):
        return f"Ticket: {self.id} \nPrice: {self.price}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Wrong ticket_price type")
        if not value > 0:
            raise ValueError("Wrong ticker_price value")
        self.__price = value


class RegularTicket(Ticket):

    def __init__(self, event_id):
        super().__init__(event_id)
        with open("Events.json", "r", encoding="utf-8") as file:
            event = json.load(file)["events"][event_id]
        self.price = event["ticketPrice"]

    def __str__(self):
        return f"Ticket: {self.id} \nPrice: {self.price}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError("Wrong ticket_price type")
        if not value > 0:
            raise ValueError("Wrong ticker_price value")
        self.__price = value


class Payment:
    @staticmethod
    def buy_ticket(customer: Customer, event: Event):
        ticket = event.create_new_ticket(customer)
        with open("Events.json", "r", encoding="utf-8") as file:
            event_info = json.load(file)
        if not event_info["events"][event.id]["boughtTickets"]:
            event_info["events"][event.id]["boughtTickets"] = {}
        if str(ticket.id) not in event_info["events"][event.id]["boughtTickets"]:
            event_info["events"][event.id]["boughtTickets"][str(ticket.id)] = {}
        event_info["events"][event.id]["boughtTickets"][str(ticket.id)]["name"] = customer.name
        event_info["events"][event.id]["boughtTickets"][str(ticket.id)]["surname"] = customer.surname
        event_info["events"][event.id]["boughtTickets"][str(ticket.id)]["price"] = ticket.price
        event_info["events"][event.id]["boughtTickets"][str(ticket.id)]["purchase_date"] = str(datetime.now())
        with open("Events.json", "w") as file:
            json.dump(event_info, file, indent=4)


event1 = Event(2)
customer1 = Customer("Oleksandr", "Kalenskyi", "Regular")
customer2 = Customer("Zahar", "Domnenko", "Student")
payment_process = Payment()
payment_process.buy_ticket(customer2, event1)
event1.find_already_bought_ticket(2)

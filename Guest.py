# guest.py
from typing import List


class Guest:
    """
    Represents a hotel guest with name, contact info, loyalty status, and reservation history.
    """
    def __init__(self, name: str, contact_info: str, loyalty_status: str = "Regular"):
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_status = loyalty_status
        self.__reservations: List = []


    # Getter methods
    def get_name(self) -> str:
        return self.__name


    def get_loyalty_status(self) -> str:
        return self.__loyalty_status


    def get_reservations(self) -> List:
        return self.__reservations


    def get_guest_info(self) -> str:
        return (f"Guest: {self.__name}, Contact: {self.__contact_info}, "
                f"Loyalty Status: {self.__loyalty_status}")


    # Setter method
    def set_loyalty_status(self, status: str):
        self.__loyalty_status = status


    # Add booking to reservation history
    def add_reservation(self, booking) -> None:
        self.__reservations.append(booking)


    def __str__(self):
        return self.get_guest_info()

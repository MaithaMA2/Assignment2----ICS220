# room.py
class Room:
    """
    Represents a hotel room with room number, type, amenities, price, and availability status.
    """
    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__availability = True  # Room is available by default


    # Getter methods
    def get_room_number(self) -> int:
        return self.__room_number


    def get_price(self) -> float:
        return self.__price_per_night


    def is_available(self) -> bool:
        return self.__availability


    def get_room_info(self) -> str:
        return (f"Room {self.__room_number} - {self.__room_type}, "
                f"Price: ${self.__price_per_night:.2f}, "
                f"Amenities: {', '.join(self.__amenities)}, "
                f"Available: {self.__availability}")


    # Setter method
    def set_price(self, new_price: float):
        self.__price_per_night = new_price


    # Change room status
    def book_room(self) -> bool:
        if self.__availability:
            self.__availability = False
            return True
        return False


    def release_room(self):
        self.__availability = True


    def __str__(self):
        return self.get_room_info()

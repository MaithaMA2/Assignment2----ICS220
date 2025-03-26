# booking.py
class Booking:
    """
    Manages the reservation process for a guest and a room.
    """
    def __init__(self, booking_id: int, guest, room, check_in: str, check_out: str):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        self.__status = "Confirmed" if room.book_room() else "Failed"


    # Cancel booking and release the room
    def cancel_booking(self):
        self.__status = "Cancelled"
        self.__room.release_room()


    # Getter
    def get_status(self) -> str:
        return self.__status


    def __str__(self):
        return (f"Booking ID: {self.__booking_id}, Guest: {self.__guest.get_name()}, "
                f"Room: {self.__room.get_room_number()}, Dates: {self.__check_in} to {self.__check_out}, "
                f"Status: {self.__status}")

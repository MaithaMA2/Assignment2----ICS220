# hotel_services.py
class HotelServices:
    """
    Manages service requests made by a guest.
    """
    def __init__(self, service_id: int, guest, request: str):
        self.__service_id = service_id
        self.__guest = guest
        self.__request = request
        self.__status = "Pending"


    # Complete the service request
    def complete_service(self):
        self.__status = "Completed"


    def __str__(self):
        return (f"Service ID: {self.__service_id}, Guest: {self.__guest.get_name()}, "
                f"Request: {self.__request}, Status: {self.__status}")

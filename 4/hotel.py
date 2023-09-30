# Задание №4
# Вам необходимо написать тест с использованием моков для сервиса бронирования отелей.
# Условие: У вас есть класс HotelService с методом public boolean isRoomAvailable(int roomId),
# который обычно проверяет, доступен ли номер в отеле.
# Вам необходимо проверить правильность работы класса BookingService, который
# использует HotelService для бронирования номера, если он доступен.

import random


class HotelService:
    def is_room_available(self, room_id: int):
        return random.choice([True, False])
    
    
class BookingService:
    def __init__(self, hotelservice: HotelService) -> None:
        self._hotel_service = hotelservice
        
    @property
    def hotel_service(self):
        return self._hotel_service
    
    def book_room(self, room_id) -> str:
        if self._hotel_service.is_room_available(room_id):
            return f'Комната номер {room_id} свободна'
        return f'Комната {room_id} уже забронирована'

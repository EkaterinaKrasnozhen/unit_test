import unittest
from unittest.mock import Mock
from unittest.mock import patch
from hotel import BookingService


class TestHotel(unittest.TestCase):
    @patch('hotel.HotelService')
    def test_book_room(self, mock_hotel):
        self.booking_service = BookingService(mock_hotel)
        room_id = 6
        self.booking_service.book_room(room_id)  
        self.booking_service.hotel_service.is_room_available.assert_called_once_with(room_id)  
        
        
if __name__ == '__main__':
    unittest.main()
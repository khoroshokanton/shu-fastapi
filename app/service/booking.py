from app.core.service import BaseService
from app.models import Booking


class BookingService(BaseService):
    model = Booking

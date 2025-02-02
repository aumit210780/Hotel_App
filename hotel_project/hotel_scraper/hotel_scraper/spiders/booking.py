import scrapy
from hotel_app.models import Hotel

class BookingSpider(scrapy.Spider):
    name = 'booking'
    allowed_domains = ['booking.com']
    start_urls = ['https://www.booking.com/']

    def __init__(self, city=None, *args, **kwargs):
        super(BookingSpider, self).__init__(*args, **kwargs)
        self.city = city  # Pass the city parameter to the spider

    def parse(self, response):
        # Example: Extract hotel data from Booking.com
        hotel = Hotel(
            name=response.css('div.hotel-name::text').get(),
            city=self.city,  # Use the city passed from Django
            price=response.css('div.price::text').get(),
            star_rating=response.css('div.stars::attr(data-rating)').get(),
            image_url=response.css('img.hotel-image::attr(src)').get(),
            booking_url=response.url,
            source="Booking.com"
        )
        hotel.save()

import scrapy
from hotel_app.models import Hotel

class AgodaSpider(scrapy.Spider):
    name = 'agoda'
    allowed_domains = ['agoda.com']
    start_urls = ['https://www.agoda.com/']

    def __init__(self, city=None, *args, **kwargs):
        super(AgodaSpider, self).__init__(*args, **kwargs)
        self.city = city  # Pass the city parameter to the spider

    def parse(self, response):
        # Example: Extract hotel data from Agoda
        hotel = Hotel(
            name=response.css('div.hotel-name::text').get(),
            city=self.city,  # Use the city passed from Django
            price=response.css('div.price::text').get(),
            star_rating=response.css('div.stars::attr(data-rating)').get(),
            image_url=response.css('img.hotel-image::attr(src)').get(),
            booking_url=response.url,
            source="Agoda"
        )
        hotel.save()
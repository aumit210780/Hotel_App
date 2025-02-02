from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from hotel_scraper.hotel_scraper.spiders.booking import BookingSpider
from hotel_scraper.hotel_scraper.spiders.agoda import AgodaSpider

def run_spiders(city):
    """
    Run Scrapy spiders to scrape hotel data for the given city.
    """
    # Configure Scrapy settings
    settings = get_project_settings()
    settings.set('FEED_FORMAT', 'json')
    settings.set('FEED_URI', 'hotels.json')  # Save scraped data to a JSON file

    # Initialize the Scrapy process
    process = CrawlerProcess(settings)

    # Run the Booking.com spider
    process.crawl(BookingSpider, city=city)

    # Run the Agoda spider
    process.crawl(AgodaSpider, city=city)

    # Start the Scrapy process
    process.start()
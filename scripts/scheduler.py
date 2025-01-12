import schedule
import time
import logging
from pathlib import Path
from datetime import datetime
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from scraper import PriceScraper

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)

class ScraperScheduler:
    def __init__(self, urls, interval_hours=24):
        """
        Initialize the scheduler
        :param urls: List of URLs to scrape
        :param interval_hours: Interval between scrapes in hours
        """
        self.urls = urls
        self.interval_hours = interval_hours
        self.setup_directories()

    def setup_directories(self):
        """Create necessary directories for data and logs"""
        Path('data').mkdir(exist_ok=True)
        Path('logs').mkdir(exist_ok=True)

    def scrape_job(self):
        """Execute scraping job for all configured URLs"""
        job_start_time = datetime.now()
        logging.info(f"Starting scraping job at {job_start_time}")

        for url in self.urls:
            try:
                logging.info(f"Processing URL: {url}")
                scraper = PriceScraper(url)
                
                # Generate filename with timestamp
                timestamp = datetime.now().strftime('%Y%m%d')
                filename = f"data/prices_{timestamp}.csv"
                
                # Run scraper
                scraper.run()
                logging.info(f"Successfully scraped data from {url}")
                
            except Exception as e:
                logging.error(f"Error scraping {url}: {e}")
                continue

        job_end_time = datetime.now()
        duration = (job_end_time - job_start_time).total_seconds()
        logging.info(f"Completed scraping job. Duration: {duration} seconds")

    def start(self):
        """Start the scheduler"""
        # Schedule job
        schedule.every(self.interval_hours).hours.do(self.scrape_job)
        
        # Run job immediately on start
        self.scrape_job()
        
        logging.info(f"Scheduler started. Will run every {self.interval_hours} hours")
        
        # Keep the script running
        while True:
            try:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
            except KeyboardInterrupt:
                logging.info("Scheduler stopped by user")
                break
            except Exception as e:
                logging.error(f"Scheduler error: {e}")
                # Wait before retrying
                time.sleep(300)  # 5 minutes

def main():
    # Configure target URLs
    urls = [
        "https://example.com/products",
        # Add more URLs as needed
    ]
    
    # Create and start scheduler
    scheduler = ScraperScheduler(urls)
    scheduler.start()

if __name__ == "__main__":
    main()
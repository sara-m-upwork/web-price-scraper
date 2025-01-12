import os
import csv
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

class PriceScraper:
    def __init__(self, url):
        self.url = url
        self.setup_driver()
        
    def setup_driver(self):
        """Configure Chrome driver with appropriate options"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def get_page_content(self):
        """Load page and get its content"""
        try:
            self.driver.get(self.url)
            # Wait for price elements to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "price"))
            )
            return self.driver.page_source
        except Exception as e:
            print(f"Error loading page: {e}")
            return None
            
    def parse_prices(self, html_content):
        """Parse prices from HTML content"""
        soup = BeautifulSoup(html_content, 'html.parser')
        products = []
        
        # Find all product containers
        for item in soup.find_all('div', class_='product'):
            try:
                name = item.find('h2', class_='product-name').text.strip()
                price = item.find('span', class_='price').text.strip()
                # Remove currency symbol and convert to float
                price_value = float(price.replace('₩', '').replace(',', '').strip())
                
                products.append({
                    'name': name,
                    'price': price_value,
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                })
            except Exception as e:
                print(f"Error parsing product: {e}")
                continue
                
        return products
        
    def save_to_csv(self, products, filename='price_data.csv'):
        """Save scraped data to CSV file"""
        file_exists = os.path.isfile(filename)
        
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'price', 'timestamp'])
            
            if not file_exists:
                writer.writeheader()
                
            writer.writerows(products)
            
    def run(self):
        """Execute the complete scraping process"""
        try:
            html_content = self.get_page_content()
            if html_content:
                products = self.parse_prices(html_content)
                if products:
                    self.save_to_csv(products)
                    print(f"Successfully scraped {len(products)} products")
                else:
                    print("No products found")
        except Exception as e:
            print(f"Error during scraping: {e}")
        finally:
            self.driver.quit()

def main():
    # Example usage
    url = "https://example.com/products"  # Replace with target website
    scraper = PriceScraper(url)
    scraper.run()

if __name__ == "__main__":
    main()
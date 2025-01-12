# Web Price Scraper

An automated web scraping system that collects price information from websites and stores it in a structured format. Built with Python, Selenium, and BeautifulSoup4.

## Features

- 🤖 Automated price data collection
- 📊 CSV data export with timestamps
- ⏰ Scheduled scraping at customizable intervals
- 📝 Comprehensive logging system
- 🔄 Error handling and retry mechanism
- 🎯 Multi-URL support
- 🚀 Headless browser operation

## Project Structure

```
web-price-scraper/
├── src/
│   ├── scraper.py      # Core scraping logic
│   └── config.py       # Configuration management
├── scripts/
│   └── scheduler.py    # Automated scheduling
├── data/               # Scraped data storage
├── logs/               # Log files
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── .gitignore         # Git ignore rules
```

## Prerequisites

- Python 3.8 or higher
- Chrome browser
- ChromeDriver matching your Chrome version

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/web-price-scraper.git
cd web-price-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy and configure environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

## Configuration

Configure the scraper by editing the `.env` file:

```plaintext
CHROME_DRIVER_PATH=/path/to/chromedriver
SCRAPE_INTERVAL=24
LOG_LEVEL=INFO
DATA_DIR=./data
LOG_DIR=./logs
```

## Usage

### Single Scraping Run

To perform a single scraping run:

```bash
python src/scraper.py
```

### Automated Scheduling

To start the automated scheduler:

```bash
python scripts/scheduler.py
```

The scheduler will:
- Run immediately upon starting
- Continue running at specified intervals (default: 24 hours)
- Save data to CSV files with timestamps
- Maintain detailed logs

## Data Format

The scraper stores data in CSV format with the following structure:

```csv
name,price,timestamp
Product A,29.99,2024-01-12 14:30:00
Product B,49.99,2024-01-12 14:30:00
```

## Logging

Logs are stored in the `logs` directory with the following information:
- Scraping start/end times
- Number of products scraped
- Any errors or warnings
- Processing duration

## Error Handling

The system includes robust error handling:
- Automatic retries for failed requests
- Detailed error logging
- Graceful failure recovery
- Session cleanup

## License

This project is licensed under the MIT License

## Acknowledgments

- Selenium Documentation
- BeautifulSoup4 Documentation
- Python Schedule Library
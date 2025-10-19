# Web Scraping Job Site Project

A Python web scraping project that extracts job listings from a sample website, demonstrating the use of BeautifulSoup4 for HTML parsing.

## Tutorial Reference
This project follows the Real Python tutorial:
["Beautiful Soup: Build a Web Scraper With Python"](https://realpython.com/beautiful-soup-web-scraper-python/)

Original tutorial: [https://realpython.com/beautiful-soup-web-scraper-python/](https://realpython.com/beautiful-soup-web-scraper-python/)

## Project Structure
```
webScrapingJobSite/
├── README.md
├── scraper.ipynb      # Jupyter notebook with documented code
├── hello.py          # Python script version
└── .venv/           # Python virtual environment
```

## Features
- Fetches job listings from a sample website
- Parses HTML content using BeautifulSoup4
- Filters for Python-related job positions
- Extracts job details including:
  - Job titles
  - Company names
  - Locations
  - Application links

## Requirements
- Python 3.x
- requests
- beautifulsoup4

## Setup
1. Clone or download this repository
2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

3. Install required packages:
```bash
pip install requests beautifulsoup4
```

## Usage
You can run the scraper in two ways:

### Using the Jupyter Notebook
1. Open `scraper.ipynb` in VS Code or Jupyter
2. Run cells sequentially to see the scraping process step by step

### Using the Python Script
```bash
python hello.py
```

## Code Structure
- Fetches webpage content using `requests`
- Creates a BeautifulSoup object to parse HTML
- Finds job listings container by ID
- Extracts job details from card elements
- Filters for Python-specific positions
- Retrieves application and learning resource links

## Tutorial Reference
The code is based on the Real Python tutorial which covers:
- Basic web scraping concepts
- HTML parsing with BeautifulSoup
- Finding elements by ID and class
- Extracting text and attributes
- Navigating HTML structure
- Filtering content

## License
This project is created for educational purposes, following the Real Python tutorial.
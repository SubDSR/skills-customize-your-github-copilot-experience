# 📘 Assignment: Web Scraping with Beautiful Soup

## 🎯 Objective

Learn how to extract and parse data from websites using Python's Beautiful Soup library and HTTP requests. You'll build a web scraper that collects real-world data, processes it, and stores it for analysis.

## 📝 Tasks

### 🛠️ Task 1: Set Up and Fetch Web Content

#### Description
Write a Python program that fetches HTML content from a website using the `requests` library and parses it with Beautiful Soup. Start by scraping a simple, public website to understand the structure of HTML and how to navigate it.

#### Requirements
Completed program should:

- Install and import the `requests` and `beautifulsoup4` libraries
- Use `requests.get()` to fetch a website's HTML content
- Parse the HTML with `BeautifulSoup`
- Print the formatted HTML to understand its structure
- Include error handling for network requests (try/except blocks)

### 🛠️ Task 2: Extract Specific Data

#### Description
Identify specific HTML elements (tags, classes, IDs) on the page and extract meaningful data such as titles, links, prices, or descriptions. Use Beautiful Soup's selection methods to find and extract the information.

#### Requirements
Completed program should:

- Identify and extract at least 3 different data elements from the website
- Use methods like `find()`, `find_all()`, and CSS selectors (`.select()`)
- Store extracted data in a structured format (list or dictionary)
- Print or display the extracted data in a readable format
- Handle cases where elements might be missing

### 🛠️ Task 3: Save and Analyze Scraped Data

#### Description
Save the scraped data to a CSV file or JSON file so it can be analyzed or imported elsewhere. Add basic data processing to demonstrate understanding of the collected information.

#### Requirements
Completed program should:

- Save scraped data to a CSV or JSON file
- Include headers or structure appropriate to the data
- Count or aggregate the data in some way (e.g., number of items, categories)
- Display summary statistics or insights
- Be reusable (function-based approach for scraping)


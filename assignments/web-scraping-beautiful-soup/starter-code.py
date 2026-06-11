"""
Web Scraping with Beautiful Soup - Starter Code

This starter code provides a foundation for building a web scraper
that extracts data from websites and saves it for analysis.
"""

import requests
from bs4 import BeautifulSoup
import csv
import json

# TODO: Task 1 - Set Up and Fetch Web Content
def fetch_webpage(url):
    """
    Fetch HTML content from a website.
    
    Args:
        url (str): The URL of the website to scrape
        
    Returns:
        BeautifulSoup: Parsed HTML content, or None if request fails
    """
    try:
        # TODO: Use requests.get() to fetch the webpage
        # TODO: Add headers to make the request look like a real browser
        # TODO: Check for successful status code (200)
        # TODO: Parse with BeautifulSoup and return
        pass
    except requests.exceptions.RequestException as e:
        # TODO: Handle network errors
        print(f"Error fetching the webpage: {e}")
        return None


# TODO: Task 2 - Extract Specific Data
def extract_data(soup):
    """
    Extract specific data from the parsed HTML.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        
    Returns:
        list: List of dictionaries containing extracted data
    """
    data = []
    
    # TODO: Use soup.find_all() or soup.select() to find elements
    # TODO: Extract at least 3 different pieces of information per item
    # TODO: Handle missing elements gracefully
    # TODO: Store data in a list of dictionaries
    
    return data


# TODO: Task 3 - Save and Analyze Data
def save_to_csv(data, filename):
    """
    Save scraped data to a CSV file.
    
    Args:
        data (list): List of dictionaries to save
        filename (str): Name of the output CSV file
    """
    if not data:
        print("No data to save.")
        return
    
    try:
        # TODO: Get the keys from the first dictionary as headers
        # TODO: Open the file in write mode
        # TODO: Use csv.DictWriter to write the data
        pass
    except Exception as e:
        print(f"Error saving to CSV: {e}")


def save_to_json(data, filename):
    """
    Save scraped data to a JSON file.
    
    Args:
        data (list): List of dictionaries to save
        filename (str): Name of the output JSON file
    """
    try:
        # TODO: Write data to JSON file with proper formatting
        pass
    except Exception as e:
        print(f"Error saving to JSON: {e}")


def analyze_data(data):
    """
    Analyze and display summary statistics about the scraped data.
    
    Args:
        data (list): List of dictionaries containing the scraped data
    """
    if not data:
        print("No data to analyze.")
        return
    
    # TODO: Count total items
    # TODO: Display any patterns or interesting statistics
    # TODO: Show data in a readable format
    
    print(f"Total items scraped: {len(data)}")


# Main execution
if __name__ == "__main__":
    # TODO: Change this to the URL you want to scrape
    url = "https://example.com"
    
    print(f"Fetching {url}...")
    soup = fetch_webpage(url)
    
    if soup:
        print("Extracting data...")
        data = extract_data(soup)
        
        if data:
            print("Saving data...")
            save_to_csv(data, "scraped_data.csv")
            save_to_json(data, "scraped_data.json")
            
            print("Analyzing data...")
            analyze_data(data)
        else:
            print("No data was extracted.")
    else:
        print("Failed to fetch the webpage.")

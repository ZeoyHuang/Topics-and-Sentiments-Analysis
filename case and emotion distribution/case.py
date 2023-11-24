# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:01:49 2023

@author: Hzy
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta

# URL to the Health Commission's daily epidemic notification page
base_url = "http://example.com/epidemic/notification?page="

# Function to parse a single page of epidemic data
def parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Below line is a placeholder and needs to be replaced with actual data extraction logic.
    data = soup.find_all('tag', {'class': 'className'})
    return data

# Function to write data to CSV
def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Number of New Confirmed Cases'])
        for entry in data:
            writer.writerow(entry)

# Crawling data between the dates
start_date = datetime(2022, 3, 1)
end_date = datetime(2022, 4, 30)
current_date = start_date

# Loop through the range of dates and pages (if pagination is there)
all_data = []
while current_date <= end_date:
    formatted_date = current_date.strftime('%Y-%m-%d')
    # Assuming each day's data is on a separate page, you would update the page URL here
    page_url = base_url + str(current_date.day)
    daily_data = parse_page(page_url)
    all_data.append([formatted_date] + daily_data)  # Combine date with data
    current_date += timedelta(days=1)

# Write all data to CSV
write_to_csv(all_data, 'case.csv')
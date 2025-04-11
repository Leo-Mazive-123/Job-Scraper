import time
import logging
import pandas as pd
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_jobs():
    logging.info("Scraping started...")

    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://vacancymail.co.zw/jobs/")

        job_data = []

        job_cards = driver.find_elements(By.CLASS_NAME, "job-listing")

        for job in job_cards[:10]:  # Only top 10 jobs
            try:
                title = job.find_element(By.CLASS_NAME, "job-listing-title").text
                company = job.find_element(By.CLASS_NAME, "job-listing-company").text
                description = job.find_element(By.CLASS_NAME, "job-listing-text").text

                # Footer fields
                footer_items = job.find_elements(By.CSS_SELECTOR, ".job-listing-footer ul li")
                location = ""
                expiry_date = ""

                for item in footer_items:
                    text = item.text.strip()
                    if "Expires" in text:
                        expiry_date = text.replace("Expires", "").strip()
                    elif not location and any(city in text for city in ["Harare", "Bulawayo", "Mutare", "Gweru", "Chitungwiza", "Masvingo"]):
                        location = text

                job_data.append({
                    "Title": title,
                    "Company": company,
                    "Location": location,
                    "Expiry Date": expiry_date,
                    "Description": description
                })

            except Exception as e:
                logging.warning(f"Error parsing a job listing: {e}")

        df = pd.DataFrame(job_data)

        # Clean and save data
        df.drop_duplicates(inplace=True)
        df.to_csv("scraped_data.csv", index=False)
        logging.info("✅ Data saved to scraped_data.csv")

        driver.quit()

    except Exception as e:
        logging.error(f"Scraping failed: {e}")

    logging.info("Scraping finished.\n")

# Run immediately and schedule every 2 minutes for demo/testing
scrape_jobs()
schedule.every(2).minutes.do(scrape_jobs)

logging.info("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)

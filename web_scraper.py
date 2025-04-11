import time
import logging
import pandas as pd
import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def scrape_jobs():
    logging.info("Scraping started...")
    start_time = time.time()

    try:
        # Setup headless browser with image loading disabled
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--blink-settings=imagesEnabled=false")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://vacancymail.co.zw/jobs/")

        driver.implicitly_wait(5)  # Optional wait

        job_data = []
        job_cards = driver.find_elements(By.CLASS_NAME, "job-listing")

        for job in job_cards[:10]:  # Top 10 jobs
            try:
                title = job.find_element(By.CLASS_NAME, "job-listing-title").text
            except:
                title = ""

            try:
                company = job.find_element(By.CLASS_NAME, "job-listing-company").text
            except:
                company = ""

            try:
                description = job.find_element(By.CLASS_NAME, "job-listing-text").text
            except:
                description = ""

            # Footer fields
            location = ""
            expiry_date = ""
            try:
                footer_items = job.find_elements(By.CSS_SELECTOR, ".job-listing-footer ul li")
                for item in footer_items:
                    text = item.text.strip()
                    if "Expires" in text:
                        expiry_date = text.replace("Expires", "").strip()
                    elif not location and any(city in text for city in ["Harare", "Bulawayo", "Mutare", "Gweru", "Chitungwiza", "Masvingo"]):
                        location = text
            except:
                pass

            if title:  # Only save if title is present
                job_data.append({
                    "Title": title,
                    "Company": company,
                    "Location": location,
                    "Expiry Date": expiry_date,
                    "Description": description
                })
            else:
                logging.warning("⚠️ Skipped a job listing due to missing title.")

        # Save data
        df = pd.DataFrame(job_data)
        df.drop_duplicates(inplace=True)
        df.to_csv("scraped_data.csv", index=False)
        logging.info(f"✅ {len(df)} job(s) scraped.")
        logging.info("✅ Data saved to scraped_data.csv")

        driver.quit()

    except Exception as e:
        logging.error(f"❌ Scraping failed: {e}")

    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"⏱️ Scraping finished in {duration:.2f} seconds.\n")

# Run immediately and every 2 mins (for demo)
scrape_jobs()
schedule.every(2).minutes.do(scrape_jobs)

logging.info("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)

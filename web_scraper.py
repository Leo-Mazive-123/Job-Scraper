from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")

# Start the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the website
print("Scraping started...\n")
driver.get("https://vacancymail.co.zw/jobs/")

try:
    # Wait until job titles are present
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-listing-title"))
    )

    # Find all job title elements
    job_titles = driver.find_elements(By.CLASS_NAME, "job-listing-title")

    print("Job Titles Found:\n")
    for job in job_titles:
        print("-", job.text)

except Exception as e:
    print("Error extracting job titles:", e)

# Close the driver
driver.quit()
print("\nScraping finished.")

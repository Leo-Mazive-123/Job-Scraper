✅ Final README.md (Ready to Submit)

# 🕷️ Python Job Scraper & Data Aggregator

> A Python-based web scraper that automates the process of collecting the **10 most recent job listings** from [VacancyMail Zimbabwe](https://vacancymail.co.zw/jobs/), saves them in structured CSV format, and supports scheduled scraping and logging.

---

## 📌 Project Objective

This project was developed as part of a Python crash course. It reinforces programming fundamentals while exploring practical applications like:

- Web scraping
- Data handling using `pandas`
- Task scheduling with `schedule`
- Automation & error logging

---

## 📥 Extracted Data

For each job listing, the scraper extracts:

- 🧑‍💼 **Job Title**
- 🏢 **Company**
- 📍 **Location**
- 🗓️ **Expiry Date**
- 📝 **Job Description**

---

## 📁 Output File

Scraped data is saved to:

```plaintext
scraped_data.csv
This file contains a structured tabular format of job listings.

🛠️ Setup Instructions
1. Clone the Repository

git clone https://github.com/yourusername/job-scraper.git
cd job-scraper

2. Create a Virtual Environment

python -m venv .venv
.venv\Scripts\activate   # Windows
# OR
source .venv/bin/activate   # macOS/Linux

3. Install Dependencies

pip install -r requirements.txt
Or manually:

pip install selenium pandas schedule webdriver-manager

🚀 Usage
To run the scraper manually:

python web_scraper.py
The script will:

Launch a headless browser

Scrape the 10 latest jobs

Save them to scraped_data.csv

Log events and errors to scraper.log

⏰ Scheduling
Scraping can be scheduled to run at regular intervals using the schedule module.
You can modify this line in web_scraper.py:

python

schedule.every(6).hours.do(scrape_jobs)
Change .hours to .minutes or .day as needed.

⚙️ Project Structure

job-scraper/
├── web_scraper.py         # Main script
├── requirements.txt       # Python dependencies
├── scraped_data.csv       # Output file
├── scraper.log            # Logging output
└── README.md              # You're reading it!
🧠 Implementation Notes
Scraping Engine: Built using Selenium for dynamic rendering.

Driver Management: Handled by webdriver-manager (no manual downloads).

Error Handling: Parsing and connection failures are caught and logged.

Logging: All events and warnings are written to scraper.log.

🧪 Sample Output Preview
Job Title	Company	Location	Expiry Date	Description
Software Engineer	ABC Ltd	Harare	2025-04-30	Develop and maintain systems...
Marketing Officer	XYZ Marketing	Bulawayo	2025-04-28	Create campaigns and analyze...



👨‍💻 Author
Leo T. Mazive
Python Automation | Web Scraping
Course Project - Crash Program 2025

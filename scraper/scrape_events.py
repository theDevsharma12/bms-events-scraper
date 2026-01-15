from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

URL = "https://in.bookmyshow.com/explore/events-jaipur"

def scrape_events():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    )

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(6)

    events = []

    cards = driver.find_elements(By.CSS_SELECTOR, "a[class*='EventCard']")

    for card in cards:
        try:
            name = card.find_element(By.TAG_NAME, "h3").text
            date = card.find_element(By.CSS_SELECTOR, "div[class*='date']").text
            venue = card.find_element(By.CSS_SELECTOR, "div[class*='venue']").text
            link = card.get_attribute("href")

            events.append({
                "Event Name": name,
                "Date": date,
                "Venue": venue,
                "Link": link
            })
        except:
            continue

    driver.quit()
    return events

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from notifypy import Notify

# Notification setup
notification = Notify()
notification.title = "Extracting Data"
notification.message = "Extracting data from Amazon"
notification.send()

# Create an instance of Options
chrome_options = Options()

# Adding proxy-server argument to the options
chrome_options.add_argument("--proxy-server=gate.nodemaven.com:8080")

# Setting user-agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={user_agent}")

# Initialize the Chrome WebDriver with options (make sure options is lowercase)
driver = webdriver.Chrome(options=chrome_options)

# Opening the products file and reading its contents
with open("products.txt") as f:
    products = f.readlines()

    i = 0
    for product in products:
        driver.get(product.strip())  # Strip the newline from each product URL
        i += 1
        page_source = driver.page_source

        # Save the page source in separate HTML files
        with open(f"data/{i}.html", "w", encoding="utf-8") as f_out:
            f_out.write(page_source)

# Placeholder for data extraction function
def extract_data():
    pass

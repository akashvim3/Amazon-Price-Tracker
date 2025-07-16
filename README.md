# Amazon Price Tracker

A **Python-based Amazon Price Tracker** that monitors the prices of products on Amazon and notifies you when they drop below your desired threshold. This tool is great for bargain hunters and anyone who wants to get the best deal on Amazon!

## Features

- Track prices of one or multiple Amazon products.
- Set your own target price for each product.
- Receive notifications (via email, push notification, or console) when prices drop.
- Easy to use and configure (no coding experience required).
- Supports scheduling with cron or Windows Task Scheduler.
- Clean, high-level Python code using popular libraries.

## How It Works

1. **Add product URLs and target prices** to a configuration file.
2. The script fetches the current price for each product using web scraping.
3. If the price drops below your target, you get notified.
4. Run the script manually or schedule it to run automatically.

## Requirements

- Python 3.8 or higher
- `requests`
- `beautifulsoup4`
- `lxml` (optional, for faster parsing)
- `smtplib` (for email notifications)

Install dependencies using:

```bash
pip install requests beautifulsoup4 lxml
```

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/akashvim3/amazon-price-tracker.git
cd amazon-price-tracker
```

### 2. Configure Your Products

Create or edit a `products.json` file in the project directory:

```json
[
  {
    "url": "https://www.amazon.com/dp/B09G9F5C7Q",
    "target_price": 199.99
  },
  {
    "url": "https://www.amazon.com/dp/B07FZ8S74R",
    "target_price": 499.00
  }
]
```

### 3. Set Up Notification (Optional)

- For **email notifications**, configure your SMTP settings in `config.py`.
- For basic usage, the script will print notifications to the console.

### 4. Run the Tracker

```bash
python amazon_price_tracker.py
```

### 5. Automate (Optional)

- Use `cron` (Linux/macOS) or Task Scheduler (Windows) to run the script periodically.

## Example Code (High-Level)

```python
import requests
from bs4 import BeautifulSoup

def get_price(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    price = soup.find(id="priceblock_ourprice")
    return float(price.text.replace("$", "").replace(",", ""))

def notify(product, current_price):
    print(f"Price drop! {product['url']} is now ${current_price}")

# Load products from products.json and check their prices
```

## Disclaimer

- This tool is for educational purposes.
- Scraping Amazon may violate their Terms of Service.
- Amazon may change their website structure, which can break the script.

## License

MIT License

---

**Happy tracking!**

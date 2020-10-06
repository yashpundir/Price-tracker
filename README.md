# Price-tracker
### E-commerce product price tracker and notifier
Python script that tracks your e-commerce products for you. Give in the name of the product, name of the website, URL of the product
and the script will track the product and its price from that day onwards.
The source.py script is deployed on heroku, which scrapes of the prices of the products that the user has listed, everyday at 01:00 PM
and stores the prices in Google Spreadsheets.
If the price of any particular product drops in future, the user is notified through a WhatsApp message about the same.

The APIs that are used :

1) Google Sheets API (Google Developers Console)
2) Google Drive API (Google Developers Console)
3) Twilio API (WhatsApp)

The websites that are currently supported :

1) https://www.amazon.in/
2) https://www.flipkart.com/

Might add more websites soon :smiley:

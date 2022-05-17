# casvenmo

This is a script I wrote to automatically add new venmo transactions to a google spreadsheet. I decided to write this script because of a club I am involved with:
Chinese American Society @ Virginia Tech. During the year, we have members pay dues, as well as event and merchandise costs if they so choose. We take all these payments
through Venmo. In previous years, all payment verification was done manually, by periodically checking the Venmo app/website and typing new transcations into a Google
Sheet. I am planning on running for Treasurer of the club in my sophomore year, and thought that automating this process would make my job much easier. This script can
be run with Windows Task Scheduler to check for updates every day.


**Libraries:**
venmo-api
gspread


**How it Works:**

First, the venmo-api and gspread libraries must be added. Then, using the Google Cloud Platform, both Google Drive and Google Sheets APIs must be enabled.
From the API dashboard, credentials were made and downloaded as 'service_account.json'. Additionally, an access token to view the transactions of the venmo account
is required. Then, I created clients for both Venmo and Google Sheets. Next, I open the specific sheet titled 'venmo_python', and select the page titled 'Payments'.
Then, the last 50 Venmo transactions are obtained using the access token and finding its userID. The resulting data are Transaction objects stored in a list.
I iterated through the list, and evaluate each Transaction object. The sender, receiver, amount paid, and the note are all stored in variables. Next, I needed to 
determine whether or not the transaction was already in the spreadsheet. In order to do this, I used the wks.get_all_records() method which returns a dictionary.
I then put the data of the current transaction into a dictionary temp, and checked to see if they were equivalent. If the transaction did not already exist in the
Google Sheet, the data is put into a list insertion, and it is added through the wks.append_row(insertion). I also added a counter to notify the number of new Venmo
transactions that were added or if none were added.


**Further Development:**

I plan on utlizing keywords to determine the "type" of transaction is being added. Whether it be for club dues, purchasing merchandise, etc.
Additionally, I would like to try implementing a form of verification through the use of our college IDs, 'Hokie Passport'. Members would be able to swipe their card
into a reader, and we would be notified if they have paid their dues for the year.

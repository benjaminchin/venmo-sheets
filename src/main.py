from __future__ import print_function
from venmo_api import Client
import os
import gspread
from dotenv import load_dotenv


def main():

    # load access token and service account environment variables
    load_dotenv()

    # venmo access token
    access_token = os.getenv('ACCESS_TOKEN')

    client = Client(access_token=access_token)  # create venmo client

    sa = gspread.service_account(filename=os.getenv(
        'SERVICE_FILENAME'))  # create google client

    # open google sheet 'venmo_python' and access sheet 'Payments'
    sheet = sa.open('venmo_python')
    wks = sheet.worksheet('Payments')

    me = client.user.get_my_profile()  # get venmo userid
    my_id = me.id

    transactions = client.user.get_user_transactions(
        user_id=my_id, limit=50)  # get last 50 venmo transactions

    sheet_updates = 0
    all_data = wks.get_all_records()
    for t in transactions:
        # data from each venmo transaction
        sender = t.actor.first_name + ' ' + t.actor.last_name
        receiver = t.target.first_name + ' ' + t.target.last_name
        amt = t.amount
        note = t.note

        temp = {'Amount': amt,
                'Note': note,
                'Receiver': receiver,
                'Sender': sender
                }

        already_exists = False

        for dictionary in all_data:  # check if transaction already exists in spreadsheet
            if dictionary == temp:
                already_exists = True
                break

        if not already_exists:  # if the transaction doesn't exist in spreadsheet, add it
            insertion = [receiver, sender, amt, note]
            wks.append_row(insertion)
            sheet_updates += 1

    # notify whether updates have been made to the spreadsheet
    if sheet_updates > 0:
        print(str(sheet_updates) +
              ' new venmo transaction(s) have been added to the sheet.')
    elif sheet_updates == 0:
        print('No new venmo transactions.')


if __name__ == '__main__':
    main()

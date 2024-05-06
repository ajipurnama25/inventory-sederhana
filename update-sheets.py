from __future__ import print_function
from auth import spreadsheet_service
from auth import drive_service

def read_range():

    range_name = 'add stock!A1:H10'  # retrieve data from existing sheet

    spreadsheet_id = '10YgWzGWXBtVvlLRnPyZAZ-xmt0cNZZwRu_23wgqyccw'

    result = spreadsheet_service.spreadsheets().values().get(

    spreadsheetId=spreadsheet_id, range=range_name).execute()

    rows = result.get('values', [])

    print('{0} rows retrieved.'.format(len(rows)))

    print('{0} rows retrieved.'.format(rows))

    return rows

def write_range():

    spreadsheet_id = '10YgWzGWXBtVvlLRnPyZAZ-xmt0cNZZwRu_23wgqyccw'  # get the ID of the existing sheet

    range_name = 'add stock!A2:H2'  # the range to update in the existing sheet

    values = [
        ['Chiki', '90'],  # new row of data
        # ['Goodday', '230'],  # new row of data
        # ['Kecap Manis','260']
        ]  # new row of data

    value_input_option = 'USER_ENTERED'

    body = {

    'values': values

    }

    result = spreadsheet_service.spreadsheets().values().update(

    spreadsheetId=spreadsheet_id, range=range_name,

    valueInputOption=value_input_option, body=body).execute()

    print('{0} cells updated.'.format(result.get('updatedCells')))

if __name__ == '__main__':

    write_range()

    read_range()
from __future__ import print_function

from auth import spreadsheet_service

from auth import drive_service

def read_range():

    range_name = 'add stock!A1:H10'  # read an empty row for new data
    spreadsheet_id = '10YgWzGWXBtVvlLRnPyZAZ-xmt0cNZZwRu_23wgqyccw'

    result = spreadsheet_service.spreadsheets().values().get(

    spreadsheetId=spreadsheet_id, range=range_name).execute()

    rows = result.get('values', [])

    print('{0} rows retrieved.'.format(len(rows)))

    print('{0} rows retrieved.'.format(rows))

    return rows

def write_range():

    spreadsheet_id = '10YgWzGWXBtVvlLRnPyZAZ-xmt0cNZZwRu_23wgqyccw'  # get the ID of the existing sheet

    range_name = 'add harga!A2:H2'  # update the range for three rows

    values = [

        ['Galapagos', '100', '120.000'],  # new row of data
        ['Goodday', '230', '5.000'],  # new row of data
        ['Kecap Manis','260', '8.000']
    ]

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
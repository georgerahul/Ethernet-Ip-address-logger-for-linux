import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheet:

    def __init__(self, credential_json_path, gSheetName):
        self.sheet_name = gSheetName
        self.get_credential(credential_json_path)

    def get_credential(self, credential_json_path):
        """ Get the credential info from the json file for google connection. """
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
            credential_json_path, scope)
        # exception handling pending.

    def connect(self):
        self.gc = gspread.authorize(self.credentials)
        # exception handling pending.

    def get_sheet1(self):
        #gc= self.connect()
        sheet = self.gc.open(self.sheet_name).sheet1
        return sheet

    def make_entry_in_gsheet(self, 
                             row_value, # row value is a list of values to enter. Example ['ubuntu, 'eth0', '192.168.1.100']
                             primary_row_index, # primary index is used to serach for a matching row.( 0 index based). Example [0,1]
                             timestamp_col = 0): # If you need an time stamp entry in your row, enter the col position. (1 based index)
        """ The method will serach in google  sheet whether there is an entry for rows at primary index.
         If present it will update the rows. Else will make a new entry.
         * row_value : is a list of values to enter. Example ['ubuntu, 'eth0', '192.168.1.100']
         * primary index : is used to serach for a matching row.( 0 index based). Example [0,1]
         * timestamp_col : If you need an time stamp entry in your row, enter the col position. (1 based index). Default 0 means no timeStamp added. """

        new_row_location = 2
        worksheet = self.get_sheet1()
        cell_list = worksheet.get_all_values()
        row_found = False

        # Check if primary row values are already available in sheet, then update the information.
        for row in range(len(cell_list)):
            matching_cell_found = True

            # Find rows with matching primary rows
            for col in primary_row_index:
                if cell_list[row][col] != row_value[col] :
                    matching_cell_found = False

            # If mathcing row foudn update the values.
            if matching_cell_found == True :
                row_found = True
                # Get all columns other than primary columns.
                update_columns=list(set(list(range(len(row_value))))- set(primary_row_index))
                for col in update_columns:
                    worksheet.update_cell(row + 1, col+1, row_value[col])
                if timestamp_col != 0: 
                    self.set_timestamp(worksheet, row + 1, timestamp_col)

        # If the host-interface is a new one, add a new host row.
        if row_found == False:            
            worksheet.insert_row(row_value, new_row_location)
            if timestamp_col != 0: 
                self.set_timestamp(worksheet, new_row_location, timestamp_col)

    def set_timestamp(self, worksheet, row, col):
        """ The method will set time stamp when it updates the cell. """
        approach = 1
        if approach == 1:
            # paste Now() equation get the current date time.
            worksheet.update_cell(row, col, '=Now()')

            # time got from Now() is copied to the same cell, removing the equation from the cell.
            worksheet.update_cell(row, col, worksheet.cell(row, col).value)

        elif approach == 2:
            # Get value from a fixed time cell at a cell lets say D1.
            worksheet.update_cell(row, col, worksheet.cell(1, 4).value)

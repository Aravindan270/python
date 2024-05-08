import win32com.client as win32

def copy_excel_data():
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = True

    # Open the source workbook
    wb = excel.Workbooks.Open(r"C:\Users\JK\Downloads\PO AGING Jan FY24 (2) 2.xlsx")

    # Get references to the sheets
    sheet1 = wb.Sheets('Trans FBL3N')
    sheet2 = wb.Sheets('Table EKKN')
    sheet3 = wb.Sheets('Table EKKO')

    # Get the used ranges for each sheet
    sheet1_range = sheet1.UsedRange
    sheet2_range = sheet2.UsedRange
    sheet3_range = sheet3.UsedRange

    # Get the values from the used ranges
    sheet1_data = sheet1_range.Value
    sheet2_data = sheet2_range.Value
    sheet3_data = sheet3_range.Value

    # Add a new workbook
    new_wb = excel.Workbooks.Add()
    new_sheet = new_wb.Sheets(1)

    # Copy data from sheet1
    new_sheet.Range(new_sheet.Cells(1, 1),
                    new_sheet.Cells(sheet1_range.Rows.Count, sheet1_range.Columns.Count)).Value = sheet1_data

    # Copy data from sheet2 with a one-row gap
    new_sheet.Range(new_sheet.Cells(sheet1_range.Rows.Count + 2, 1),
                    new_sheet.Cells(sheet1_range.Rows.Count + sheet2_range.Rows.Count + 2,
                                    sheet2_range.Columns.Count)).Value = sheet2_data

    # Determine the starting row for sheet3 data
    start_row_sheet3 = sheet1_range.Rows.Count + sheet2_range.Rows.Count + 4

    # Determine the starting column for sheet3 data
    start_col_sheet3 = 1

    # Calculate the offset to adjust the starting row for sheet3
    row_offset = 23062 - start_row_sheet3

    # Copy data from sheet3 with a one-row gap after sheet2
    new_sheet.Range(new_sheet.Cells(start_row_sheet3 + row_offset, start_col_sheet3),
                    new_sheet.Cells(start_row_sheet3 + row_offset + sheet3_range.Rows.Count - 1,
                                    start_col_sheet3 + sheet3_range.Columns.Count - 1)).Value = sheet3_data

    # Save the new workbook
    new_wb.SaveAs(r"C:\Users\JK\Downloads\output_file.xlsx")

    # Close both workbooks
    wb.Close(False)
    new_wb.Close(True)

    # Quit Excel application
    excel.Quit()

copy_excel_data()

from python_calamine import CalamineWorkbook
workbook = CalamineWorkbook.from_path("CustIDtoLineID.xlsx")
print(workbook.sheet_names)
print(workbook.get_sheet_by_name("CustIDtoLineID").to_python())

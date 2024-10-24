from python_calamine import CalamineWorkbook
workbook = CalamineWorkbook.from_path("CustIDtoLineID.xlsx")
print(workbook.sheet_names)

df = workbook.get_sheet_by_name("CustIDtoLineID").to_python()
#print(type(df))
for (custID,custName) in df:
  print(custName)

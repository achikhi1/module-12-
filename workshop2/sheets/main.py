import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1A_0z-b3b8s_aagRbWCa6qisBPp2th5dpItLrLC9p5kI')
worksheet = sh.sheet1

#res = worksheet.get_all_records()
#res = worksheet.get_all_values()
#res = worksheet.col_values(1)
res = worksheet.get('A2:C2')
user = ["Susan", 25, "Sydney"]
# worksheet.append_row(user)

worksheet.update_cell(4,1, "hoi")

# worksheet.delete_rows(1)


import pywhatkit as pwk
import gspread

gc = gspread.oauth(credentials_filename='credentials.json')

sht1 = gc.open_by_key('1ERjOeFq0Q_rzsnZmdAvxAwYCazcOsDwY8fdEH8U-1Tg')

# print(sht1.sheet1.get('a6'))


worksheet = sht1.sheet1

for i in range(1,4):
    val = worksheet.cell(i, 2).value  # row, col

    print(val)
    base = "+" + str(val)
    pwk.sendwhatmsg_instantly(base, "PC Building Group https://chat.whatsapp.com/HoTxB8Py5wRFic49tsNWdD", 20, tab_close=True)



# list_of_lists = worksheet.get_all_values()

# print(list_of_lists)




# pwk.sendwhatmsg("+60104246844", "PC Building Group https://chat.whatsapp.com/HoTxB8Py5wRFic49tsNWdD", 13, 56) # hr, min
# pwk.sendwhatmsg_instantly("+60104246844", "Test msg.", 20, tab_close=True)


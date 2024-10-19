from importings import *

conn=sqlite3.connect("DataBase_V\\test.db", check_same_thread=False)
cursor=conn.cursor()
def get_key_id():
    bot_token = get_key_entry.get()
    chat_id = get_id_entry.get()
    get_all=cursor.execute(f'UPDATE tg_bot SET bot_token=?, chat_id=?',(bot_token, chat_id))
    conn.commit()
    root.quit()

root=Tk()
get_key_label=Label(root,text='Введіть ключ:',font='Verdana 10').place(x=5,y=15)
get_key_entry=Entry(root, width=50)
get_key_entry.place(x=140,y=15)
get_id_label=Label(root,text='Введіть ID:',font='Verdana 10').place(x=5,y=50)
get_id_entry=Entry(root, width=50)
get_id_entry.place(x=140,y=50)
get_key_id_button=Button(root,text='Записати дані',height=3,command=get_key_id).place(x=550,y=10)

root.geometry('700x100+600+200')
root.mainloop()
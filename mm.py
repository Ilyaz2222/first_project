import requests
from pprint import pprint
from tkinter import *
from tkinter import ttk


# https://github.com/\\
#hgkjfhg

# respons = requests.get('https://api.github.com/')
# respons2 = requests.get('https://google.com')

# print(respons)
# print(respons.ok)
# print(respons.status_code)

# print("")

# print(respons2.content)
# print(respons.content)

# json_respons = respons.json()
# pprint.pprint(json_respons['current_user_url'])
# print(json_respons)

# params = {'q' : 'python'}
# respons = requests.get('https://api.github.com/search/repositories', params = params)
# print(pprint.pprint(respons.json()))


# img_url = 'https://ru.freepik.com/free-photo/forest-landscape_40855681.htm#query=%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&position=1&from_view=keyword&track=ais&uuid=08d34202-b1b5-4477-90e3-76e0bf3c2089'
# response = requests.get(img_url)

# with open('img.png', 'wb') as file:
#     file.write(response.content)


# pprint.pprint(respons2)


# print(len(respons2))

root = Tk()
root.title("text")
root.geometry("500x700")


respons = requests.get('https://api.github.com')
respons2 = respons.json()

massiv = []
for i in respons2:
    massiv.append(i)

massiv2 = []
for i in range(len(massiv)):
    massiv2.append(respons2[massiv[i]])



# print(massiv2)

# print(massiv)
# columns = ("value", "key")
# tree = ttk.Treeview(columns = columns, show="headings")
# tree.pack(fill=BOTH, expand=1)
# tree.heading("value", text="1")
# tree.heading("key", text="2")


# for person in respons2:
#     tree.insert("", END, values=person)

rows = []

M = True
for i in range(len(respons2)):
    cols = []
    for j in range(2):
        e = Entry(relief=GROOVE)
        e.grid(row=i, column=j)
        if (M):
            e.insert(END,(massiv[i]))
            M = False
        else:
            e.insert(END,(massiv2[i]))
            M = True
        cols.append(e)

    rows.append(cols)

root.mainloop()
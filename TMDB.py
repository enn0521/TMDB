import tkinter as tk
import json
import requests

# api_key, access_token -> https://www.themoviedb.org/settings/api

api_key = "your_api_key"
read_access_token = "your_read_access_token"

with open("key.json", "r") as f:
    keys = json.load(f)

api_key = keys["api_key"]
read_access_token = keys["read_access_token"]

root = tk.Tk()
root.title("TMDB Movie Revenue")
root.geometry("350x500")

label_movie_id = tk.Label(root, text="movie_ID")
label_movie_id.pack(pady=(10,5))
entry_movie_id = tk.Entry(root, width=25)
entry_movie_id.pack()

def print_movie():
    movie_id = entry_movie_id.get()
    print('-' * 30)
    print('[PRINT] Movie ID = ', movie_id)
    print('-' * 30)
    
button_print = tk.Button(root, text='Print', command=print_movie)
button_print.pack(pady=15)

def print_revenue():
    movie_id = entry_movie_id.get()
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    revenue_value = data.get('revenue')
    print('[Result] Revenue = ', revenue_value)
    print('-' * 30)


button_revenue = tk.Button(root, text='Revenue', command=print_revenue)
button_revenue.pack(pady=15)

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer {read_access_token}"
}

response = requests.get(url, headers=headers)

print(response.text)


root.mainloop()
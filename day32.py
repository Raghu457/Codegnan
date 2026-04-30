
'''
import matplotlib.pyplot as plt
plt.bar([2024,2025,2026],[67,89,50],color='black')
plt.title("Car Sales")
plt.xlabel("Years")
plt.ylabel("Number of cars sold")
plt.show()
'''

'''
import matplotlib.pyplot as plt
plt.pie([40,15,35,20],labels=["Backend(Python)","Frontend(HTML,CSS)","Database(SQL)","Datasets"])
plt.title("Major Project")
plt.legend(["Raghu","Dimple","Tarun","Sai"])
plt.show()
'''

'''
import matplotlib.pyplot as plt
plt.bar(['Attic','velvet','commision','objects','mankind','Red','Voodhul','Olympics','ck Maria'],[50,55,45,43,60,20,35,15,20])
plt.title('Top 10 book prices')
plt.ylabel('Prices')
plt.xlabel('names')
plt.show()
'''


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re
url="http://books.toscrape.com/"

try:
    response=requests.get(url)
    response.encoding='utf-8'
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:",e)
    exit()

soup=BeautifulSoup(response.text,"html.parser")

books=soup.find_all("article",class_="product_pod")
names=[]
prices=[]


for book in books:
    name=book.h3.a["title"]

    price_text=book.find("p",class_="price_color").text
    price=float(re.findall(r'\d+\.\d+',price_text)[0])

    names.append(name)
    prices.append(price)

df=pd.DataFrame({
    "Book Name": names,
    "Price":prices
})

print("\n Table Data:\n")
print(df.head())


df.to_csv("books_data.csv",index=False)
print("\n CSV file 'books_data.csv' created successfully!")



plt.figure()
plt.bar(names[:10],prices[:10])
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()
    

import pandas as pd
import re
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
df = pd.read_csv("Ecommerce Purchases")

# Check the head of the DataFrame.
print("Check the head of the DataFrame.")
print(df.head())

# How many rows and columns are there?
print("How many rows and columns are there?")
print(df.info())

# What is the average Purchase Price?
print("What is the average Purchase Price?")
print(df['Purchase Price'].mean())

# What were the highest and lowest purchase prices?
print("What were the highest and lowest purchase prices?")
print(df['Purchase Price'].max())
print(df['Purchase Price'].min())

# How many people have English 'en' as their Language of choice on the website?
print("How many people have English 'en' as their Language of choice on the website?")
print(df[df['Language'] == 'en'].count())

# How many people have the job title of "Lawyer" ?
print("How many people have the job title of \"Lawyer\" ?")
print(df[df['Job'] == 'Lawyer'].count())

# How many people made the purchase during the AM and how many people made the purchase during PM ?
print("How many people made the purchase during the AM and how many people made the purchase during PM ?")
print(df['AM or PM'].value_counts())

# What are the 5 most common Job Titles?
print("What are the 5 most common Job Titles?")
print(df['Job'].value_counts().head())

# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
print("Someone made a purchase that came from Lot: \"90 WT\" , what was the Purchase Price for this transaction?")
print(df[df['Lot'] == '90 WT']['Purchase Price'])

# What is the email of the person with the following Credit Card Number: 4926535242672853
print("What is the email of the person with the following Credit Card Number: 4926535242672853")
print(df[df["Credit Card"] == 4926535242672853]['Email'])

# How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
print("How many people have American Express as their Credit Card Provider and made a purchase above $95 ?")
print(df[(df['CC Provider'] == 'American Express') & (df['Purchase Price'] > 95)].count())

# Hard: How many people have a credit card that expires in 2025?
print("Hard: How many people have a credit card that expires in 2025?")
print(df['CC Exp Date'].apply(lambda x: re.search('...25', x)).count())

# Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
print("Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)")
print(df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head())

# import pandas as pd
# url= "https://dummyjson.com/users?limit=100"
# df= pd.read_json(url)
# print(df.head)

import pandas as pd
import requests

url = "https://dummyjson.com/users?limit=100"

# Step 1: Define headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Step 2: Use the requests library to fetch the data
response = requests.get(url, headers=headers)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()
    
    # Step 4: Extract the 'users' list into a DataFrame
    df = pd.DataFrame(json_data['users'])
    
    # Step 5: Print the first 5 rows (use head() with parentheses to execute the function)
    print(df.head())
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# Returns a tuple like (100, 30)
print(df.shape)

# To print it in a more readable format:
rows, columns = df.shape
print(f"The DataFrame has {rows} rows and {columns} columns.")

# 2-Columns Names 
print(df.columns)

#3- Data types 
print(df.dtypes)

#4- Number of missing values per column
cntnas= df.isna().sum()
print(cntnas)

#5- Number of duplicates 
# Replace your current DataFrame creation with this:
json_data = response.json()
df = pd.json_normalize(json_data['users'])

# Now this will work:
NofDuplicates = df.duplicated().sum()
print(f"Number of duplicates: {NofDuplicates}")

#6- Stats of Data
print(df.describe())

#7-Value counts for important categorical columns
cols_to_check= df.columns
for col in cols_to_check:
        if col in df.columns:
            print(f"--- Value Counts for {col} ---")
            print(df[col].value_counts())
            print("\n")

#8- 
if "country" not in df.columns:
    print("Column 'country' is missing")
 
print(df.head())

import json

import json

df["country"] = df.get("country")  # creates column if missing
address_series = df.get("address")  # returns None column if missing

if address_series is not None:
    extracted = address_series.dropna().apply(
        lambda x: json.loads(x).get("country") if x else None
    )
    df.loc[extracted.index, "country"] = df.loc[extracted.index, "country"].fillna(extracted)

#9- na values (age-height-weight)
ageNa= df["age"].isnull().sum()

heightNa= df["height"].isnull().sum()

weightNa= df["weight"].isnull().sum()

print(f"--- Value Counts for missing values for age, height, weight {ageNa},{heightNa},{weightNa} ---")

# proj Analysis 
#1-What is the average age of users
avgAge= df["age"].mean() 
print(avgAge)

#2-Average age by gender? 
AgeGBgender= df.groupby("gender")["age"].mean()
print(AgeGBgender)

#3-Number of users per gender

NofUsersGender= df.groupby("gender")["id"].count()
print(NofUsersGender)

#4- Top 10 cities with the most users
top_cities= df["city"].value_counts().head(10)
print(f"the top cities are: {top_cities}")

#5- Average height and weight overall
avg_height = df["height"].mean()
avg_weight = df["weight"].mean()

print("Average height:", avg_height)
print("Average weight:", avg_weight)

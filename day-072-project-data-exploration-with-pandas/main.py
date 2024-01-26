from bs4 import BeautifulSoup
import pandas as pd
import requests

url = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
df = None

while url:
    response = requests.get(url)
    response.raise_for_status()
    website_html = response.text
    soup = BeautifulSoup(website_html, "html.parser")

    table_headers = [tr.text for tr in soup.find_all("tr")[0]]
    table_rows = [tr.text for tr in soup.find_all("span", class_="data-table__value")]
    rows = [table_rows[i:i + 6] for i in range(0, len(table_rows), len(table_headers))]

    table_data = {
        f"{table_headers[i]}": [row_data[i] for row_data in rows] for i in range(len(table_headers))
    }

    if df is None:
        df = pd.DataFrame(table_data)
    else:
        df = pd.concat([df, pd.DataFrame(table_data)], ignore_index=True)

    # Get Next pagination button
    next_button = soup.find(name="a", class_="pagination__btn pagination__next-btn")
    if next_button:
        url = "https://www.payscale.com" + next_button.get("href")
    else:
        break

# Data Exploration
# print(df.head())  # Return the first 5 rows.
# print(df.tail())  # Return the last 5 rows.
# print(df.shape)  # Return (rows, columns) count.
# print(df.columns)  # Return column labels.
# print(df.isna())  # Return a boolean same-sized object indicating if the values are NA.
# df.dropna()  # Remove missing values.
# print(df["Major"])  # Show all the values for column "Major".
# print(df["Major", "Mid-Career Pay"]) # Show all the values for columns "Major" and "Mid-Career Pay".
# print(df["Major"][30])  # Return the value of column "Major" for row 30.
# print(df["Major"].loc(30))  # Same as above.
# print(df["Mid-Career Pay"].max())  # Show max value for "Mid-Career Pay" in the entire DataFrame.
# print(df["Mid-Career Pay"].min())  # Show min value for "Mid-Career Pay" in the entire DataFrame.
# print(df["Mid-Career Pay"].idxmax())  # Show the row position of the max value for "Mid-Career Pay" in the DataFrame.
# print(df["Mid-Career Pay"].idxmin())  # Show the row position of the min value for "Mid-Career Pay" in the DataFrame.
# df.sort_values(["Mid-Career Pay"]) # Sort values by "Mid-Career Pay" column. Argument ascending=True by default.
# df.insert(1, "Column Name", [1, 2]) # Add new column "Column Name" at position 1 with [1, 2] as values.
# df.groupby(["Degree Type"])  # Group DataFrame using a mapper or by a Series of columns (in this case, "Degree Type").

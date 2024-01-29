# Day 74 Project: LEGO dataset Analysis

## Concept

This project aims to perform some analysis into a LEGO dataset containing a predetermined schema.
Below is a summary of some of the techniques applied and the questions availed to query over the dataset.

- How many different colours does the LEGO company produce?
- How many transparent colours and opaque colours are available?
- In which year were the first LEGO sets released and what were these sets called?
- How many different sets did LEGO sell in their first year?
- What are the top 5 LEGO sets with the most number of parts?
- How many sets have been released per year since 1955 (exclude 2020 and 2021 excluded)? (with a line chart).
- How many different themes were shipped by year (2020 and 2021 excluded)? (with a line chart)
  - How the last two visualizations compare in a single line chart?
- What was the average number of parts per set per year since 1955 (2020 and 2021 excluded)? (with a scatter plot)
- Which theme has the largest number of individual sets?
- How many ids correspond to the name "Star Wars"? (merge two DataFrames)
- What are the top 10 themes with the most number of sets? (bar chart)

## Resources

- [Jupyter Notebook documentation](https://docs.jupyter.org/en/latest/)
- [Matplotlib: Visualization with Python](https://matplotlib.org/)
- [Pandas documentation](https://pandas.pydata.org/docs/)

### Useful functions used here

- groupby()
- count()
- value_counts()
- agg()
- rename()
- merge()
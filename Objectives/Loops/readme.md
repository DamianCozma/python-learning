# Carly's Clippers Project

In the Carly's Clippers project, you take on the role of a Data Analyst at Carly’s Clippers, the newest hair salon in town. Your task is to analyze data collected over the past few weeks to calculate key metrics that Carly can use for planning the business operations for the rest of the month.

## Data Provided

You are provided with three lists:

- `hairstyles`: Names of the haircuts offered.
- `prices`: Prices for each hairstyle.
- `last_week`: Number of each hairstyle sold last week.

Each index across these lists corresponds to a specific hairstyle, its price, and how many times it was purchased last week.

## Objective

The project's goal is to calculate the average price of a haircut, adjust haircut prices, calculate total revenue, and identify haircuts under a certain price to target specific marketing strategies.

## Tasks Overview

- Calculate the average price of a haircut.
- Reduce all haircut prices by $5.
- Calculate the total revenue from the last week.
- Find the average daily revenue.
- Create a list of haircuts priced under $30 to target for advertising.

## Features

- **Average Price Calculation**: Sum all haircut prices and divide by the total number of haircuts to find the average.
- **Price Adjustment**: Use list comprehension to reduce each haircut price by $5.
- **Revenue Calculation**: Multiply each haircut's price by the number

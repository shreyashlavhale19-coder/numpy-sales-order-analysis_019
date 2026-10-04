# NumPy Sales Order Analysis

## Project Objective

The main objective of this project is to analyze sales order data using **Python and NumPy**.

This project performs different data analysis operations such as revenue calculation, filtering orders, finding averages, discounts, percentiles, and statistical analysis.

## Dataset

The dataset contains the following columns:

* **Order ID** – Unique ID of the order
* **Quantity** – Number of products ordered
* **Price** – Price of the product
* **Rating** – Customer rating

## Technologies Used

* Python
* NumPy

## NumPy Concepts Used

* NumPy Arrays
* Array Dimension, Shape and Size
* Array Slicing
* Boolean Indexing
* Conditional Filtering
* Vectorized Operations
* `np.sum()`
* `np.mean()`
* `np.median()`
* `np.argmax()`
* `np.where()`
* `np.around()`
* `np.std()`
* `np.percentile()`
* Array Reshaping
* Array Flattening

## Analysis Performed

The project performs the following analysis:

1. Finds the dimension, shape and size of the dataset.
2. Displays the first 5 and last 3 orders.
3. Selects every second order.
4. Calculates revenue for each order.
5. Calculates total and average revenue.
6. Finds the order with the highest revenue.
7. Calculates median revenue.
8. Categorizes orders into High, Medium and Low revenue.
9. Filters orders based on quantity and rating.
10. Finds orders based on price and rating conditions.
11. Applies discounts to orders with price above 1000.
12. Calculates price after discount.
13. Rounds discounted prices to 2 decimal places.
14. Calculates standard deviation of prices.
15. Calculates 25th and 75th percentiles.
16. Finds prices above the 75th percentile.
17. Calculates the percentage of orders having a rating of 4 or above.
18. Reshapes revenue data into a 3 × 4 array.
19. Calculates average revenue of each row.
20. Flattens the reshaped revenue array.
21. Calculates total revenue of highly rated orders whose revenue is above average.

## Project Structure

```text
numpy-sales-order-analysis/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Install NumPy

```bash
pip install numpy
```

### 3. Run the program

```bash
python main.py
```

## Learning Outcome

Through this project, I learned how to use NumPy for basic data analysis and how numerical data can be processed efficiently using arrays and vectorized operations.

## Future Improvements

* Add Pandas for advanced data analysis.
* Add Matplotlib for data visualization.
* Read data from a CSV file instead of manually creating the array.
* Create charts for revenue and order analysis.

## Author

**Shreyash Lavhale**

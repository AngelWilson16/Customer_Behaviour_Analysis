# Customer_Behaviour_Analysi


## Overview
This project focuses on analyzing customer purchasing behavior using Python, SQL, PostgreSQL, and Power BI. The objective of the project is to identify customer trends, purchasing patterns, revenue contribution, and business insights through data analysis and visualization.

The project includes:
- Data loading and preprocessing using Python
- Exploratory Data Analysis (EDA)
- Data cleaning and feature engineering
- SQL analysis using PostgreSQL
- Interactive dashboard development in Power BI
- Business insights and recommendations
- Report and presentation creation

---

## Dataset
The dataset contains customer demographic and transactional information, including:

- Customer ID
- Age
- Gender
- Item Purchased
- Category
- Purchase Amount
- Review Rating
- Subscription Status
- Shipping Type
- Previous Purchases
- Frequency of Purchases
- Payment Method

The dataset consists of 3,900 records and includes both numerical and categorical variables.

---

## Tools & Technologies

## Tools & Technologies

**Programming & Analysis:** Python, SQL  
**Libraries:** Pandas, NumPy, Matplotlib, Seaborn  
**Database:** PostgreSQL  
**Visualization:** Power BI  
**Development Environment:** Jupyter Notebook  
**Presentation & Reporting:** Gamma, PowerPoint  
**Version Control:** GitHub

---

## Project Workflow

### 1. Data Loading
- Imported the dataset using Pandas
- Performed initial exploration using:
  - `df.head()`
  - `df.info()`
  - `df.describe()`

---

### 2. Data Cleaning
- Handled missing values using median imputation
- Standardized column names
- Verified data types
- Performed consistency checks
- Converted categorical purchase frequency into numerical values

#### Example
```python
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)


### 3. Exploratory Data Analysis (EDA)
Performed analysis to identify:
- Revenue trends
- Customer purchasing behavior
- Product performance
- Customer segmentation
- Revenue contribution by demographics

Visualizations included:
- Bar charts
- Pie charts
- Histograms
- Correlation analysis

---

### 4. SQL Analysis
SQL queries were executed in PostgreSQL to extract business insights such as:

- Revenue contribution by gender
- Subscriber vs non-subscriber spending
- Top-rated products
- Customer segmentation
- Top-selling products by category
- Revenue contribution by age group

#### Example Query
```sql
SELECT gender, SUM(purchase_amount) AS revenue
FROM customer
GROUP BY gender;
```

---

## Dashboard
An interactive Power BI dashboard was developed to visualize key insights and KPIs.

### Dashboard Highlights
- Total Revenue
- Average Review Rating
- Customer Segmentation
- Sales by Category
- Revenue by Age Group
- Subscription Analysis
- Product Performance

The dashboard enables quick and effective business decision-making through interactive visualizations.

---

## Key Results & Insights

- Male customers contributed higher overall revenue compared to female customers.
- Young Adults generated the highest revenue among all age groups.
- Loyal customers formed the largest customer segment.
- Clothing was the highest-performing product category.
- Top-rated products showed consistent customer satisfaction.
- Subscription status had minimal impact on average spending behavior.

---

## Business Recommendations

- Focus marketing efforts on high-revenue customer segments.
- Improve customer acquisition strategies to attract new customers.
- Promote top-performing and highly rated products.
- Strengthen customer retention through loyalty programs.
- Enhance subscription benefits to increase subscriber engagement.

---

## Project Structure

```text
Customer-Behavior-Analysis/
│
├── dataset/
├── notebooks/
├── sql_queries/
├── powerbi_dashboard/
├── report/
├── presentation/
├── README.md
```

---

## Project Files

- Python Notebook (`.ipynb`) for data cleaning and analysis
- SQL file (`.sql`) containing business queries
- Power BI dashboard (`.pbix`)
- Project report (`.pdf`)
- Presentation (`.pptx` / Gamma PPT)

The project can be viewed using Jupyter Notebook, PostgreSQL, and Power BI Desktop.

---

## Conclusion
This project demonstrates how data analytics can transform raw customer data into actionable business insights. By combining Python, SQL, and Power BI, the project provides a complete workflow for data cleaning, analysis, visualization, and business decision-making.

---

## Author
**Angel Wilson**  
B.Sc. Data Analytics Student  
SQL | Python | Power BI | PostgreSQL

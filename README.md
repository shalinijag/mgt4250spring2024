# MGT 4250 Spring 2024 Course Project
Author: Shalini Jagannathan (sjagannathan@elon.edu)

## Project Description
### Questions of Interest:
- Question 1
- Question 2
- Question 3
### Importance Statement
These questions are *especially* **important** because ...
1. Reason 1
2. Reason 2
3. Reason 3

[Elon University](https://www.elon.edu)

<img width="298" alt="Screenshot 2024-05-02 at 2 53 41 PM" src="https://github.com/shalinijag/mgt4250spring2024/assets/167243104/5db55508-a59f-401e-a0c0-0c5b8bc17b74">

## Data Description
Improving sales performance and customer satisfaction are main objectives for any e-commerce business. In a highly competitive online marketplace, understanding customer behavior and purchase patterns is essential for survival within the market. By leveraging data, businesses can make informed decisions that enhance the user experience and increase sales and customer loyalty.

For this analysis, I utilized a comprehensive e-commerce dataset from the month of November 2019, sourced from (Kechinov ECommerce behavior data from Multi Category Store). This dataset was chosen for its extensive details on customer interactions and transactions, offering an overall view of consumer behavior over a significant period.

## Interpreting Visualizations

<img width="424" alt="Screenshot 2024-05-02 at 2 59 17 PM" src="https://github.com/shalinijag/mgt4250spring2024/assets/167243104/a7865b55-0442-49d0-afd4-f042ed76914a">

1. The main purpose is to segment customers into groups based on their purchasing behavior and preferences. By visually breaking down the customer base into distinct segments, it is easy to identify which groups contribute most to sales and might have distinct needs or behaviors. Understanding the size and purchasing power of each segment allows for more targeted marketing, sales strategies, and personalized customer experiences, which are essential for improving sales performance and satisfaction. I plan to make the tree map interactive using machine learning which will be detailed later in the report. It needs improvement in terms of aesthetics as the segment names are long and random ID’s, so that would be another improvement.

## Discussion & Summary
I plan to incorporate machine learning within my project. I have a few ways to do this such as KMeans and clustering which I will detail below. First I need to ensure the data is clean which involves handling missing values, removing duplicates, and standardizing features. So, I would create features that are relevant to customer behavior analysis. A few could be Recency (time since last purchase), Frequency (number of purchases during a period), Monetary Value (total spend by the customer), or even Average Order Value (average spend per purchase). I will divide the dataset into a training set and a testing set (not sure of ratio yet). I will use KMeans and use the method to find the optimal amount of clusters.


```python
import pandas as pd
```

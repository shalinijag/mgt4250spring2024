# MGT 4250 Spring 2024 Course Project
Author: Shalini Jagannathan (sjagannathan@elon.edu)

### This repository is for the course project of MGT 4250 at Elon University.

## *READ BEFOREHAND*
The original data file is too large to download within Github. I have put in the Jupyter Notebook and Python files as well as linked the dataset within a Google Drive link before. The code works properly within the local source and local streamlit, but when trying to connect the data to the streamlit cloud service, I was unable to transfer it over. If you would like to see the proper visualizations, please use the app4.py python file and run it in the FINAL MGT4250.ipynb jupyter notebook. I used many methods to try and solve this problem, including AI. So, if you see any odd and improper code, that was me trying to fix the problem I was encountering. I tried to directly link the Google Drive file in my code, but it would read the file as html and would be unable to load any of the actual visualizations. Next, I tried to use the Github Large File software, however, since the file size was 9.01 GB, even when i tried to zip, or pickle the file, it was still too large for Github to upload. I tried various other methods before finally landing on my last solution which seems to work the best except for the fact that the app is not loading. I have attempted to link the direct Kaggle file within the code and it seems to load the data atleast, it just stops before loading the actual visualizations. Hopefully after talking with my professor this will be removed or shortened, but for now this is the progress that has been made.

## Download the Data
The full dataset is available for download here:
- [2019-Nov.csv on Google Drive](https://drive.google.com/file/d/1IYV7FA4p_-0JPGxyDFneiIn336HvBPTy/view?usp=sharing)

## Project Link:
[E-commerce Customer Analysis](https://mgt4250spring2024-ftolldtimtv8aolpqumwad.streamlit.app/)

## Project Description
The project aims to analyze e-commerce customer behavior to identify patterns and trends that can improve sales performance and customer satisfaction. By investigating customer purchase behavior, the project seeks to answer the following core questions:

### Questions of Interest:
- Which products or categories are most popular among different customer segments?
- What purchase patterns can be identified across different customer segments?
- How can certain customer behaviors help predict a high lifetime value?

#### Importance Statement
E-commerce is rapidly growing, and companies need better insights into customer behavior to improve their sales and customer satisfaction. This analysis hopes to provides data-driven insights, helping businesses tailor their marketing, management, and customer service strategies. According to reports by the National Retail Federation, improving customer experience and personalization are crucial for staying competitive in the digital marketplace.

#### These questions are *especially* **important** because ...
1. Enhanced Customer Retention:
Analyzing customer behavior helps identify patterns that contribute to high customer satisfaction and retention. By recognizing loyal customers and understanding their needs, businesses can implement strategies that foster long-term relationships and increase customer lifetime value.

2. Optimized Product Recommendations:
Studying customer behavior allows businesses to predict customer preferences and recommend products more effectively. This optimization leads to a more personalized shopping experience, increases cross-selling opportunities, and drives overall sales growth by encouraging customers to explore additional products or categories.

3. Improved Inventory Management:
Understanding customer behavior aids in forecasting demand more accurately. This insight allows businesses to manage inventory efficiently, ensuring popular products remain stocked while reducing excess inventory. As a result, businesses can minimize storage costs, prevent low stock, and enhance the overall customer experience.

## Data Description and Upload

For this analysis, I utilized a comprehensive e-commerce dataset from the month of November 2019, sourced from (Kechinov ECommerce behavior data from Multi Category Store). This dataset was chosen for its extensive details on customer interactions and transactions, offering an overall view of consumer behavior over a significant period.

- Dataset Source: E-commerce Dataset on [Kaggle](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- Required File: 2019-Nov.csv

- How to Download:
  - Option 1: Access it via Kaggle with the link provided and follow the instructions for downloading.
  - Option 2: Alternatively, download it from the Google Drive link provided above.

## Data Types and Columns Descriptions

- event_time (datetime64[ns, UTC]): The timestamp when an event occurred. It helps identify the patterns of customer actions and provides insights into their behavior over time.
- category_id (int64): An integer representing the unique identifier for each product category. It's useful for the grouping and filtering products by category.
- category_code (object): The string representation of a product's category, indicating the type of product being purchased. It helps in understanding product preferences across different categories.
- price (float64): The value representing the price of an individual item. This data is crucial for calculating total spending and analyzing the monetary value of transactions.
- user_id (int64): An integer representing the unique identifier for each customer. This allows grouping and tracking purchase patterns by individual customers.
- total_price (float64): The numeric value representing the **total** price of products in a transaction or user-specific aggregation. This helps analyze customer spending patterns and determine customer lifetime value.

## Interpreting Visualizations

#### 1a:
<img width="557" alt="Screenshot 2024-05-09 at 1 51 10 AM" src="https://github.com/shalinijag/mgt4250spring2024/assets/167243104/ba8d9371-1729-45db-afcf-81be6f05fd1c">

#### 1b:
<img width="561" alt="Screenshot 2024-05-09 at 1 51 43 AM" src="https://github.com/shalinijag/mgt4250spring2024/assets/167243104/422f22d8-91f0-4919-85e5-96353fa7e4e3">

#### 2:
<img width="575" alt="Screenshot 2024-05-09 at 1 52 04 AM" src="https://github.com/shalinijag/mgt4250spring2024/assets/167243104/a6866a02-50d0-4ffd-9e62-cc282d3624b6">

#### 3:
<img width="574" alt="Screenshot 2024-05-09 at 1 52 19 AM" src="https://github.com/shalinijag/mgt4250spring2024/assets/167243104/abea08a9-71ec-4574-83d6-ae311a63111a">


1. Customer Segmentation Tree Maps:
- a. Static Tree Map:
  - Interpretation: The static tree map provides a clear visual representation of the top 20 customers based on their total spending. The size of each block indicates the total revenue contributed by each customer. It helps businesses quickly identify their most valuable customers
  - Contribution to Questions: This visualization directly addresses the question of identifying the customers who contribute the most to overall revenue. By understanding which customer segments are critical for revenue generation, businesses can focus on retention strategies, personalized marketing campaigns, and special offers for these key clients. This ensures that high-value customers continue to remain loyal and their lifetime value (LTV) is maximized.
- b. Interactive Tree Map:
  - Interpretation: The interactive tree map applies KMeans clustering to group customers based on their total spending and purchasing frequency. This creates distinct clusters, making it possible to observe customer segments and their behavior patterns. The clustering allows users to explore high-value segments interactively.
  - Contribution to Questions: By identifying distinct clusters, this visualization reveals segmentation patterns that help in designing targeted marketing strategies. For instance, a cluster with high total spending but low frequency may benefit from campaigns encouraging repeat purchases. Meanwhile, high-frequency clusters may receive personalized product recommendations. This strategy optimizes customer experience, enhances brand loyalty, and maximizes revenue from different customer groups.
2. Predictive Lifetime Value (LTV) Scatter Plot:
  - Interpretation: The LTV scatter plot visualizes the relationship between customers' purchase frequency and monetary value. Each point represents a customer, with the x-axis showing purchase frequency and the y-axis showing the total monetary value they have generated. The use of log scales makes it easier to observe patterns even in a diverse dataset.
  - Contribution to Questions: This visualization allows businesses to identify and categorize customers by their lifetime value (LTV). Those who make frequent purchases and have high monetary value can be prioritized for targeted retention campaigns to secure their loyalty and drive future purchases. Conversely, low-frequency or low-value customers may receive tailored strategies to increase their engagement and purchasing behavior. This insight is critical in resource allocation, focusing marketing efforts on customers who provide the highest returns.
3. Total Sales by Product Category Bar Chart:
  - Interpretation: The bar chart displays the total revenue generated by each product category, ranked from highest to lowest. Each bar represents a specific product category, with its height showing the total sales achieved in that category.
  - Contribution to Questions: By providing a clear view of the top-selling product categories, this visualization helps businesses identify the most lucrative categories, guiding decisions in inventory management, marketing strategies, and product development. Understanding which product types are generating the most sales ensures that businesses can prioritize stocking and promoting the most profitable items. Furthermore, low-performing categories can be examined for improvement opportunities or reconsideration.

## Discussion & Summary

### Article Discussion

I was able to find an article that discussed predictive analytics with customer behavior in e-commerce. This article was closely related to my project.

[Article Link](https://cotinga.io/blog/predictive-analytics-in-e-commerce/)

The article emphasizes the role of predictive analytics in refining e-commerce marketing strategies through data visualization and machine learning. It exemplifies the value of analyzing customer behavior and historical data to better forecast trends, tailor marketing strategies, and adjust inventory planning. These insights directly relate to my project, where I used similar techniques to help identify high-LTV customer segments and personalized marketing. The clustering and predictive LTV visualizations in my project demonstrate how data analysis can reveal key customer patterns to improve targeted campaigns.

### AI Query

I used ChatGPT4.0 for this query.

- At first, I had just asked the three Questions of Interest listed above just to see what AI would come back with. This was it's response:
    - Most Popular Products/Categories: By analyzing the data, you can identify which product categories are most popular among various customer segments. For instance, electronics and home appliances may attract distinct segments based on age and location.
    - Purchase Patterns Across Segments: Patterns like frequent small purchases versus occasional big-ticket buys can help differentiate segments.
    - Predicting High Lifetime Value: Tracking behaviors like early repeat purchases and higher average order value helps predict which customers will likely have a higher lifetime value due to their consistent, high-volume purchases.
 
- I then asked "I have an e-commerce behavior analysis project that I am doing. I have a few questions as listened above that I am solving and wanted to see your thoughts/answers on the questions", and this was it's response:
    - For your e-commerce behavior analysis project, here are some thoughts on each of your questions:
      1. Popular Products or Categories Among Different Customer Segments:
        - Analysis Approach: 
          - Segment customers based on attributes like demographics, location, or purchase behavior.
          - Identify popular products or categories by analyzing transaction data per segment.
        - Insights:
          - Younger customers might favor trending products or gadgets, while older segments could prefer essentials or luxury goods.
          - Region-specific preferences could emerge due to climate or cultural factors.
      2. Identifying Purchase Patterns Across Segments:
        - Analysis Approach:
          - Track metrics like frequency, average order value (AOV), or repeat purchase rates.
          - Look for seasonality in purchase behaviors, e.g., holiday spikes.
        - Insights:
          - Segments with high frequency but low AOV might prefer deals and discounts, while others with less frequent but larger purchases are likely focused on premium items.
          - A notable pattern could be cross-category affinity, where a purchase in one category often leads to purchases in another.
      3. Predicting High Lifetime Value Based on Customer Behaviors:
        - Analysis Approach:
           - Use predictive modeling like logistic regression or machine learning algorithms on historical data to identify predictors.
        - Key Behaviors:
          - Early repeat purchase: Customers who make a second purchase quickly after their first tend to have higher lifetime value.
          - Diverse purchasing: Customers buying across multiple categories might be more likely to stay loyal.
          - Loyalty program membership and engagement can be a strong indicator of high LTV.

- Lastly, I asked AI "what do you think the answers are to these questions?". This is what it came up with:
1. Most Popular Products/Categories Across Customer Segments:
    - Younger demographics often favor trendy tech gadgets, fashion items, or gaming products.
    - Older customers may lean towards home goods, appliances, or personal care.
    - Geographic regions could have unique preferences due to local trends or cultural influences. Urban areas may show higher interest in luxury products, while rural regions might focus on essentials.
2. Identified Purchase Patterns Across Segments:
    - Budget-conscious customers frequently purchase discounted items, smaller-sized goods, or economy packs.
    - Premium buyers are inclined toward high-quality, luxury, or niche products with fewer purchases but a higher average order value (AOV).
    - Seasonal shifts reveal patterns such as gift shopping around holidays or summer gear for vacation periods.
3. Predicting High Lifetime Value (LTV) Behaviors:
    - Early repeat purchase: Customers who make their second purchase within 30 days of the first are likelier to stay long-term.
    - Multi-category shoppers: Buying across various categories reflects adaptability and higher engagement.
    - Engagement with loyalty programs: Customers who sign up for and actively use rewards or membership programs tend to exhibit stronger loyalty and lifetime value.
 

### Alignment with Visualizations:

1. Most Popular Products/Categories Across Customer Segments:
  - The bar chart visualization aligns with this finding by showing the total sales per category. Trends across segments can be identified through this chart, allowing businesses to target specific groups.
2. Identified Purchase Patterns Across Segments:
  - The static and interactive tree maps illustrate customer segments and their spending patterns, revealing segments' purchasing behaviors, such as budget-conscious versus premium buyers.
3. Predicting High Lifetime Value (LTV) Behaviors:
  - The predictive LTV scatter plot identifies patterns between purchase frequency and monetary value. Early repeat purchases and high engagement can help prioritize customer retention.

#### These visualizations, supported by data, align closely with the article's insights.

### Final Summary

In this project, "Analyzing and Visualizing E-commerce Customer Behavior for Enhanced Business Strategy," we aimed to uncover insights from e-commerce data to identify trends, patterns, and strategies to improve business outcomes. The static and interactive tree maps revealed key customer segments and their revenue contributions, while KMeans clustering further refined the analysis, identifying high-value clusters. The LTV scatter plot showed relationships between purchase frequency and monetary value, helping identify high-LTV customers. The sales bar chart provided an understanding of the top-selling categories.

Informed by articles on customer behavior, we found that trends vary across segments and are influenced by demographics, geography, and seasonal patterns. Predicting high-LTV customers involved identifying early repeat purchases, multi-category buying habits, and loyalty program engagement. Our visualizations align with these findings, helping businesses tailor marketing, inventory planning, and customer retention strategies based on data insights.

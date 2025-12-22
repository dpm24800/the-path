---
layout: post
title:  EDA and Feature Engineering Test
description: 
thumbnail: /assets/images/eda/eda-test.png
author: Dipak Pulami Magar
date:   2025-12-19 16:12:45 +0545
categories: test eda
status: published
---
<center><h2>Section A: Multiple Choice Questions (12 x 0.5 = 6 marks)</h2></center>
1. Which imputation method is most suitable for skewed numerical data?  
    a. Mean  
    **b. Median**  
    c. Mode  
    d. Zero  
2. `dropna(axis=1)` removes:  
    a. Rows with missing values  
    **b. Columns with missing values**  
    c. Only numeric missing values  
    d. Only categorical missing values  
3. One-hot encoding converts categories into:  
    a. Single integer  
    **b. Binary columns**  
    c. Probability values  
    d. Ranks  
4. Which encoding can cause dimensionality explosion?  
    a. Ordinal  
    b. Target  
    **c. One-hot**  
    d. Label  
5. Which plot best shows data distribution?  
    a. Line plot  
    b. Bar chart  
    **c. Histogram**  
    d. Heatmap  
6. A correlation value of 0 indicates:  
    a. Strong positive relation  
    b. Strong negative relation  
    **c. No linear relation**  
    d. Perfect relation  
7. Which method ensures every data point appears in test set exactly once?  
    a. Hold-out  
    b. Random split  
    **c. K-Fold**  
    d. Stratified split  
8. Normalization scales data between:  
    a. -1 and 1  
    **b. 0 and 1**  
    c. Mean 0, std 1  
    d. Any range  
9. Which scaler is sensitive to outliers?  
    a. StandardScaler  
    **b. MinMaxScaler**  
    c. RobustScaler  
    d. MaxAbsScaler  
10. Feature engineering improves:  
    a. Data size  
    **b. Model performance**  
    c. Data leakage  
    d. Missing values  
11. Suppose you have a column “Chest Pain Type” which features [‘Normal’, ‘Moderate’, and, ‘Severe’, what is the best way to encode it?  
    a. One Hot Encoding  
    b. Nominal Encoding  
    **c. Ordinal Encoding**  
    d. Frequency Based Encoding  
12. Which distribution does the following histogram is shown here:

<!-- ![right-skewed-histogram]({{base.url}}/the-path/assets/images/matplotlib/right-skewed-histogram.png)   -->

![right-skewed-histogram](/the-path/assets/images/matplotlib/right-skewed-histogram.png)  
    a. Left Skew  
    **b. Right Skew**    
    c. Normal  
    d. Uniform  

---
<center><h2>Section B: Debug the Code (6 × 1 = 6 Marks)</h2></center>

**1. This code results in an Error. Why? Fix it.**
```py  
df.fillna(mean)  
```  
Debugged:  
```py
df.fillna(df['column_name'].mean())
# df.fillna(df.mean(), inplace=True)
```

**2. From this code snippet, debug the error:**
```py  
import pandas as pd  
import matplotlib.pyplot as plt  
  
### i. Loading the Dataset  
df = pd.read_csv("adult.csv")  
  
### ii. Cheking the null values

df.isna.sum()  
  
### iii. Checking the Bar Plot for Gender column  
gender_counts = df['sex'].value_counts()  
  
# Extract categories and their counts  
categories = gender_counts.index.tolist()  
counts = gender_counts.values.tolist()  
  
# Plot using matplotlib  
plt.figure(figsize=(6,4))  
plt.plot(categories, counts)  
plt.title('Count of Each Gender')
plt.xlabel('Gender')  
plt.ylabel('Count')  
  
### iv. Encode the Column Male with 1 and Female with 0:  
  
df ['gender'] = df['gender'].rename({"Male":1, "Female":0})  
```  

Debugged:
```py
import pandas as pd
import matplotlib.pyplot as plt

# i. Loading the Dataset
df = pd.read_csv("adult.csv")

# ii. Checking the null values
df.isna().sum() # 🕷️df.isna.sum() is wrong

# iii. Checking the Bar Plot for Gender column
gender_counts = df['sex'].value_counts()

# Extract categories and their counts
categories = gender_counts.index.tolist()
counts = gender_counts.values.tolist()

# Plot using matplotlib
plt.figure(figsize=(6, 4))
plt.bar(categories, counts) # 🕷️ Using plt.plot() for categorical data, it's not appropriate
plt.title('Count of Each Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# iv. Encode the Column Male with 1 and Female with 0
# 🕷️ Encoding using .rename(): .rename() is for renaming labels
# 🕷️ Encoding wrong column: df['gender'] does not exist
df['gender'] = df['sex'].map({'Male': 1, 'Female': 0})
```
### Errors and Fix

| **Error**                               | **Fix**                                                               |
| --------------------------------------- | --------------------------------------------------------------------- |
| `df.isna.sum()`                         | Missing `()` → `df.isna().sum()`                                      |
| `plt.plot(categories, counts)`          | Not suitable for categorical data → use `plt.bar(categories, counts)` |
| `.rename()` used for encoding           | `.rename()` is for renaming labels → use `.map()`                     |
| Encoding on `df['gender']`              | Column does not exist → encode from `df['sex']`                       |
| `df['sex']` (spacing issue in original) | Remove extra space → `df['sex']`                                      |

**3. This code results in an Error. Why? Fix it.**
```py
OneHotEncoder.fit_transform(data)
```
Debugged:
```py
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False)
encoded_data = encoder.fit_transform(data)
```

**4. Why does unpacking throw an error?**
```py
from sklearn.model_selection import train_test_split
X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)
```
Debugged:
```py
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42, shuffle=True)
```

**5. This code results in an Error. Why? Fix it.**
```py
plt.hist(df)
```
Debugged:
```py
plt.hist(df['numerical_column'])
plt.show()
```

**6. This code results in an Error. Why? Fix it.**
```py
df.interpolate(method='average')
```

Debugged:
```py
df.interpolate(method='linear')
```
---

<center><h2>Section D: Coding Questions (2 × 2.5 = 5 Marks)</h2></center>

**1. Create a new feature `BMI` from `Weight` and `Height`, then select top 3 features using correlation.**

Example dataset:

| Weight | Height | Age | BP  |
| ------ | ------ | --- | --- |
| 60     | 1.65   | 22  | 120 |
| 70     | 1.70   | 25  | 130 |
| 80     | 1.75   | 30  | 140 |
| 90     | 1.80   | 35  | 150 |

$$
{BMI} = \frac{\text{Weight (in kilograms)}}{\text{Height}^2 \text{ (in meters)}}
$$

### **Explanation**
1. **BMI formula:** `Weight / Height²`
2. **Correlation:** `df.corr()` calculates pairwise correlation. 
3. **Top features:** Sorted by **absolute correlation with BMI**.
    - `index[1:4]` skips BMI itself.


```py
import pandas as pd

# Create DataFrame
data = {
    'Weight': [60, 70, 80, 90],
    'Height': [1.65, 1.70, 1.75, 1.80],
    'Age': [22, 25, 30, 35],
    'BP': [120, 130, 140, 150]
}

df = pd.DataFrame(data)

# Create BMI feature
df['BMI'] = df['Weight'] / (df['Height'] ** 2)

# Check correlation
corr = df.corr()

# Select top 3 features correlated with BMI
top_features = corr['BMI'].abs().sort_values(ascending=False).index[1:4]

print("DataFrame with BMI:")
print(df)
print("\nTop 3 features correlated with BMI:", list(top_features))
```

Expected Output:
```
   Weight  Height  Age   BP        BMI
0      60    1.65   22  120  22.038567
1      70    1.70   25  130  24.221453
2      80    1.75   30  140  26.122449
3      90    1.80   35  150  27.777778

Top 3 features correlated with BMI: ['Weight', 'BP', 'Height']
```

**2. Given a dataset with a Date column, split it into:**
- Year
- Month
- Day

| Date       | Sales |
| ---------- | ----- |
| 2024-01-15 | 1000  |
| 2024-02-20 | 1500  |
| 2024-03-10 | 1200  |

```py
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'Date': ['2024-01-15', '2024-02-20', '2024-03-10'],
    'Sales': [1000, 1500, 1200]
})

# Convert Date to datetime and split into Year, Month, Day
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

print(df)
```

Expected Output:
```
        Date  Sales  Year  Month  Day
0 2024-01-15   1000  2024      1   15
1 2024-02-20   1500  2024      2   20
2 2024-03-10   1200  2024      3   10
```
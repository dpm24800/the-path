
Below is a **well-structured, complete, and detailed article** on **Train–Test Split in Machine Learning**, written in a clear and beginner-friendly style. It fits perfectly with your ML study plan.

---

# **📘 Train–Test Split in Machine Learning
Machine learning models must **generalize** well to new, unseen data. To measure this generalization ability, we must **evaluate the model on data it has never seen during training**. This concept is achieved through the **Train–Test Split**, one of the most fundamental steps in any ML workflow.

This article covers:

* What train–test split means
* Why it is necessary
* How to perform it
* Common splitting strategies
* Avoiding data leakage
* Best practices
* Python examples

---

# **1. What Is Train–Test Split?**
Train–test split is the process of **dividing your dataset into two parts**:

### **1. Training Set**
Used to **teach the model**.
It contains most of the data (usually 70–90%).

### **2. Test Set**

Used to **evaluate the model**.
Contains the remaining portion (usually 10–30%).

The key idea:
👉 **Train on one portion, test on another.**
This ensures the evaluation reflects the model’s performance on truly unseen data.

---

# **2. Why Do We Need Train–Test Split?**

If we train a model on the entire dataset and then test it on the same data:

* The model will perform extremely well
* But it is only memorizing patterns
* It fails to generalize
* This is called **overfitting**

To avoid this, we separate the data:

| Dataset Part  | Purpose                 |
| ------------- | ----------------------- |
| **Train Set** | Learn the patterns      |
| **Test Set**  | Evaluate on unseen data |

This separation simulates how the model behaves in the **real world**.

---

# **3. Typical Train–Test Ratios**

The ratio depends on dataset size:

| Dataset Size            | Recommended Split                       |
| ----------------------- | --------------------------------------- |
| Small (< 1,000 samples) | 80% train, 20% test OR cross-validation |
| Medium (1,000–50,000)   | 75–80% train, 20–25% test               |
| Large (> 100,000)       | 90–95% train, 5–10% test                |

Why larger datasets need a smaller test size:
Even 5% of 1 million data points gives 50,000 samples—enough to measure performance.

---

# **4. How Train–Test Split Works (Conceptually)**

Imagine a dataset of 10,000 rows.
A typical 80/20 split gives:

* 8,000 → used to train the model
* 2,000 → used to test the model

The model sees the 8,000 examples, learns from them, and then takes the 2,000 examples as a **final exam**.

The test set must remain **locked** until the end.

---

# **5. Performing Train–Test Split in Python (scikit-learn)**

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train size:", len(X_train))
print("Test size:", len(X_test))
```

### Explanation of parameters:

* `test_size=0.2` → 20% test, 80% train
* `random_state=42` → Reproducible split
* `shuffle=True` (default) → Shuffles before splitting

---

# **6. Types of Splitting Strategies**

Train–test split is not always random. Different datasets need different strategies.

---

## **6.1 Random Split (Most Common)**

Randomly distributes data into train and test.

Best for:

* Large datasets
* Non-time-dependent data
* When class ratio is already balanced

---

## **6.2 Stratified Split (For Classification)**

If dataset has **imbalanced classes**, random splitting may cause:

* Training set missing minority class
* Test set having wrong proportions

Example:
Class A = 90%, Class B = 10%

Random split could accidentally give:

* Train: 95% A, 5% B
* Test: 85% A, 15% B

This ruins evaluation.

To fix this, use stratification:

```python
train_test_split(X, y, test_size=0.2, stratify=y)
```

Stratified split **preserves class proportion** in both sets.

---

## **6.3 Time-Series Split**

For time-dependent datasets (stock prices, sales, weather), **random splitting is wrong**.

Why?

It breaks temporal order and leaks future data into the past.

Correct approach:

```
Train → Past data  
Test  → Future data
```

Example:

* Train: Jan–Oct
* Test: Nov–Dec

This simulates real-world prediction.

---

# **7. Avoiding Data Leakage**

**Data leakage** happens when information from the test set accidentally influences the training process.

This creates a model that looks good on tests but fails on real data.

### Common causes of data leakage:

❌ Scaling (Standardization/Normalization) before splitting
❌ Feature selection before splitting
❌ Time-series shuffled randomly
❌ Using test set during model tuning

### Correct approach:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", SomeModel())
])

pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)
```

The pipeline ensures:

* Scaling happens **only** on training data
* Test data scaling uses training parameters

---

# **8. Train–Validation–Test Split (Recommended Setup)**

Sometimes two splits are not enough.

ML problems often require:

* Hyperparameter tuning
* Model selection
* Early stopping

Using test set for tuning is wrong—it causes leakage.

Solution → 3-way split:

1. **Training Set** → Model learns
2. **Validation Set** → Tune hyperparameters
3. **Test Set** → Final model evaluation

Typical ratio:

* 70% train
* 15% validation
* 15% test

---

# **9. Cross-Validation (Better Than a Single Split)**

Instead of one train–test split, cross-validation splits data into **K folds**.

### Example: 5-fold CV

* Data is divided into 5 parts
* Model trains on 4 parts
* Tests on 1 part
* Repeats 5 times

This gives a stable, trustworthy performance score.

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
print(scores.mean())
```

---

# **10. How to Choose the Right Splitting Method?**

| Scenario                       | Best Method             |
| ------------------------------ | ----------------------- |
| Balanced classification        | Random split            |
| Imbalanced classification      | Stratified split        |
| Time-series data               | Time-based split        |
| Small datasets                 | Cross-validation        |
| Deep learning (large datasets) | 90/10 split or 70/15/15 |

---

# **11. Common Mistakes to Avoid**

### ❌ Using test data in any part of training

👉 Always keep test data untouched until the end.

### ❌ Scaling the entire dataset before splitting

👉 Always split first, then scale within training only.

### ❌ Very small test sets

👉 Leads to unreliable evaluation.

### ❌ Not shuffling non-time-series data

👉 May create biased splits.

### ❌ Using random split for time-series

👉 Future leakage ruins the model.

---

# **12. Summary Table**

| Component             | Purpose               | Notes                           |
| --------------------- | --------------------- | ------------------------------- |
| **Train Set**         | Learn patterns        | Should be the largest portion   |
| **Test Set**          | Final evaluation      | Never used during training      |
| **Validation Set**    | Hyperparameter tuning | Prevents leakage                |
| **Random Split**      | Standard method       | Works for most cases            |
| **Stratified Split**  | Balanced classes      | Prevents class imbalance issues |
| **Time-Series Split** | For temporal data     | Maintain chronological order    |

---

# **13. Conclusion**

Train–test split is a **fundamental concept** in machine learning.
A well-designed split ensures:

* Fair evaluation
* Avoidance of data leakage
* Better generalization
* More trustworthy models

Understanding how to split your data correctly is just as important as choosing the right model. Whether you're working with balanced data, imbalanced classes, or time-series, choosing the right splitting strategy is crucial for building a successful machine learning pipeline.

---

If you'd like, I can also create:

📌 **A diagram that visually explains the split**
📌 **A Jupyter Notebook-ready version**
📌 **MCQs + answers for practice**
📌 **A Nepali translation of the article**

Just tell me!

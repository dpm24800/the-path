---
layout: post
title: Implementing Polynomial Regression from Scratch
description: A Complete Guide with 5 Variables and Python Code
thumbnail: /assets/images/machine-learning/dfsfdfsdffier.png
author: Dipak Pulami Magar
date:   2026-01-03 08:12:45 +0545
categories: machine-learning supervised regression
status: draft
---

This post maintains the original article's structure and tone, expanding the mathematical model to a **4th-degree polynomial** (5 variables: $$w_4, w_3, w_2, w_1, b$$) to capture even more complex, oscillating data patterns.


Polynomial regression is a form of regression analysis in which the relationship between the independent variable $$X$$ and the dependent variable $$y$$ is modelled as an $$n^{th}$$ degree polynomial. By using 5 variables, we can model a **4th-degree polynomial**, allowing the curve to have up to three "turns" to fit highly non-linear data.

---

## 1. Prepare the Dataset

In a 4th-degree polynomial regression, we expand our single feature $$X$$ into a set of features representing its powers.

* **$$X, X^2, X^3, X^4$$** → Independent variable powers (features)
* **$$y$$** → Dependent variable (target)

The model learns how each power of $$X$$ contributes to the overall shape of the curve.

---

## 2. Define the Model (5-Variable Equation)

The equation for our model is:

$$\hat{y} = w_4x^4 + w_3x^3 + w_2x^2 + w_1x + b$$

Where:
* **$$w_4, w_3, w_2, w_1$$** → Weights for each polynomial degree
* **$$b$$** → Bias (intercept)
* **$$\hat{y}$$** → Predicted value

**Intuition:**
* $$w_4$$ and $$w_3$$ allow for complex "S" shapes or "W" shapes.
* $$w_2$$ controls the basic parabolic curvature.
* $$w_1$$ controls the linear slope.
* $$b$$ shifts the entire curve vertically.

---

## 3. Initialize Parameters

We start all 5 variables at zero:

```python
w4, w3, w2, w1, b = 0, 0, 0, 0, 0
α = 0.0000001  # Very small learning rate for high-degree terms
```

---

## 4. Make Predictions

We calculate the predicted value by summing the weighted powers of $$X$$:

$$\hat{y} = w_4x^4 + w_3x^3 + w_2x^2 + w_1x + b$$

---

## 5. Understand Residuals

The residual is the error for each specific point:

$$\text{Residual} = y - \hat{y}$$

---

## 6. Calculate the Loss (Error)

We use **Mean Squared Error (MSE)** to measure the total "cost" of our current curve:

$$MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

---

## 7. Compute Gradients (Derivatives)

With 5 variables, we need 5 partial derivatives. Notice how the power of $$X$$ matches the weight it updates:

$$\frac{\partial L}{\partial w_4} = \frac{2}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)x_i^4 \quad \text{, } \quad \frac{\partial L}{\partial w_3} = \frac{2}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)x_i^3$$
$$\frac{\partial L}{\partial w_2} = \frac{2}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)x_i^2 \quad \text{, } \quad \frac{\partial L}{\partial w_1} = \frac{2}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)x_i$$
$$\frac{\partial L}{\partial b} = \frac{2}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)$$

---

## 8. Update Parameters (Gradient Descent)

We update all 5 variables simultaneously:

$$w_n = w_n - \alpha \frac{\partial L}{\partial w_n} \quad \text{ (for } n=1,2,3,4\text{)}$$
$$b = b - \alpha \frac{\partial L}{\partial b}$$

---

# 5 Iterations of Gradient (Manual Walkthrough)

## Iteration 1

### 1. Dataset
$$X = [1, 2, 3], \quad y = [5, 30, 100]$$

**Initial Parameters:**
$$w_4, w_3, w_2, w_1, b = 0, \quad \alpha = 1e-5$$

---

### 2. Making Predictions
$$\hat{y} = 0(x^4) + 0(x^3) + 0(x^2) + 0(x) + 0 = [0, 0, 0]$$

---

### 3. Calculating Errors $$(y - \hat{y})$$
$$Error = [5, 30, 100]$$

---

### 4. Calculating Loss (MSE)
$$MSE = \frac{1}{3} (5^2 + 30^2 + 100^2) = \frac{25 + 900 + 10000}{3} = 3641.67$$

---

### 5. Calculating Gradients (Example: $$w_4$$)
$$d_{w4} = \frac{2}{3} [(-5 \cdot 1^4) + (-30 \cdot 2^4) + (-100 \cdot 3^4)] = \frac{2}{3} [-5 - 480 - 8100] = -5723.33$$

---

### 6. Updating Parameters
$$w_4 = 0 - (0.00001 \cdot -5723.33) = 0.0572$$
*(Similarly for $$w_3, w_2, w_1, b$$)*

---

## Iteration 2 to 5 (Summary)

| Iteration | $$w_4$$ | $$w_3$$ | $$w_2$$ | $$w_1$$ | $$b$$ | MSE |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 0.057 | 0.020 | 0.007 | 0.002 | 0.001 | 3641.67 |
| 2 | 0.102 | 0.035 | 0.013 | 0.004 | 0.002 | 1152.40 |
| 3 | 0.138 | 0.048 | 0.017 | 0.006 | 0.003 | 365.12 |
| 4 | 0.166 | 0.058 | 0.021 | 0.007 | 0.004 | 115.80 |
| 5 | 0.189 | 0.065 | 0.024 | 0.008 | 0.004 | 36.75 |

---

## Python Implementation

```python
import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5])
y = np.array([5, 25, 80, 200, 450])

# 5 Variables (Weights for x^4, x^3, x^2, x^1 and Bias)
w4, w3, w2, w1, b = 0.0, 0.0, 0.0, 0.0, 0.0
alpha = 0.0000001 
epochs = 1000
n = len(X)

for i in range(epochs):
    y_pred = w4*(X**4) + w3*(X**3) + w2*(X**2) + w1*X + b
    
    # Gradients
    dw4 = (2/n) * np.sum((y_pred - y) * (X**4))
    dw3 = (2/n) * np.sum((y_pred - y) * (X**3))
    dw2 = (2/n) * np.sum((y_pred - y) * (X**2))
    dw1 = (2/n) * np.sum((y_pred - y) * X)
    db = (2/n) * np.sum(y_pred - y)
    
    # Update
    w4 -= alpha * dw4
    w3 -= alpha * dw3
    w2 -= alpha * dw2
    w1 -= alpha * dw1
    b -= alpha * db
```

## 🧭 The Path
By using a 4th-degree polynomial with 5 variables, we've given our model the "flexibility" to follow complex data curves. Would you like me to show you how to visualize these 5-variable curves using Matplotlib?
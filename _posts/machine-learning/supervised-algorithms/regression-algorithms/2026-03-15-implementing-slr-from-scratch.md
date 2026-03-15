---
layout: post
title: Implementing Simple Linear Regression from Scratch
description: A Complete Guide with Example and Python Code
thumbnail: /assets/images/machine-learning/slr-from-scratch.png
author: Dipak Pulami Magar
date:   2026-03-15 08:12:45 +0545
categories: machine-learning supervised regression
status: draft
---


<!-- # Implementing Simple Linear Regression from Scratch -->

Here are the major steps to implement Simple Linear Regression from scratch.

---

## 1. Prepare the Dataset

You start with input–output data.

* **X** → independent variable (feature)
* **y** → dependent variable (target)

The goal of the model is to **learn the relationship between X and y** so that it can predict the target value for new inputs.

---

## 2. Define the Model (Linear Equation)

Simple linear regression assumes a **straight-line relationship** between the input and output:

$$
\hat{y} = wx + b
$$

Where:

* **w** → weight (slope of the line)
* **b** → bias (intercept)
* **x** → input feature
* **ŷ** → predicted value

**Intuition:**

* **w (slope)** controls how steep the line is.
* **b (intercept)** shifts the line up or down.
* The algorithm adjusts the line so that it passes as close as possible to all data points.

Visually:

* Data → scattered points
* Model → straight line
* Training → moving the line until it fits the points best

---

## 3. Initialize Parameters

Before training begins, we start with initial parameter values:

```python
w = 0
b = 0
α = 0.01  # learning rate
```

Where:

* **w** → weight
* **b** → bias
* **α** → learning rate (controls how large each update step is)

---

## 4. Make Predictions

Using the model equation, we compute predictions for each input:

$$
\hat{y} = wx + b
$$

This gives the **predicted output** for every data point.

---

## 5. Understand Residuals

A **residual** is the difference between the actual value and predicted value:

$$
\text{Residual} = y - \hat{y}
$$

Residuals tell us **how wrong each prediction is**:

* Positive residual → prediction too small
* Negative residual → prediction too large

---

## 6. Calculate the Loss (Error)

We measure how far the predictions are from the true values using **Mean Squared Error (MSE)**:

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

Where:

* **n** = number of samples
* **yᵢ** = actual value
* **ŷᵢ** = predicted value

The goal of training is to **find values of w and b that minimize this loss**, i.e., make residuals as small as possible.

---

## 7. Compute Gradients (Derivatives)

To reduce the loss, we calculate how sensitive the loss is to changes in the parameters.

Gradients show **how the parameters should change to reduce the loss**.

$$
\frac{\partial L}{\partial w} = \frac{2}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)x_i
$$

$$
\frac{\partial L}{\partial b} = \frac{2}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)
$$

**Why 2/n?**

1. The MSE is $(\frac{1}{n}\sum (y_i - \hat{y}_i)^2)$
2. Differentiating $((y_i - \hat{y}_i)^2)$ gives **$2*(ŷ - y)$**
3. Multiply by **$1/n$** from the mean → **$2/n$**

This scaling ensures the gradient points in the correct direction and is proportional to the average error.

---

## 8. Update Parameters (Gradient Descent)

We update the parameters in the opposite direction of the gradients:

$$
w = w - \alpha \frac{\partial L}{\partial w}
$$

$$
b = b - \alpha \frac{\partial L}{\partial b}
$$

Intuition:

* If prediction > actual → gradient pushes line downward
* If prediction < actual → gradient pushes line upward

The learning rate α controls **how big each adjustment is**.

---

## 9. Repeat for Many Iterations

Each full pass through the dataset is called an **epoch**.

During each epoch:

1. Predict values
2. Compute loss
3. Compute gradients
4. Update parameters

Repeat for many epochs until the **loss converges** (stops decreasing significantly).

---

## 10. Use the Model for Prediction

After training is complete, the model has learned the optimal **w** and **b**.

For any new input x:

$$
\hat{y} = wx + b
$$

This allows the model to **estimate target values for unseen data**.

---

## Final Algorithm (Summary)
1. Load dataset **$(X, y)$**
2. Initialize **w**, **b**, and **learning rate**
3. Loop for a number of **epochs**
4. Compute predictions
5. Compute residuals and loss (MSE)
6. Compute gradients
7. Update parameters using gradient descent
8. Repeat until loss converges
9. Use the trained model for predictions
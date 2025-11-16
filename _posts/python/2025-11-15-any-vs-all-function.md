---
layout: post
title: any() vs all()
description: 
thumbnail: ../../../../assets/images/python/any-vs-all.png
author: Dipak Pulami Magar
date:   2025-11-15 10:12:45 +0545
categories: python
status: draft
---

- The `any()` and `all()` functions in Python are built-in functions used to check the truthiness of elements within an iterable object (e.g., a list, tuple, or dictionary).
- Both any() and all() are short-circuiting functions, meaning they stop processing the iterable as soon as the result can be determined, which can lead to performance optimizations in certain scenarios. 
- They are particularly useful for concisely expressing conditions that would otherwise require loops.
- They **enhance code readability** by providing a concise way to express logical checks on iterables.


# 1. any() function

## 1.1. Introduction
- Returns **True**: if any one of the item in an iterable is True.
- Returns **False**: if all items in an iterable are false 
    - or iterable is *empty*.
- Similar to a **logical OR** operator
- **Syntax**: any(iterable)

**Example**:
```py
list1 = [5 < 10, 10 > 20, 50 < 100] # list1 = [True, False, True]
list2 = [5 > 10, 10 > 20, 50 > 100] # list2 = [False, False, False]
list3 = [] # list3 = [empty]

print(any(list1)) # Output ---> True
print(any(list2)) # Output ---> False
print(any(list3)) # Output ---> False
```
**Output**,
```
True
False
False
```

## 1.2. Use Cases
### 1.2.1. Checking for at least one match
Determining if any element in a list, tuple, or other iterable satisfies a given condition.

```py
products = [{"name": "Laptop", "in_stock": False}, \
            {"name": "Mouse", "in_stock": True}]

if any(product["in_stock"] for product in products):
    print("At least one product is in stock.")
```
### 1.2.2. Validating user input
Ensuring that at least one required field in a form or input is provided.

```py
user_inputs = ["", "John Doe", ""]
if any(user_input for user_input in user_inputs):
    print("At least one input field is filled.")
```
### 1.2.3. Error detection
Identifying if any error condition exists within a collection of status flags.

```py
error_flags = [False, False, True, False]
if any(error_flags):
    print("An error occurred.")
```

---

# 2. all() function
## 2.1. Introduction
- Returns **True**: if every item in an iterable is True 
  - or iterable is *empty*.
- Returns **False**: if any one of the item in an iterable is False.
- Similar to a **logical AND** operator
- **Syntax**: any(iterable)

**Example**:
```py
list1 = [5 < 10, 10 < 20, 50 < 100] # list1 = [True, True, True]
list2 = []
list3 = [5 < 10, 10 > 20, 50 < 100] # list2 = [True, False, True]

print(all(list1)) # Output ---> True
print(all(list2)) # Output ---> True
print(all(list3)) # Output ---> False
```
**Output**:
```
True
True
False
```

## 2.2. Use Cases
**1. Verifying complete adherence to a condition**  
Confirming that every element in an iterable meets a specific criterion.

```py
grades = [85, 92, 78, 95]

if all(grade >= 70 for grade in grades):
    print("All students passed.")
```

**2. Data validation**:  
Ensuring that all values in a data structure are valid or non-empty.

```py
user_data = {"name": "Alice", "email": "alice@example.com", \
            "phone": "123-456-7890"}

if all(user_data.values()):
    print("All user data fields are filled.")
```
**3. Checking for uniform status:**  
Confirming that all items in a system or process are in a particular state.

```py
device_statuses = ["online", "online", "online"]
if all(status == "online" for status in device_statuses):
    print("All devices are online.")
```


Guide to Line Plot in Matplotlib

Matplotlib is the most popular Python library for creating static, animated, and interactive visualizations. Its core module, **matplotlib.pyplot**, provides a MATLAB-style interface for creating quick and powerful plots.

---

# 📌 **1. Importing Matplotlib**

### ✔ Basic Syntax

```python
import matplotlib.pyplot as plt
```

### ✔ Optional — Improve plot readability

```python
plt.style.use('ggplot')  # Simple, clean grid theme
```

---

# **2. Basic Line Plot (Default Settings)**

### ✔ Syntax

```python
plt.plot(x, y)
plt.show()
```


Example: Temperature change during the day

```python
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
temperature = [17, 18, 21, 24, 27, 29]

plt.plot(hours, temperature)
plt.xlabel("Hour of Day")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Throughout the Day")

plt.show()
```

---

# 📌 **3. Plot WITHOUT the X-Axis**

You can hide either axis using:

```python
plt.gca().axes.xaxis.set_visible(False)
```

### ✔ Example: Stock price changes (X-axis hidden)

```python
import matplotlib.pyplot as plt

prices = [115, 122, 118, 128, 122, 132, 128]

plt.plot(prices, marker='o', linestyle='-')
plt.title("Stock Price Movement (X-axis Hidden)")
plt.ylabel("Price ($)")
plt.gca().axes.xaxis.set_visible(False)

plt.show()
```
**Output**:




📌 **Use-case**: Showing trends without worrying about the time scale.

---

# 📌 **4. Plot WITH X-Axis (custom labels)**

### ✔ Real-world example: Company quarterly sales

```python
import matplotlib.pyplot as plt

quarters = ["Q1", "Q2", "Q3", "Q4"]
sales = [25000, 27000, 30000, 35000]

plt.plot(quarters, sales, marker='o')
plt.xlabel("Quarter")
plt.ylabel("Sales (USD)")
plt.title("Quarterly Sales Trend")
plt.grid(True)

plt.show()
```

---

# **5. Changing Line Colors**

Matplotlib supports:

| Example           | Color     |
| ----------------- | --------- |
| `"r"`             | Red       |
| `"g"`             | Green     |
| `"b"`             | Blue      |
| `"k"`             | Black     |
| `"y"`             | Yellow    |
| `"#FF5733"`       | Hex color |
| `(0.2, 0.5, 0.7)` | RGB tuple |

### ✔ Example

```python
plt.plot(x, y, color='red')
```

### ✔ Real-world example: Website traffic trend

```python
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]
visitors = [120, 150, 180, 160, 200, 240, 260]

plt.plot(days, visitors, color="#2E86C1", linewidth=2)
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.title("Weekly Website Traffic")
plt.show()
```

---

# **6. Changing Line Styles**

| Style  | Meaning         |
| ------ | --------------- |
| `"-"`  | Solid (default) |
| `"--"` | Dashed          |
| `"-."` | Dash-dot        |
| `":"`  | Dotted          |

### ✔ Example

```python
plt.plot(x, y, linestyle='--')
```

### ✔ Real-world example: Comparing cost trends

```python
import matplotlib.pyplot as plt

months = [1,2,3,4,5]
electricity = [800, 820, 790, 850, 870]

plt.plot(months, electricity, linestyle='--', color='g')
plt.title("Electricity Cost Trend")
plt.xlabel("Month")
plt.ylabel("Cost (Rs)")
plt.show()
```

---

## **7. Line Width, Marker Style & Marker Size**

### ✔ Syntax

```python


plt.plot(x, y, 
         color='red', 
         linestyle='--',
         linewidth=2,
         marker='o',
         markersize=10)
```

---

# 📌 **8. MULTIPLE LINES in a Single Plot**

### ✔ Example

```python



plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)

```

### ✔ Real-world example: Compare sales of 3 products

```python
import matplotlib.pyplot as plt

months = [1,2,3,4,5,6]

product_A = [40, 42, 45, 50, 55, 58]
product_B = [30, 35, 40, 38, 42, 44]
product_C = [20, 25, 22, 24, 30, 32]

plt.plot(months, product_A, label="Product A", color="r", linestyle='-')
plt.plot(months, product_B, label="Product B", color="g", linestyle='--')
plt.plot(months, product_C, label="Product C", color="b", linestyle=':')

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales (Units)")
plt.legend()
plt.grid(True)

plt.show()
```

---

# 📌 **9. Plotting Without Connecting Lines (Scatter Effect)**

```python
plt.plot(x, y, marker='o', linestyle='')  # OR linestyle='None'
```

### ✔ Example

```python
plt.plot(hours, temperature, marker='s', linestyle='None')
plt.title("Temperature Readings (No line)")
plt.show()
```

---

# 📌 **10. Plot with Custom Figure Size**

### ✔ Syntax

```python
plt.figure(figsize=(8,4))
```

### ✔ Example

```python
plt.figure(figsize=(10,5))
plt.plot(x, y)
```

---

# 📌 **11. Adding Titles, Labels, Grids**

### ✔ Syntax

```python
plt.title("Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.grid(True)
```

---

# 📌 **12. Saving Plot to File**

```python
plt.savefig("myplot.png", dpi=300)
```

---

# 📌 **13. Real-World Example: Portfolio Growth**

```python
import matplotlib.pyplot as plt

years = [2019, 2020, 2021, 2022, 2023]
stocks = [10000, 12000, 15000, 18000, 22000]
crypto = [5000, 9000, 25000, 20000, 15000]

plt.figure(figsize=(8,5))

plt.plot(years, stocks, label="Stocks", color="blue", linestyle='-')
plt.plot(years, crypto, label="Crypto", color="orange", linestyle='--')

plt.xlabel("Year")
plt.ylabel("Portfolio Value (USD)")
plt.title("Portfolio Growth Comparison")
plt.grid(True)
plt.legend()
plt.show()
```

---

# 📌 **14. Complete Syntax Summary**

```python
plt.plot(
    x, y,
    color='r',           # line color
    linestyle='--',      # -, --, -., :
    linewidth=2,
    marker='o',          # o, s, ^, *, etc.
    markersize=8,
    label="Series name"
)
plt.xlabel("")
plt.ylabel("")
plt.title("")
plt.grid(True)
plt.legend()
plt.gca().axes.xaxis.set_visible(False)   # hide x-axis
plt.figure(figsize=(8,4))                 # set figure size
plt.savefig("figure.png", dpi=300)
plt.show()
```
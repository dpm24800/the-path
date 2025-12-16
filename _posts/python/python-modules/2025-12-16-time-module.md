---
layout: post
title:  Python time Module
description: Complete Guide with Examples
thumbnail: /assets/images/python/time-module.png
author: Dipak Pulami Magar
date:   2025-12-16 10:12:45 +0545
categories: python modules
status: draft
---

The **`time` module** in Python provides functions to work with **time-related tasks**, such as measuring execution time, delaying program execution, working with timestamps, and converting between different time formats. It is part of Python’s **standard library** and is widely used in performance testing, logging, scheduling, and automation scripts.

To use it:

```python
import time
```

## 1. Understanding Time in Python
In Python, time is commonly represented as a **timestamp**:
the number of seconds that have passed since **January 1, 1970, 00:00:00 (UTC)**.
This reference point is called the **Unix Epoch**.

## 2. Getting the Current Time

### 2.1 `time.time()`

Returns the **current time in seconds** since the Unix Epoch as a floating-point number.

```python
import time

current_time = time.time()
print(current_time)
```
Ouput:
```
1765889855.670495
```

**Use cases:**
* Measuring execution time
* Creating unique timestamps
* Logging events

## 3. Pausing Program Execution
### 3.1 `time.sleep(seconds)`
Suspends program execution for the given number of seconds.

```python
import time

print("Start")
time.sleep(2)
print("End after 2 seconds")
```
```
Start
End after 2 seconds
```

**Use cases:**
* Rate limiting (e.g., API calls)
* Delays in automation scripts
* Simulating waiting time

## 4. Measuring Execution Time
### 4.1 Simple Timing with `time.time()`

```python
start = time.time()

for i in range(1000000):
    pass

end = time.time()
print("Execution time:", end - start, "seconds")
```
Output:
```
Execution time: 0.1364123821258545 seconds
```

### 4.2 `time.perf_counter()`

Returns a **high-resolution timer** suitable for precise performance measurement.

```python
start = time.perf_counter()
time.sleep(1)
end = time.perf_counter()

print("Elapsed:", end - start)
```
Output:
```
Elapsed: 1.0012454999960028
```

**Why use it?**

* More accurate than `time.time()`
* Ideal for benchmarking code

---

## 5. Working with Structured Time

### 5.1 `time.localtime([seconds])`

Converts a timestamp to **local time** as a `struct_time` object.

```python
local_time = time.localtime()
print(local_time)
```
Output:
```
time.struct_time(tm_year=2025, tm_mon=12, tm_mday=16, tm_hour=18, tm_min=44, tm_sec=58, tm_wday=1, tm_yday=350, tm_isdst=0)
```

Output includes:
* Year, month, day
* Hour, minute, second
* Day of week, day of year

### 5.2 `time.gmtime([seconds])`

Converts a timestamp to **UTC (Greenwich Mean Time)**.

```python
utc_time = time.gmtime()
print(utc_time)
```
Output:
```
time.struct_time(tm_year=2025, tm_mon=12, tm_mday=16, tm_hour=13, tm_min=0, tm_sec=32, tm_wday=1, tm_yday=350, tm_isdst=0)
```

## 6. Formatting Time for Humans

### 6.1 `time.strftime(format, struct_time)`

Formats time into a **readable string**.

```python
now = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", now)
print(formatted)
```
Output:
```
2025-12-16 18:46:00
```
Common format codes:

* `%Y` – Year
* `%m` – Month
* `%d` – Day
* `%H` – Hour
* `%M` – Minute
* `%S` – Second

### 6.2 `time.asctime([struct_time])`

Converts a `struct_time` to a readable string.

```python
print(time.asctime(time.localtime()))
```
Output:
```
Tue Dec 16 18:46:26 2025
```

### 6.3 `time.ctime([seconds])`

Converts a timestamp directly to a readable string.

```python
print(time.ctime(time.time()))
```
Output:
```
Tue Dec 16 18:46:54 2025
```

## 7. Parsing Time Strings

### 7.1 `time.strptime(string, format)`

Parses a time string into a `struct_time`.

```python
date_string = "2025-12-16"
parsed = time.strptime(date_string, "%Y-%m-%d")
print(parsed)
```

**Use cases:**

* Reading dates from files
* Parsing user input
* Processing logs

---

## 8. Converting Structured Time to Timestamp

### 8.1 `time.mktime(struct_time)`

Converts `struct_time` to seconds since the epoch.

```python
t = time.localtime()
timestamp = time.mktime(t)
print(timestamp)
```

---

## 9. CPU and Process Time

### 9.1 `time.process_time()`

Returns CPU time used by the current process.

```python
start = time.process_time()

for i in range(10**6):
    pass

end = time.process_time()
print("CPU time:", end - start)
```

**Note:** Does not include sleep time.

---

## 10. Time Module Constants

* **`time.timezone`** – Offset of local timezone from UTC (in seconds)
* **`time.daylight`** – Whether daylight saving time is used
* **`time.tzname`** – Names of local timezones

```python
print(time.timezone)
print(time.tzname)
```

---

## 11. Practical Examples

### Example 1: Simple Countdown Timer

```python
import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Time's up!")
```

---

### Example 2: Logging with Timestamp

```python
import time

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"[{timestamp}] {message}")

log("Program started")
time.sleep(2)
log("Program ended")
```

---

## 12. When to Use `time` vs `datetime`

| Task                    | Recommended Module |
| ----------------------- | ------------------ |
| Simple delays           | `time`             |
| Performance measurement | `time`             |
| Date arithmetic         | `datetime`         |
| Timezones               | `datetime`         |

---

## 13. Summary

The **`time` module** is best for:

* Measuring execution and performance
* Adding delays
* Working with timestamps
* Formatting and parsing time strings
* Logging and automation tasks

### Key Functions to Remember
* `time.time()`
* `time.sleep()`
* `time.strftime()`
* `time.strptime()`
* `time.perf_counter()`
* `time.localtime()`
* `time.ctime()`

---
layout: post
title: Changing case in VS Code
# description: A practical, example-driven tutorial for data science & machine learning
thumbnail: ../../../../assets/images/pandas/data-cleaning.png
author: Dipak Pulami Magar
date: 2026-02-08 10:12:45 +0545
categories: vscode
status: published
---


**VS Code does have a “sentence case” option**, but **not by default**.

### Built-in options (default)

VS Code only includes:

* **Uppercase**
* **Lowercase**
* **Title Case**

You can access them via:

* **Windows/Linux:** `Ctrl + Shift + P`
* **macOS:** `Cmd + Shift + P`
  → type **“Transform to…”**

You won’t see **Sentence Case** there.

---

### How to get Sentence Case in VS Code

#### ption 1: Install an extension (recommended)

Install **“Change Case”** extension.

**Steps:**

1. Open Extensions (`Ctrl + Shift + X`)
2. Search for **Change Case**
3. Install it
4. Select your text
5. Press `Ctrl + Shift + P`
6. Choose **Change Case → Sentence case**

This converts text like:

```
this is a test. this is another test.
```

```
This is a test. This is another test.
```

---

#### ption 2: Keyboard shortcut (after extension)

Once installed, you can bind a shortcut:

* Go to **Keyboard Shortcuts**
* Search for `sentence case`
* Assign your own key combo

---

### If you want a quick workaround (no extension)

You can:

* Convert to **lowercase**
* Manually capitalize the first letter

…but this **won’t handle multiple sentences correctly**.

<!-- ---

### Recommendation (especially if you write/code a lot)

Use the **Change Case** extension — lightweight, fast, and very useful for documentation, comments, and markdown.

If you want, I can also:

* Show how to do this with **regex**
* Create a **custom VS Code macro**
* Suggest **other writing-friendly extensions**

Just tell me  -->

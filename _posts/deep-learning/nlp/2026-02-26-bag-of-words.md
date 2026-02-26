---
layout: post
title:  Bag of Words (BoW)
description: 
thumbnail: ../../../../assets/images/deep-learning/nlp/bow.png
author: Dipak Pulami Magar
date:   2026-02-25 13:12:45 +0545
categories: deep-learning nlp
status: published
---

## Overview
* Bag of Words is a feature extraction method that converts text into a vector of word counts.
* It is a simple way to represent text as numbers by counting how many times each word appears in a document.
* It **ignores grammar and word order** and only keeps:
  * which words appear, and
  * how often they appear.
* This is the base idea behind models like text classification, spam detection, and sentiment analysis.

## Example
Suppose you have these documents:
* D1: `"Blue sky"`
* D2: `"Bright sun today"`
* D3: `"Bright sun sky"`
* D4: `"Can see bright sun shining"`

### Step 1: Build the vocabulary (all unique words)
Remove stop words (common words that don't add much meaning).

Then, build the vocabulary from the remaining words:

* Vocabulary: `[blue, sky, bright, sun, today, can, see, shining]`
* Sorted alphabetically:
  `[blue, bright, can, see, shining, sky, sun, today]`

### Step 2: Represent each document as word counts

| Sentence | blue | bright | can | see | shining | sky | sun | today |
| -------- | ---- | ------ | --- | --- | ------- | --- | --- | ----- |
| D1       | 1    | 0      | 0   | 0   | 0       | 1   | 0   | 0     |
| D2       | 0    | 1      | 0   | 0   | 0       | 0   | 1   | 1     |
| D3       | 0    | 1      | 0   | 0   | 0       | 1   | 1   | 0     |
| D4       | 0    | 1      | 1   | 1   | 1       | 0   | 1   | 0     |

So:
* `D1` → `[1, 0, 0, 0, 0, 1, 0, 0]`
* `D2` → `[0, 1, 0, 0, 0, 0, 1, 1]`
* `D3` → `[0, 1, 0, 0, 0, 1, 1, 0]`
* `D4` → `[0, 1, 1, 1, 1, 0, 1, 0]`

This numeric vector is the **Bag of Words representation**.

## Key points
* Word order is ignored:
  * “bright sun today” gives the same vector as “today bright sun”.
* Only frequency matters.
* Very easy to compute and widely used in basic NLP and ML models.

## In one line
> Bag of Words = vocabulary of all words + frequency of each word in a text.

## Python implementation
```py
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "Blue sky",
    "Bright sun today",
    "Bright sun sky",
    "Can see bright sun shining"
]

# Create Bag of Words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Get feature names (vocabulary)
# Vocabulary should be fitted or provided beforehand
feature_names = vectorizer.get_feature_names_out() 

print("Vocabulary:", feature_names)
print("\nDocument vectors:")
print(X.toarray())
```

**Output:**
```text
Vocabulary: ['blue' 'bright' 'can' 'see' 'shining' 'sky' 'sun' 'today']

Document vectors:
[[1 0 0 0 0 1 0 0]
 [0 1 0 0 0 0 1 1]
 [0 1 0 0 0 1 1 0]
 [0 1 1 1 1 0 1 0]]
```

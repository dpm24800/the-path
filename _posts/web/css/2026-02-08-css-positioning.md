---
layout: post
title: CSS Positioning
# description: A practical, example-driven tutorial for data science & machine learning
thumbnail: ../../../../assets/images/pandas/data-cleaning.png
author: Dipak Pulami Magar
date:   2026-02-08 10:12:45 +0545
categories: css
status: published
---
<!-- 
position: static; 
postition: relative;
position: absolute;
postion: sticky;
position: fixed;


# Centering Items
Centering a div in css is now too easy with positions. -->

CSS positioning controls the placement of elements on a web page, allowing developers to override the normal document flow. The core property is `position`, which accepts five main values: `static`, `relative`, `absolute`, `fixed`, and `sticky`. 

The `top`, `right`, `bottom`, and `left` properties are then used to specify the final location, but they behave differently depending on the `position` value. 

## Types of CSS Positioning
- **`static`**: This is the **default** value for all elements. Elements are positioned according to the normal flow of the page and the `top`, `right`, `bottom`, and `left` properties have **no effect**.
- **`relative`**: The element remains in the normal flow but can be offset from its original position using `top`, `right`, `bottom`, or `left`. The space the element would have occupied is preserved, and the offset does not affect the position of other elements.
- **`absolute`**: The element is **removed entirely from the normal document flow**. It is then positioned relative to its *nearest positioned ancestor* (any ancestor with a position other than `static`). If no such ancestor exists, it is positioned relative to the initial containing block (usually the `<html>` element/viewport). Other elements on the page will behave as if the absolutely positioned element does not exist.
- **`fixed`**: This is similar to `absolute` positioning, but the element is positioned relative to the **viewport** (the browser window itself) and stays in the same place even when the page is scrolled. This is commonly used for persistent navigation menus or floating buttons.
- **`sticky`**: This value toggles between `relative` and `fixed` positioning based on the user's scroll position. It behaves as a relative element until it reaches a specified scroll threshold (e.g., `top: 10px`), at which point it becomes fixed to that position within its parent container. 

## Key Concepts

- **Containing Block**: The ancestor element relative to which an `absolute` or `fixed` element is positioned. For `absolute` positioning to work as expected within a specific container, that container must have its `position` set to something other than `static` (usually `position: relative` is used for this purpose).
- **Z-index**: Positioned elements (anything but `static`) can overlap other elements. The `z-index` property defines the stack order along the imaginary z-axis (coming out of the screen), with higher values appearing on top of lower values. 


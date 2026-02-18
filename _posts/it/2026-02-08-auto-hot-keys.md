---
layout: post
title: Auto Hot Keys
# description: Finding a Specific Text Inside Multiple Files Using PowerShell
date: 2026-02-08 06:12:45 +0545
author: Dipak Pulami Magar
categories: windows
status: published
---

```bash
#Requires AutoHotkey v2.0

^+m:: {
    ; Open context menu (right-click)
    Send "+{F10}"
    Sleep 5 ; 120

    ; New → Text Document
    Send "w"
    Sleep 5 ; 80
    Send "t"
    Sleep 5 ; 120

    ; Rename to Markdown file
	FileName := FormatTime(A_Now, "yyyy-MM-dd_HH-mm-ss")
    Send FileName ".md"
	Send "{Del}{Del}{Del}{Del}{Enter}{Enter}{Enter}"
}

^+b::{
	Send "{#} -------------------------------"
}

^+v::{
	Send "venv\Scripts\Activate.ps1"
}

^+k::{
	Send "jekyll serve"
}

^!d::  ; Ctrl + Alt + D
{
    SendText(FormatTime(A_Now, "yyyy-MM-dd-"))
}
```


```bash
^!h::  ; Ctrl + Alt + H
{
    today := FormatTime(A_Now, "yyyy-MM-dd HH:mm:ss")

    text := "
(
---
layout: post
title: Data Cleaning With Pandas
# description: A practical, example-driven tutorial for data science & machine learning
thumbnail: ../../../../assets/images/pandas/data-cleaning.png
author: Dipak Pulami Magar
date:   " today " +0545
categories: pandas
status: published
---
)"

    SendText(text)
}
```
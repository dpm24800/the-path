---
layout: post
author: Dipak Pulami Magar
title: Fast Ways to Locate Text in Files Using Terminal or VS Code
date:   2026-02-07 10:12:45 +0545
categories: windows
status: published
---

The easiest way is to **search inside files by content**. Here are the quickest methods depending on what you’re using:

---

## Linux / macOS (Terminal)

Use `grep`:

```bash
grep -R --include="*.txt" --include="*.md" "Posts in category:" .
```

**What it does:**

* `-R` searches recursively in the folder
* `--include` limits the search to `.txt` and `.md` files
* `"Posts in category:"` is the text you’re looking for
* `.` means the current folder

It will print the **filename** where the text exists.

If you only want filenames:

```bash
grep -Rl --include="*.txt" --include="*.md" "Posts in category:" .
```

---

## Windows (PowerShell)

```powershell
Select-String -Path *.txt, *.md -Pattern "Posts in category:" -List
```

This shows which file contains that text.

---

## VS Code

1. Open the folder in VS Code
2. Press **Ctrl + Shift + F**
3. Search:

```
Posts in category:
```

4. Filter files:

```
*.txt, *.md
```

<!-- ---

If you want, tell me:

* your OS (Windows / Linux / Mac)
* whether files are in subfolders

and I can give you a clean one-line command for your exact setup. -->

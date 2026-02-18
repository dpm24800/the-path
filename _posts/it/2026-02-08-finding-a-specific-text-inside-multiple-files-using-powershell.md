---
layout: post
author: Dipak Pulami Magar
title: Finding a Specific Text Inside Multiple Files Using PowerShell
date:   2026-02-08 06:12:45 +0545
categories: windows
status: published
---

When working with many `.txt` and `.md` files, opening them one by one to locate a specific phrase is slow and inefficient. PowerShell allows you to search inside files recursively and instantly identify where a string appears.

### Basic Recursive Search
Use `Get-ChildItem` together with `Select-String`:

```powershell
Get-ChildItem "C:\Users\ABC\Desktop\my-repos\the-path" -Recurse -File |
Select-String -Pattern "Posts.*category"
```

**How it works:**

* `Get-ChildItem -Recurse -File` collects all files inside the folder and its subfolders.
* The pipeline (`|`) sends those files to `Select-String`.
* `Select-String -Pattern` searches inside each file using a regex pattern.

In this example, the pattern `Posts.*category` matches any text where “Posts” appears before “category”, even if extra words or spaces exist between them.

### Show Only the Matching Filenames

If you only need the file paths without preview lines:

```powershell
Get-ChildItem "C:\Users\ABC\Desktop\my-repos\the-path" -Recurse -File |
Select-String -Pattern "Posts.*category" |
Select-Object -ExpandProperty Path -Unique
```

### Limit the Search to Specific File Types

```powershell
Get-ChildItem "C:\Users\ABC\Desktop\my-repos\the-path" -Recurse -File |
Where-Object { $_.Extension -in ".txt",".md" } |
Select-String -Pattern "Posts.*category"
```

This approach is reliable because it avoids issues with `-Include` filters and works consistently across folders.

<!-- ---

If you want, I can also give you a stronger blog subsection like “Why your exact phrase search failed (and how regex fixed it)” — it would fit very well after this part. -->

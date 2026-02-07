---
layout: post
author: Dipak Pulami Magar
title: How to Fix the Airplane Mode Loop Bug on Windows Laptops
# youtube: https://www.youtube.com/watch?v=bgmfiENIkuc
date:   2026-02-07 10:12:45 +0545
categories: windows troubleshooting
status: published
---

If your laptop’s **Airplane mode keeps turning ON and OFF by itself**, you’re not alone — and it’s usually not a keyboard problem.

This issue is almost always caused by a **Windows service bug** related to wireless and hotkey handling.
Tools like AutoHotkey or key-remapping apps **cannot fix it**.

Here is a simple and very effective fix.

---

## Why this happens

Windows uses a background service to manage:

* Airplane mode
* Wireless radios (Wi-Fi, Bluetooth, etc.)
* Hardware hotkeys for network toggling

When that service becomes unstable, it can repeatedly trigger Airplane mode, causing the annoying on–off loop.

---

## Quick fix (works in most cases)

Follow these steps exactly.

### Step 1 – Open Windows services

Press:

**Win + R**

Type:

```
services.msc
```

Press **Enter**.

---

### Step 2 – Find the correct service

In the list, locate:

**Radio Management Service**

---

### Step 3 – Disable it

Double-click **Radio Management Service**.

Change:

**Startup type → Disabled**

Then click:

* Stop
* OK

---

### Step 4 – Restart your laptop

After the restart, the automatic Airplane mode toggling should be gone.

---

## What this service actually does

The **Radio Management Service** controls:

* automatic radio state switching
* airplane mode logic
* wireless hotkey coordination

When it bugs out, Windows keeps thinking it should enable or disable airplane mode over and over.

Disabling it prevents Windows from applying that broken logic.

---

## Important note (Is it safe?)

Yes. For normal users, this is safe.

After disabling this service:

* Wi-Fi still works
* Bluetooth still works
* You can still turn Wi-Fi on and off manually

Only this part is disabled:

automatic radio control and airplane-mode switching logic

So you are not disabling your network, only the buggy controller.

---

## Why key remapping will not fix this

Many people try:

* AutoHotkey
* SharpKeys
* registry key remapping

But this problem is not caused by your keyboard.

It is a background Windows service repeatedly changing the network state.

That is why remapping keys does nothing.

---

## Summary

If Airplane mode keeps switching on and off by itself on Windows, the fastest and most reliable fix is:

Disable the **Radio Management Service** and restart.

In most cases, the problem stops immediately.

If the issue still continues even after this fix, it usually points to a deeper OEM hotkey driver problem from the laptop manufacturer. However, for most users this single change solves it completely.

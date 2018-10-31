# Wox.Plugin.PRPR Clean

Auto clean PRPR cache pictures.

This script depends on **data** to clean PRPR cache, it will clean up  all the cache **one week ago**.

![screenshots](/Images/zero_20181031_223501.png)

## Example

### Before

Look this, it created at **2018-8-13**.
Now **2018-10-31**, it already had around **4.5GB** files only **two and a half months**.

> ![screenshots](/Images/Wallpaper.png) > ![screenshots](/Images/Lockscreen.png)

### After

**Cleaning**, now.

> ![screenshots](/Images/zero_20181031_223337.png)

## Setting

Two parameters can config.

1. PATH

    > PRPR's local path.

1. LIMIT_DAYS (default 7 days)

    > How long apart from now and delete it.

### Step

1. Install `Wox`.
1. Install `Wox.Plugin.PRPR-Clean`.
1. Open the **Plugin** folder.
1. Open the **clean.py** file.
1. Find the **paramters** and change it.

## Attention

This script will **DELETE** all caches which match the config .

## Requirements

`Python3.x`

## Reference

When dealing with **byte's unit**, using this [code](https://www.cnblogs.com/misspy/p/3661770.html).

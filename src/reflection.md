# Reflection on Data Cleaning with GitHub Copilot

## 1. What Copilot Generated
I used GitHub Copilot to write the basic code for my cleaning functions and to help me fix errors.
- It wrote the starting code for `clean_column_names` and `remove_invalid_rows` after I wrote comments to explain what I wanted.
- The most helpful part was when it fixed a `"NoneType"` error. My code crashed because it couldn't find the file. Copilot saw that `load_data` was failing silently. It told me to change the function so it raises a `FileNotFoundError` instead of just returning `None`.

## 2. What I Modified
I had to change a lot of the code that Copilot wrote because the raw data was much messier than Copilot expected.
- **Fixing Data Types:** Copilot thought the qty and price columns were already numbers. But when I ran the script, I got a `TypeError` because they were actually text. I changed the code to use `pd.to_numeric(..., errors='coerce')`. This forces them to be numbers.
- **Cleaning Strings:** Copilot just used `.strip()`, but that was not enough. The data had quote marks around the words (like "Electronics"). I added `.str.replace('"', '')` to remove the quotes first, and I added `.str.title()` to make the capitalization look correct.
- **Missing Values:** Copilot suggested deleting all rows that had missing information. I didn't want to do that. I changed the logic to fill missing quantities with 0 (meaning no sales), and I only deleted rows if the price was missing.

## 3. What I Learned
This assignment taught me the difference between coding errors and data errors.
- Copilot is good for crashes: When my script stopped working because of the `AttributeError`, Copilot found the file path mistake very fast.
- Copilot is weak on logic: However, Copilot did not notice that my "clean" data still had negative numbers and quote marks. The code ran without crashing, but the results were wrong. I learned that I have to check the data myself, because AI often thinks the data is cleaner than it really is.
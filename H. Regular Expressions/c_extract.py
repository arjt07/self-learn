# Extract info
import re

url = input("URL: ").strip()

# ?: -> non-capturing version of Grouping
matches = re.search(r"^(?:https?://)?(?:www\.)?(?:twitter\.com/)?(\w+)$", url, re.IGNORECASE)

if matches:
    print(f"username: {matches.group(1)}")


 
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"username: {username}")


# # replace() -> 2 arg -> (what do ypu want to Replace), (...Replace it with)
# username = url.replace("https://twitter.com/", "")
# print(f"username: {username}")

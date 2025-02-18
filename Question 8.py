def valid_url(url):
    """
    Checks if the given string is a valid URL using only basic string operations.
    MY REASONING IS THE FOLLOWING 3 POINTS TO CONSIDER:
      1. start "http://" or "https://"
      2. contain at least '.'
      3. character after the last '.'

    :param url: The string to check
    :return: True if valid, False otherwise
    """
    if not (url.startswith("http://") or url.startswith("https://")): #Sirst condition done
        return False
    if '.' not in url: #second condition
        return False
    last_dot_position = url.rfind('.') #third condition
    if last_dot_position == len(url) - 1: #using the inverse of len to find the last position
        return False
    return True #if its all good then it passes

# Asked chatgpt for examples good and bad to see if it worked
test_urls = [
    "http://google.com",
    "https://example.org",
    "google.com",
    "https://invalidurl.",
    "http://sitewithoutdot",
]

for url in test_urls:
    print(url, valid_url(url))
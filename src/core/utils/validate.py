import re

def validate_username(username):
  regex = r"^[a-z0-9]{3,31}$"
  return bool(re.match(regex, username))
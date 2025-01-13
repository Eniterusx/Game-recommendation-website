import re
import requests

def extract_steam_id(profile_url):
    numeric_pattern = r"steamcommunity\.com/profiles/(\d+)"
    custom_pattern = r"steamcommunity\.com/id/([\w\d_-]+)"
    
    match_numeric = re.search(numeric_pattern, profile_url)
    if match_numeric:
        return match_numeric.group(1)

    match_custom = re.search(custom_pattern, profile_url)
    if match_custom:
        custom_id = match_custom.group(1)
        resolved_id = resolve_custom_url_to_steam_id(custom_id)
        return resolved_id

    return None

def resolve_custom_url_to_steam_id(custom_id):
    url = f"https://steamcommunity.com/id/{custom_id}?xml=1"
    response = requests.get(url)
    if response.status_code == 200:
        steam_id_match = re.search(r"<steamID64>(\d+)</steamID64>", response.text)
        if steam_id_match:
            return steam_id_match.group(1)
    return None

def get_steam_nickname(steam_id):
    url = f"https://steamcommunity.com/profiles/{steam_id}?xml=1"
    response = requests.get(url)
    if response.status_code == 200:
        nickname_match = re.search(r"<steamID><!\[CDATA\[(.*?)\]\]></steamID>", response.text)
        if nickname_match:
            return nickname_match.group(1)
    return None
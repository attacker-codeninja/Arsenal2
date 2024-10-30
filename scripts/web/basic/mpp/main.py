import requests
import re
import base64
import json
import os

def fetch_content(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch content from {url}: {e}")
        return None

# Step 1: Fetch main page HTML from a user-provided link.
main_url = input("Enter URL: ")
page_content = fetch_content(main_url)
if not page_content:
    exit("Failed to retrieve page content.")

# Step 2: Extract the 'embed_code' from the page.
embed_match = re.search(r'<script src="https://example.com/(.*)/embed', page_content)
if not embed_match:
    exit("Embed code not found in page content.")
embed_code = embed_match.group(1)

# Step 3: Set up headers with a referer for requests to bypass restrictions.
headers = {'referer': f'https://example.com/{embed_code}'}

# Step 4: Fetch embedded JavaScript code using the extracted embed_code.
embed_response = fetch_content(f'https://example.com/{embed_code}/embed', headers=headers)
if not embed_response:
    exit("Failed to retrieve embedded script.")

# Step 5: Extract the encoded JSON data.
json_encoded_match = re.search(r'window\[\".*\"\]\=\"(.*)\"\;\(function\(', embed_response)
if not json_encoded_match:
    exit("Encoded JSON not found in embedded script.")
json_encoded_text = json_encoded_match.group(1)
try:
    json_decoded_text = base64.b64decode(json_encoded_text.encode()).decode()
    json_data = json.loads(json_decoded_text)
except (base64.binascii.Error, json.JSONDecodeError) as e:
    exit(f"Error decoding JSON data: {e}")

# Step 6: Parse JSON data to extract keys for further requests.
msgn = json_data.get('msgn')
playlist_url = json_data.get('playlist') + '.m3u8'

# Step 7: Fetch the playlist data and decode it.
playlist_content = fetch_content(f'https://example.com/{playlist_url}', headers=headers)
if not playlist_content:
    exit("Failed to retrieve playlist content.")

try:
    decoded_playlist = base64.b64decode(playlist_content.encode()).decode()
except base64.binascii.Error:
    exit("Failed to decode playlist content.")

# Step 8: Process the playlist content (remove parts of filenames).
prefix = decoded_playlist.split('-')[0]
processed_playlist = decoded_playlist.replace(f"{prefix}-", '')

# Step 9: Optional: Manually input playlist URL, fetch, and decode.
playlist_url_manual = input("Enter playlist URL: ")
playlist_content_manual = fetch_content(playlist_url_manual, headers=headers)
if playlist_content_manual:
    try:
        decoded_playlist_manual = base64.b64decode(playlist_content_manual).decode()
        prefix_manual = decoded_playlist_manual.split('-')[0]
        processed_playlist_manual = decoded_playlist_manual.replace(f"{prefix_manual}-", '')
    except base64.binascii.Error:
        print("Failed to decode manual playlist content.")

# Step 10: Obtain and save the encryption key from the playlist.
playlist_filename = input("Enter playlist filename: ")
try:
    playlist_text = open(playlist_filename).read()
    key_url = playlist_text.split('URI="')[1].split('",IV')[0]
    os.makedirs('res', exist_ok=True)
    with open('res/key.key', 'wb') as key_file:
        key_file.write(requests.get(key_url, headers=headers).content)
    playlist_text = playlist_text.replace(key_url, 'res/key.key')
except (IndexError, FileNotFoundError) as e:
    exit(f"Failed to process key from playlist file: {e}")

# Step 11: Download and save each .ts file locally
ts_files = re.findall(r'(/\d+.*)', playlist_text)
for i, ts in enumerate(ts_files):
    try:
        with open(f'res/{i}.ts', 'wb') as ts_file:
            ts_file.write(requests.get(f'https://example.com{ts}', headers=headers).content)
        playlist_text = playlist_text.replace(ts, f'res/{i}.ts')
    except requests.RequestException as e:
        print(f"Failed to download {ts}: {e}")

# Step 12: Save the modified playlist to a file
with open('res/processed_playlist.m3u8', 'w') as final_playlist:
    final_playlist.write(playlist_text)

print("Playlist processing complete. All files saved in 'res' directory.")
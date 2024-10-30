# Media Playlist Processor

A Python script to fetch, decode, and reconstruct media playlists from a specified website. This tool extracts and processes embedded media, decoding base64-encoded playlist data and saving media segments locally for offline playback.

## Features
- Fetches HTML from a user-provided URL and extracts embedded JavaScript.
- Decodes base64-encoded JSON data to retrieve playlist information.
- Downloads and reassembles `.ts` media files, updating the playlist to use local paths.
- Saves encryption keys and playlists for offline use.

## Usage

    Run the script and follow the prompts to enter:
        The main page URL.
        (Optional) A manual playlist URL.
        A filename for the playlist you wish to process.

    The script will:
        Extract and decode JSON data from the page.
        Fetch and decode the playlist.
        Download all .ts media segments and update paths in the playlist.
        Save the processed playlist in the res directory for offline playback.

## Run the script with:

`python3 main.py`

## Example

```
Enter URL: https://example.com/video
Enter playlist URL: https://example.com/path/to/playlist.m3u8
Enter playlist filename: playlist.m3u8
```

## Output

All media files, keys, and the updated playlist will be saved in the res directory. You can play the media locally using a compatible media player.

Notes

    Error Handling: The script includes error handling for network and decoding issues.
    Permissions: Some websites may restrict access based on headers or referers. This script sets a referer header to bypass such restrictions.
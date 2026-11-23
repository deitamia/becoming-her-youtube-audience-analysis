
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# 1. Load the API key from our .env file
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

# 2. Check whether the API key exists
if not API_KEY:
    raise ValueError("YouTube API key not found. Check your .env file.")

# 3. Connect to YouTube Data API v3
youtube = build("youtube", "v3", developerKey=API_KEY)

# 4. Request information about a public YouTube channel
request = youtube.channels().list(
    part="snippet,statistics",
    forHandle="@YouTube"
)

response = request.execute()

# 5. Display the result
for channel in response.get("items", []):
    print("Successfully connected to YouTube!")
    print("Channel:", channel["snippet"]["title"])
    print("Subscribers:", channel["statistics"].get("subscriberCount", "Hidden"))
    print("Total views:", channel["statistics"].get("viewCount", "Unavailable"))
    print("Total videos:", channel["statistics"].get("videoCount", "Unavailable"))

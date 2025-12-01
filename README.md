# MediaSurfer
MediaSurfer is a powerful Python library that allows you to easily download media from multiple social platforms.

- **Instagram**: Download photos and videos from profiles.
- **TikTok**: Download videos in their original quality.
- **YouTube**: Download videos or audio in multiple formats.
- **Spotify**: Download tracks.
- **Pinterest**: Download images and boards.
- **Facebook**: Download videos from profiles and pages.

## Installation

You can install MediaSurfer via pip (once it's published on PyPI):

```bash
pip install MediaSurfer
```

## API Documentation (Swagger UI)

This project exposes an HTTP API with endpoints to download media from various platforms. A hosted interactive Swagger UI is available when the Flask app is running:

- Swagger UI: http://localhost:5000/docs
- OpenAPI JSON: http://localhost:5000/openapi.json

Endpoints available:

- `POST /yt` - Download YouTube (body: {"url": "...", "type": "audio|video", "quality": "optional"})
- `POST /insta` - Download Instagram (body: {"url": "..."})
- `POST /tiktok` - Download TikTok (body: {"url": "..."})
- `POST /spotify` - Download Spotify (body: {"url": "..."})
- `POST /facebook` - Download Facebook (body: {"url": "..."})
- `POST /pinterest` - Download Pinterest (body: {"url": "..."})

Example curl usage:

```bash
curl -X POST http://localhost:5000/yt -H "Content-Type: application/json" \
    -d '{"url":"https://www.youtube.com/watch?v=...","type":"video","quality":"1080p"}'
```

Visit the `/docs` page for interactive testing of the endpoints and to view schemas.

## Running the app locally

To run the application locally (development):

```bash
python app.py
```

Then open your browser at http://localhost:5000/docs to view the API docs.

# MediaSurfer
MediaSurfer is a powerful Python library that allows you to easily download media from multiple social platforms.

- **Instagram**: Download photos and videos from profiles.
- **TikTok**: Download videos in their original quality.
- **YouTube**: Download videos or audio in multiple formats.
- **Spotify**: Download tracks.
- **Pinterest**: Download images and boards.
- **Facebook**: Download videos from profiles and pages.

## Installation

You can install MediaSurfer via pip (once it's published on PyPI):

```bash
pip install MediaSurfer

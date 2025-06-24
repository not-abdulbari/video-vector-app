from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from utils.video_utils import extract_frames
from utils.feature_utils import compute_histogram
from utils.qdrant_utils import store_vector, search_similar
from r2_upload import upload_to_r2
import os

app = FastAPI()

@app.post("/upload-video")
async def upload_video(file: UploadFile = File(...)):
    video_path = f"temp_{file.filename}"
    with open(video_path, "wb") as f:
        f.write(await file.read())

    frame_paths = extract_frames(video_path)
    os.remove(video_path)

    uploaded_urls = []
    skipped = 0
    for frame_path in frame_paths:
        vector = compute_histogram(frame_path)
        print(f"Vector for {frame_path}: {vector[:5]}...")

        if not vector:
            print("Empty vector. Skipping...")
            skipped += 1
            continue

        filename = os.path.basename(frame_path)
        url = upload_to_r2(frame_path, f"frames/{filename}")
        store_vector(vector, metadata={"url": url})
        uploaded_urls.append(url)
        os.remove(frame_path)

    return {"message": "Uploaded and processed", "frames_uploaded": len(uploaded_urls), "frames_skipped": skipped}

@app.post("/search", response_class=HTMLResponse)
async def search_vector(vector: list[float]):
    results = search_similar(vector)

    html = "<h1>Search Results</h1><div style='display: flex; flex-wrap: wrap;'>"
    for hit in results:
        url = hit["payload"].get("url", "")
        vec = hit.get("vector", [])
        html += f"""
        <div style=\"margin: 10px; padding: 10px; border: 1px solid #ccc; width: 300px;\">
            <a href=\"{url}\" target=\"_blank\">
                <img src=\"{url}\" alt=\"Frame\" style=\"width:100%; border-radius: 5px;\">
            </a>
            <pre style=\"font-size: 12px; white-space: wrap;\">{vec}</pre>
        </div>
        """
    html += "</div>"
    return HTMLResponse(content=html)

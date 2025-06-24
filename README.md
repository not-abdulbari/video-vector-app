# 🎥 Video Vector Search API

A FastAPI application that extracts frames from a video, computes feature vectors, uploads them to Cloudflare R2, and stores searchable vectors in Qdrant.

---

## 🚀 Features

* Upload and process MP4 videos
* Extract frames at 1-second intervals
* Compute color histogram feature vectors (192-dim)
* Upload frames to Cloudflare R2 (public URLs)
* Store vectors in Qdrant vector database
* Search similar frames via vector comparison
* Display images and vectors with HTML output

---

## 📂 Project Structure

```
video-vector-app/
│
├── main.py                  # FastAPI app
├── r2_upload.py             # Upload to R2 storage
├── .env.example             # Environment variable template
├── requirements.txt         # Python dependencies
├── utils/
│   ├── feature_utils.py     # Histogram vector generation
│   ├── qdrant_utils.py      # Qdrant DB integration
│   └── video_utils.py       # Frame extraction from video
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/not-abdulbari/video-vector-app.git
cd video-vector-app
```

### 2. Setup Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Fill in your credentials for:

* Qdrant (URL, API key, collection name)
* Cloudflare R2 (account ID, keys, bucket name, public URL)

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

Open in browser: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📄 API Endpoints

### `POST /upload-video`

Upload a video and process it:

* Extracts frames
* Uploads to Cloudflare R2
* Stores feature vectors in Qdrant

### `POST /search`

Search for similar frames:

* Input: list of 192 floats (vector)
* Output: images and their vectors (HTML viewable/downloadable)

---

## 🌐 Technologies Used

* **FastAPI** – backend API
* **OpenCV** – frame extraction and histogram
* **NumPy** – vector operations
* **Qdrant** – vector search engine
* **Cloudflare R2** – object storage

---

## 📁 Example `.env` File

```env
# Cloudflare R2 Configuration
R2_BUCKET_NAME=your-bucket-name
R2_ACCESS_KEY_ID=your-access-key-id
R2_SECRET_ACCESS_KEY=your-secret-access-key
R2_ACCOUNT_ID=your-account-id
R2_REGION=auto
R2_PUBLIC_URL=your-public-r2-url # e.g. pub-xxxxxxx.r2.dev

# Qdrant Configuration
QDRANT_URL=https://your-qdrant-url
QDRANT_API_KEY=your-qdrant-api-key
QDRANT_COLLECTION=collection-name
```

---



## ✅ Assignment Requirements (Verified)


Video Processing:

- ✅ Implement an endpoint that accepts a video file upload (e.g., MP4 format).

- ✅ Extract frames from the uploaded video at a specified interval (e.g., every second).

- ✅ Save the extracted frames as images in a specified output directory.

Feature Vector Computation:

- ✅ For each extracted frame, compute a simple feature vector (e.g., using color histograms or any other method of your choice).g., using color histograms or any other method of your choice).

- ✅ Store the feature vectors in a vector database of your choice (Qdrant etc.).).

API for Retrieval:

- ✅ Implement an endpoint that allows querying the vector database for similar frames based on a given feature vector.

- ✅ The endpoint should return the relevant frame images and their corresponding feature vectors.
---
## 👤 Author

**Abdul Bari N**
B.E. Computer Science, CAHCET
GitHub: [@not-abdulbari](https://github.com/not-abdulbari)

---

## 📝 License

This project is open for educational and non-commercial use.

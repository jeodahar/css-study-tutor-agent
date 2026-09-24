"""
ocr.py
Extract text from a photo of a handwritten answer using Groq's vision-capable
model - no local OCR install (like Tesseract) needed, which keeps this
deployable to Streamlit Cloud / Render as-is.
"""

import base64

from groq import Groq

from config import GROQ_API_KEY, GROQ_VISION_MODEL

TRANSCRIBE_PROMPT = (
    "Transcribe all handwritten text in this image as accurately as possible. "
    "Keep the original wording and structure (paragraphs/headings) where visible. "
    "Only output the transcribed text - no commentary, no markdown."
)


def extract_text_from_image(image_bytes: bytes) -> str:
    """image_bytes: raw bytes of a JPG/PNG uploaded via Streamlit's file_uploader."""
    client = Groq(api_key=GROQ_API_KEY)
    b64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.chat.completions.create(
        model=GROQ_VISION_MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": TRANSCRIBE_PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{b64_image}"},
                    },
                ],
            }
        ],
        temperature=0.0,
        max_tokens=2000,
    )
    return response.choices[0].message.content.strip()

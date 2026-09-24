"""
config.py
Central place for API keys and model configuration.
Reads from Streamlit secrets (when deployed on Streamlit Cloud)
or from environment variables (when running locally).
"""

import os

try:
    import streamlit as st
    _HAS_STREAMLIT = True
except Exception:
    _HAS_STREAMLIT = False


def get_secret(key, default=None):
    if _HAS_STREAMLIT:
        try:
            if key in st.secrets:
                return st.secrets[key]
        except Exception:
            pass
    return os.environ.get(key, default)


GROQ_API_KEY = get_secret("GROQ_API_KEY")
GROQ_MODEL = get_secret("GROQ_MODEL", "openai/gpt-oss-120b")
GROQ_VISION_MODEL = get_secret("GROQ_VISION_MODEL", "llama-3.2-90b-vision-preview")

SUPABASE_URL = get_secret("SUPABASE_URL")
SUPABASE_KEY = get_secret("SUPABASE_KEY")

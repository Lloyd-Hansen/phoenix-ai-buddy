"""Utility functions for the Phoenix AI Tutor."""
import os
import time
import logging
import traceback
from dotenv import load_dotenv

import google.generativeai as genai

# Configuration
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment or .env file")

genai.configure(api_key=API_KEY)

MODEL_ID = "models/gemini-2.5-flash"
GEN_CONFIG = {
    "temperature": 0.35,
    "top_p": 0.9,
    "max_output_tokens": 4096
}

LOG_FILE = "phoenix_agent.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def safe_generate(model_obj, prompt: str) -> str:
    """Safely generate content with error handling and logging."""
    start = time.time()
    full_text = ""

    try:
        response = model_obj.generate_content(prompt, stream=True)

        for chunk in response:
            if hasattr(chunk, "text"):
                full_text += chunk.text

        elapsed = time.time() - start
        logging.info(
            "Model call OK | model=%s | time=%.2fs | prompt_len=%d | response_len=%d",
            getattr(model_obj, "model_name", MODEL_ID),
            elapsed,
            len(prompt),
            len(full_text)
        )

        if not full_text.strip():
            return "Sorry, no response generated. Please try with more details."

        return full_text.strip()

    except Exception as e:
        elapsed = time.time() - start
        logging.error("Model call ERROR | time=%.2fs | err=%s", elapsed, str(e))
        logging.error(traceback.format_exc())
        return f"[Agent ERROR] {str(e)}"
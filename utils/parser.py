import json
import requests
import fitz  # PyMuPDF


def extract_text_from_pdf(uploaded_file):
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    except Exception as e:
        print("❌ Error extracting text from PDF:", str(e))
        return None

def parse_resume_with_llama3(resume_text):
    import re

    GROQ_API_KEY = "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"
    MODEL = "llama3-8b-8192"
    GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

    prompt = (
        "You are a resume parser. Return ONLY valid JSON that matches this schema. "
        "NO explanation, no markdown, just JSON:\n\n"
        "{\n"
        "  \"name\": \"\",\n"
        "  \"email\": \"\",\n"
        "  \"phone\": \"\",\n"
        "  \"skills\": [],\n"
        "  \"education\": [{\"degree\": \"\", \"field\": \"\", \"institution\": \"\", \"year\": \"\"}],\n"
        "  \"work_experience\": [{\"position\": \"\", \"company\": \"\", \"duration\": \"\", \"description\": \"\"}]\n"
        "}\n\n"
        f"Resume:\n{resume_text}"
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        result = response.json()
        raw_output = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        # Try to extract JSON using regex if needed
        match = re.search(r"\{.*\}", raw_output, re.DOTALL)
        if not match:
            return {"error": "Invalid JSON received from model", "raw_output": raw_output}

        json_str = match.group(0)
        return json.loads(json_str)

    except Exception as e:
        return {"error": str(e)}

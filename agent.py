from google import genai

client = genai.Client(api_key="AIzaSyAZ0AGZSTueNl4iKZW_yGLHOby-_tnwDU0")

def extract_search_details(message):

    try:
        prompt = f"""
Extract skill and location.
Return only: skill, location
Sentence: {message}
"""
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        result = response.text.strip()

        if "," in result:
            skill, location = result.split(",")
            return skill.strip().lower(), location.strip().lower()

    except:
        pass

    # fallback (VERY IMPORTANT for assignment reliability)
    msg = message.lower()

    skills = ["mapping", "survey", "inspection", "delivery"]
    locations = ["bangalore", "chennai", "mumbai", "delhi"]

    skill = next((s for s in skills if s in msg), None)
    location = next((l for l in locations if l in msg), None)

    return skill, location

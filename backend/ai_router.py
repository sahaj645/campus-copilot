from openai import OpenAI

client = OpenAI()

def process_query(message):

    prompt = f"""
    Classify the student request into one of these categories:

    complaint
    event
    booking
    info

    Message: {message}

    Only return the category.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content.strip()
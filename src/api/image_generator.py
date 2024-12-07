import requests

def generate_image(prompt):
    url = "https://api.deepai.org/api/text2img"
    headers = {"api-key": "502d5b13-770e-470e-b281-cf3ed6937301"}
    data = {"text": prompt}

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("output_url")
    else:
        return {"error": response.status_code}
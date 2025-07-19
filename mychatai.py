import google.generativeai as genai

API_key="AIzaSyAYE3L4uR9X7pwLWF-cOOCrv4lRj27J8Vg"

genai.configure(api_key=API_key)   #initiallize

model=genai.GenerativeModel("gemini-2.5-flash")

query="who build python and when python developed"

response=model.generate_content(query)
print
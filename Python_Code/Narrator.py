import openai
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse, urljoin


openai.api_key = "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"
# Function to search for an image related to a given query
# Function to search for an image related to a given query
# Function to search for an image related to a given query
def search_image(query):
    url = f"https://www.google.com/search?q={query}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_element = soup.find('img')
    image_url = None
    if image_element:
        image_url = image_element.get('src')
        if image_url:
            parsed_url = urlparse(image_url)
            if not parsed_url.scheme:
                base_url = response.url
                image_url = urljoin(base_url, image_url)
    return image_url

# Process each paragraph and search for related images
def process_paragraphs(paragraphs):
    # Create the "images" directory if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")
    for i, paragraph in enumerate(paragraphs):
        query = paragraph.strip()
        image_url = search_image(query)
        if image_url:
            # Download the image and save it locally
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(f"images/image_{i}.jpg", 'wb') as f:
                    f.write(response.content)
                    print(f"Image_{i}.jpg saved.")
                    
def extract_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def extract_important_topics(questions):
    text = questions
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"You are a teacher , who will take a Topic to a student, i will provide you with basic summary of student's lecture note which may be bit incomplete , by you have to use it and interact with student and make sure he understand it fully, basically you have to narrate (everthing should be text):\n\n{text}\n\n"
            }
        ]
    )

    important_topics = response.choices[0].message.content
    print(important_topics)
    return important_topics

file_path = 'Files\generated_files\summarised_notes\module1_summarized.txt' 
extracted_text = extract_text_from_file(file_path)
narrate = extract_important_topics(extracted_text)


print(narrate)
# Split the text into paragraphs
paragraphs = [p.strip() for p in narrate.split('\n') if p.strip()]

# Create a directory to store the images
os.makedirs("images", exist_ok=True)
os.chdir("images")

# Process the paragraphs and search for related images
process_paragraphs(paragraphs)

# Return to the parent directory
os.chdir("..")

while(True):
    text=input(" to exit enter 0 :")
    if(text=="0"):
        break
    narrate = extract_important_topics(text)
    print(narrate)
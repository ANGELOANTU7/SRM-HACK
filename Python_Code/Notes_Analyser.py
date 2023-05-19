import openai

openai.api_key = "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"



def extract_text_from_file(file_path):
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


    
def extract_important_topics(questions):
    text = '\n'.join(questions)
    print(text)
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"create a table (extract atleast 15 important topic names and give all utube link to study those important topic) and give extra similar 3 questions from each topic:\n\n{text}\n\n",
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print("hello")
    #print(response)
    #print(response.choices[0].text)
    important_topics = response.choices[0].text
    return important_topics


file_path = 'Files\generated_files\summarised_notes\module1.txt'  # Replace with the actual file path
extracted_text = extract_text_from_file(file_path)
if extracted_text is not None:
    print(extracted_text)
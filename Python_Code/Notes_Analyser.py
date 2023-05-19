import openai

openai.api_key = "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"

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
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Read the contents of the text file
with open("Files\\notes_txt\module1.txt", "r") as file:
    text = file.read()

# Generate the summary
summary = summarizer(text, max_length=150, min_length=30, do_sample=False)

# Print the summary
print("Summary:")
print(summary[0]['summary_text'])

from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Read the contents of the text file
with open("Files\\notes_txt\module1.txt", "r", encoding='utf-8') as file:
    text = file.read()

# Split the text into smaller chunks
max_tokens_per_chunk = 2000
max_words_in_summary = 2000000

# Calculate the maximum number of chunks needed
max_num_chunks = (max_words_in_summary // max_tokens_per_chunk) + 1
print("\n chunks :"+str(max_num_chunks))

maxlen=max_words_in_summary/max_num_chunks

# Split the text into chunks
chunks = [text[i:i + max_tokens_per_chunk] for i in range(0, len(text), max_tokens_per_chunk)]

# Generate summaries for each chunk
summaries = []
for i, chunk in enumerate(chunks):
    # Break the loop if the maximum number of chunks has been reached
    if i >= max_num_chunks:
        break
    summary = summarizer(chunk, max_length=200, min_length=100, do_sample=False)
    summaries.append(summary[0]['summary_text'])
    print(summary[0]['summary_text'])

# Combine the summaries into a single summary
combined_summary = " ".join(summaries)

# Print the combined summary
print("Combined Summary:")
print(combined_summary)

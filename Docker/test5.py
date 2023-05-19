import os
import re
import chardet
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from sklearn.cluster import KMeans
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def download_file_from_s3(bucket, key, local_filepath):
    s3.download_file(bucket, key, local_filepath)

def upload_file_to_s3(bucket, key, local_filepath):
    s3.upload_file(local_filepath, bucket, key)

def extract_questions_from_file(filepath):
    with open(filepath, 'rb') as f:
        result = chardet.detect(f.read())
    encoding = result['encoding']
    with open(filepath, encoding=encoding) as f:
        content = f.read()
        pattern = r'((?:[IVX]+|\([a-z]\))\. .*(?:\n\s+\(\w\)\. .*)*)'
        matches = re.findall(pattern, content)
        questions = [re.sub(r'\n\s+\(\w\)\. ', ' ', match.strip()) for match in matches]
    return questions

def extract_questions_from_directory(directory):
    questions = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            questions += extract_questions_from_file(filepath)
    return questions


def cluster_questions(questions, num_clusters, syllabus_file):
    module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"
    embed = hub.load(module_url)
    embeddings = embed(questions).numpy()
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(embeddings)
    print("ok")
    y_kmeans = kmeans.predict(embeddings)
    return y_kmeans

# Download questions text file from S3
s3_bucket = 'srmhack'
s3_input_key = 'srmhack/pqs_text/questions.txt'
local_input_filepath = 'questions.txt'
download_file_from_s3(s3_bucket, s3_input_key, local_input_filepath)

questions = extract_questions_from_file(local_input_filepath)
num_clusters = int(input("To how many clusters do you want to cluster the questions: "))
syllabus_file = 'syllabus_txt/syllabus.txt'
labels = cluster_questions(questions, num_clusters, syllabus_file)

# Save cluster questions to file
cluster_output = ''
for i in range(num_clusters):
    cluster_questions = np.array(questions)[np.where(labels == i)[0]]
    cluster_output += f"Module {i+1}:\n"
    for question in cluster_questions:
        cluster_output += f" - {question}\n"
    cluster_output += "\n"

output_filepath = 'sorted_pqs_text/cluster_questions.txt'
with open(output_filepath, 'w') as f:
    f.write(cluster_output)

# Upload the output file to S3
s3_output_key = 'sorted_pqs_text/cluster_questions.txt'
upload_file_to_s3(s3_bucket, s3_output_key, output_filepath)

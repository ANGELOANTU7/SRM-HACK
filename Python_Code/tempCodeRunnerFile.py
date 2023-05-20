
# Process the paragraphs and search for related images
print(image_list)
process_paragraphs(image_list)

# Return to the parent directory
os.chdir("..")

while(True):
    with open('Files\generated_files\\response.txt', 'r',encoding='utf-8') as file:
        content = file.read()
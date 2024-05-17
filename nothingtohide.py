import base64
import requests

# Function to encode a string to Base64
def encode_to_base64(input_string):
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

# Function to download a file given its URL
def download_file(url, filename, rollno):
    response = requests.get(url)
    if response.status_code == 200:
        with open(rollno+"_"+filename, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded: {rollno}")
    else:
        print(f"Failed to download: {rollno}")

# Base URL and suffix
base_url = "https://results.kongu.edu/Photos_format/"
suffix = ".jpeg"

# List of example strings to encode and download
example_strings = input("Enter Roll Numbers : \n").split()

# Generate Base64 encoded filenames and attempt to download each
for example_string in example_strings:
    encoded_string = encode_to_base64(example_string)
    file_name = f"{encoded_string}{suffix}"
    file_url = base_url + file_name
    download_file(file_url, file_name, example_string)

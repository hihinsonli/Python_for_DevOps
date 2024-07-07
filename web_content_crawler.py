import os
import requests

# Function to save content to a file in /tmp directory
def save_to_tmp(filename, content, mode='wb'):
    filepath = os.path.join('/tmp', filename)
    with open(filepath, mode) as f:
        f.write(content)
    print(f"Content saved to {filepath}")

# Function to download and save HTML content
def download_html(url, filename='page.html'):
    response = requests.get(url)
    if response.status_code == 200:
        save_to_tmp(filename, response.content, mode='wb')
    else:
        print(f"Failed to retrieve HTML content. Status code: {response.status_code}")

# Function to download and save JSON content
def download_json(url, filename='data.json'):
    response = requests.get(url)
    if response.status_code == 200:
        save_to_tmp(filename, response.content, mode='wb')
    else:
        print(f"Failed to retrieve JSON content. Status code: {response.status_code}")

# Function to download and save binary content (e.g., images, PDFs)
def download_binary(url, filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        save_to_tmp(filename, response.content, mode='wb')
    else:
        print(f"Failed to retrieve binary content. Status code: {response.status_code}")

# Main function to handle different types of downloads
def download_resource(url, filename=None):
    if not filename:
        filename = url.split('/')[-1]  # Use the last part of the URL as the filename if not provided

    if filename.endswith('.html'):
        download_html(url, filename)
    elif filename.endswith('.json'):
        download_json(url, filename)
    else:
        download_binary(url, filename)

# Example usage
if __name__ == "__main__":
    # Download and save HTML content
    download_resource('http://www.hinsonli.com', 'hinsonli.html')

    # Download and save JSON content

    # Download and save an image
    download_resource('https://blog.hinsonli.com/wp-content/uploads/2024/02/cropped-logo.png', 'hinson_icon.png')

    # Download and save a PDF file

from flask import Flask, render_template
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

app = Flask(__name)

@app.route('/')
def display_image():
    # Azure Blob Storage connection string
    connection_string = "YOUR_CONNECTION_STRING"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Replace 'your-container' and 'your-image.jpg' with your container and image name
    container_name = "your-container"
    blob_name = "your-image.jpg"

    # Create a BlobClient to retrieve the image
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name

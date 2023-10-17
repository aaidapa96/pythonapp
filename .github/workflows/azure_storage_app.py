import os
from azure.storage.blob import BlobServiceClient
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_image():
    # Azure Storage Account Connection String
    connection_string = "your_connection_string_here"

    # Container and Image Name
    container_name = "your_container_name"
    image_name = "your_image_name.jpg"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get the blob URL
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{image_name}"

    # Render HTML with the image URL
    return render_template('index.html', image_url=blob_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

# Required Libraries
import sqlite3
import cv2
import os
import hashlib
from IPython.display import display, clear_output
import ipywidgets as widgets

# Database setup
DB_NAME = "fingerprint_database.db"
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Update the table: Add fingerprint_hash column if it does not exist
cursor.execute('''
PRAGMA table_info(users)
''')
columns = [column[1] for column in cursor.fetchall()]
if "fingerprint_hash" not in columns:
    cursor.execute('''
    ALTER TABLE users ADD COLUMN fingerprint_hash TEXT
    ''')
conn.commit()

# File hash calculation function
def calculate_file_hash(file_content):
    sha256 = hashlib.sha256()
    sha256.update(file_content)
    return sha256.hexdigest()

# Upload user data and fingerprint
def upload_user_data():
    clear_output()

    title = widgets.HTML(value="<h3>Upload User Data</h3>")
    
    # Input fields
    first_name = widgets.Text(description="First Name:", placeholder="Enter first name")
    last_name = widgets.Text(description="Last Name:", placeholder="Enter last name")
    nationality = widgets.Text(description="Nationality:", placeholder="Enter nationality")
    file_upload = widgets.FileUpload(accept='image/*', multiple=False)

    # Buttons
    save_button = widgets.Button(description="Save", button_style='success')
    back_button = widgets.Button(description="Back", button_style='warning')
    status_label = widgets.HTML(value="")

    # Save function
    def save_data(b):
        if not file_upload.value:
            status_label.value = "<p style='color:red;'>Please upload a fingerprint image!</p>"
            return

        # Retrieve file information
        file_info = list(file_upload.value.values())[0]
        file_name = file_info['metadata']['name']
        file_content = file_info['content']

        # Calculate file hash
        file_hash = calculate_file_hash(file_content)

        # Add to database
        cursor.execute('''
        INSERT INTO users (first_name, last_name, nationality, fingerprint_hash)
        VALUES (?, ?, ?, ?)
        ''', (first_name.value, last_name.value, nationality.value, file_hash))
        conn.commit()

        status_label.value = f"<p style='color:green;'>Data saved for {first_name.value} {last_name.value}!</p>"

    save_button.on_click(save_data)
    back_button.on_click(lambda b: main_menu())

    # Display UI
    display(widgets.VBox([title, first_name, last_name, nationality, file_upload, save_button, back_button, status_label]))

# Search fingerprint
def search_fingerprint():
    clear_output()

    title = widgets.HTML(value="<h3>Search Fingerprint</h3>")
    
    # File upload UI
    file_upload = widgets.FileUpload(accept='image/*', multiple=False)
    search_button = widgets.Button(description="Search", button_style='info')
    back_button = widgets.Button(description="Back", button_style='warning')
    status_label = widgets.HTML(value="")

    def search_data(b):
        if not file_upload.value:
            status_label.value = "<p style='color:red;'>Please upload a fingerprint image for searching!</p>"
            return

        # Retrieve file information
        file_info = list(file_upload.value.values())[0]
        file_content = file_info['content']

        # Calculate hash
        search_hash = calculate_file_hash(file_content)

        # Check hash in the database
        for row in cursor.execute("SELECT first_name, last_name, nationality, fingerprint_hash FROM users"):
            db_first_name, db_last_name, db_nationality, db_fingerprint_hash = row

            if search_hash == db_fingerprint_hash:
                status_label.value = f"<p style='color:green;'>Match Found: {db_first_name} {db_last_name}, {db_nationality}</p>"
                return

        status_label.value = "<p style='color:red;'>No match found in the database!</p>"

    search_button.on_click(search_data)
    back_button.on_click(lambda b: main_menu())

    display(widgets.VBox([title, file_upload, search_button, back_button, status_label]))

# Main menu UI
def main_menu():
    clear_output()
    title = widgets.HTML(value="<h2>Fingerprint System Menu</h2>")
    upload_button = widgets.Button(description="Upload User Data", button_style='primary')
    search_button = widgets.Button(description="Search Fingerprint", button_style='primary')

    def show_upload(b):
        upload_user_data()

    def show_search(b):
        search_fingerprint()

    upload_button.on_click(show_upload)
    search_button.on_click(show_search)

    display(widgets.VBox([title, upload_button, search_button]))

# Run main menu
main_menu()

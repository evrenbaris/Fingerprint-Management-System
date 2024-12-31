# Fingerprint Management System

## Overview
The **Fingerprint Management System** is a Python-based application that enables storing, searching, and managing fingerprint data securely using SQLite as the database. It calculates fingerprint hashes to maintain security and provides a simple interface for uploading user data and searching fingerprints.

## Features
- **Upload Fingerprint Data**: Add user details (name, nationality) and upload a fingerprint image. The image is hashed for security and stored in a SQLite database.
- **Search Fingerprint**: Compare an uploaded fingerprint image against the database and retrieve matching user details.
- **Secure Hashing**: Uses SHA-256 to hash fingerprint data.
- **Interactive Interface**: Provides a simple and intuitive UI using `ipywidgets` for operations.

## Prerequisites
- Python 3.x
- Required Python libraries:
  - `sqlite3` (built-in)
  - `opencv-python`
  - `ipywidgets`

## Usage
### Upload User Data
1. Navigate to the **Upload User Data** section in the interface.
2. Enter the following details:
   - **First Name**: The user's first name.
   - **Last Name**: The user's last name.
   - **Nationality**: The user's nationality.
3. Upload a fingerprint image by clicking the "Upload" button.
4. Once all fields are filled, click the **Save** button to store the data in the database. You will receive a success message upon completion.

### Search Fingerprint
1. Navigate to the **Search Fingerprint** section in the interface.
2. Upload a fingerprint image by clicking the "Upload" button.
3. Click the **Search** button to initiate the search in the database.
4. If a match is found, the following user details will be displayed:
   - **First Name**
   - **Last Name**
   - **Nationality**
5. If no match is found, an error message will be displayed indicating no results.


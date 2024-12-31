Fingerprint Management System
Overview
The Fingerprint Management System is a Python-based application that enables storing, searching, and managing fingerprint data securely using SQLite as the database. It calculates fingerprint hashes to maintain security and provides a simple interface for uploading user data and searching fingerprints.

Features
Upload Fingerprint Data: Add user details (name, nationality) and upload a fingerprint image. The image is hashed for security and stored in a SQLite database.
Search Fingerprint: Compare an uploaded fingerprint image against the database and retrieve matching user details.
Secure Hashing: Uses SHA-256 to hash fingerprint data.
Interactive Interface: Provides a simple and intuitive UI using ipywidgets for operations.
Prerequisites
Python 3.x
Required Python libraries:
sqlite3 (built-in)
opencv-python
ipywidgets
Install dependencies:

bash
Kodu kopyala
pip install opencv-python ipywidgets
How to Run
Clone the repository:

bash
Kodu kopyala
git clone https://github.com/your_username/fingerprint-management-system.git
cd fingerprint-management-system
Run the Python script in Jupyter Notebook or Google Colab.

Follow the on-screen instructions in the interface.

Usage
Upload User Data
Enter the user's first name, last name, and nationality.
Upload a fingerprint image.
Click "Save" to store the data in the database.
Search Fingerprint
Upload a fingerprint image for searching.
Click "Search" to find matches in the database.
If a match is found, the user details will be displayed.
File Structure
perl
Kodu kopyala
fingerprint-management-system/
│
├── fingerprint_database.db      # SQLite database file
├── fingerprints/                # Folder for uploaded fingerprint images
├── temp/                        # Temporary folder for searched fingerprint images
├── main.py                      # Main Python script
└── README.md                    # Project documentation
Contributing
Contributions are welcome! If you’d like to add features or improve this project, please fork the repository and submit a pull request.

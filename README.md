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

Install dependencies:
```bash
pip install opencv-python ipywidgets

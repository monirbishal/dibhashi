#!/usr/bin/env python
"""
Passenger WSGI file for Namecheap shared hosting deployment
"""

import sys
import os

# Add your project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)
sys.path.insert(0, os.path.join(project_dir, 'src'))

try:
    # Import your Flask application
    from dibhashi.app import app
    
    # This is what Passenger will use
    application = app
    
except ImportError as e:
    # Fallback import method
    sys.path.insert(0, os.path.join(project_dir, 'src', 'dibhashi'))
    try:
        from app import app
        application = app
    except ImportError as e2:
        # Create a simple error application for debugging
        from flask import Flask
        application = Flask(__name__)
        
        @application.route('/')
        def error_page():
            return f"Import Error: {str(e)} | {str(e2)} | Python Path: {sys.path}"

if __name__ == "__main__":
    application.run()
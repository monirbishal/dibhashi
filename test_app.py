"""
Simple test Flask app to verify hosting environment
Upload this to test if basic Flask works before deploying the full application
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>🎉 Flask is Working!</h1>
    <p>Your hosting environment can run Flask applications.</p>
    <p>If you see this message, the 503 error is likely due to:</p>
    <ul>
        <li>Missing dependencies</li>
        <li>Memory limitations with ML libraries</li>
        <li>Import path issues</li>
    </ul>
    <p><strong>Next step:</strong> Check the main application dependencies.</p>
    '''

@app.route('/test')
def test():
    import sys
    import os
    return f'''
    <h2>Environment Information</h2>
    <p><strong>Python Version:</strong> {sys.version}</p>
    <p><strong>Current Directory:</strong> {os.getcwd()}</p>
    <p><strong>Python Path:</strong></p>
    <ul>
    {"".join([f"<li>{path}</li>" for path in sys.path])}
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)
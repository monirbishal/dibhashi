# STEP-BY-STEP DEPLOYMENT INSTRUCTIONS FOR dibhashi.monirbishal.com

## 🎯 Quick Deployment Checklist

### Step 1: Access Your Namecheap cPanel
1. Log into your Namecheap account
2. Go to cPanel for your hosting account
3. Look for "Python Selector" or "Setup Python App"

### Step 2: Create Python Application
1. Click "Create Application"
2. Configure these settings:
   - **Python Version**: `3.11`
   - **Application Root**: `/home/petmxuma/dibhashi.monirbishal.com`
   - **Application URL**: `dibhashi.monirbishal.com`
   - **Startup File**: `passenger_wsgi.py`
3. Click "Create"

### Step 3: Upload Your Project Files
**Option A: Using cPanel File Manager**
1. In cPanel, open "File Manager"
2. Navigate to: `/home/petmxuma/dibhashi.monirbishal.com`
3. Upload ALL these files from your local project:
   ```
   ✓ src/ (entire folder)
   ✓ passenger_wsgi.py
   ✓ .htaccess
   ✓ requirements-production.txt
   ✓ .env.production (rename to .env)
   ✓ pyproject.toml
   ✓ README.md
   ✓ All other project files
   ```

**Option B: Using FTP/SFTP**
1. Use FileZilla or similar FTP client
2. Connect to your hosting account
3. Navigate to: `/home/petmxuma/dibhashi.monirbishal.com`
4. Upload all project files

### Step 4: Set File Permissions
In File Manager, set permissions:
- **Folders**: `755`
- **Python files**: `644`
- **passenger_wsgi.py**: `755`

### Step 5: Install Dependencies
1. In cPanel, go back to "Python Selector"
2. Click on your "dibhashi" application
3. In the "Packages" section, click "Add packages"
4. Install these key packages:
   ```
   flask
   torch
   transformers
   pytube
   banglatts
   librosa
   ```
5. Or use terminal (if available):
   ```bash
   source /home/petmxuma/virtualenv/dibhashi.monirbishal.com/3.11/bin/activate
   cd /home/petmxuma/dibhashi.monirbishal.com
   pip install -r requirements-production.txt
   ```

### Step 6: Configure Environment Variables
1. Edit the `.env` file in your project directory
2. Update these settings:
   ```
   FLASK_ENV=production
   FLASK_DEBUG=False
   SECRET_KEY=your-secret-key-here
   ```

### Step 7: Test Your Application
1. Visit: `https://dibhashi.monirbishal.com`
2. You should see your Flask application homepage
3. Test basic functionality

## 🔧 If You Encounter Issues

### Error 500 (Internal Server Error)
- Check file permissions
- Verify `.htaccess` configuration
- Check Python app settings in cPanel

### Import Errors
- Ensure all dependencies are installed
- Check `passenger_wsgi.py` import path
- Verify file structure is correct

### Memory Issues
- Your app uses heavy ML libraries
- Consider upgrading to VPS if shared hosting limits are hit
- Monitor resource usage in cPanel

## 📁 Final Directory Structure
Your `/home/petmxuma/dibhashi.monirbishal.com/` should look like:
```
/home/petmxuma/dibhashi.monirbishal.com/
├── src/
│   └── dibhashi/
│       ├── app.py
│       ├── templates/
│       ├── static/
│       └── utils/
├── passenger_wsgi.py
├── .htaccess
├── .env
├── requirements-production.txt
├── pyproject.toml
└── README.md
```

## ✅ Success Indicators
- ✓ Python app shows "Running" in cPanel
- ✓ `https://dibhashi.monirbishal.com` loads without errors
- ✓ You can see your Flask application interface
- ✓ Basic features work (translation, text processing)

## 🆘 Need Help?
If you get stuck:
1. Check error logs in cPanel
2. Verify all files are uploaded correctly
3. Double-check Python app configuration
4. Contact Namecheap support for hosting-specific issues

Your application should now be live at: **https://dibhashi.monirbishal.com** 🚀
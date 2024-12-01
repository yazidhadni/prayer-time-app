from setuptools import setup


APP = ["app.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "plist": {
        'CFBundleName': 'PrayerApp',  # App name as it appears to the user
        'CFBundleDisplayName': 'Prayer App',  # Display name
        'CFBundleIdentifier': 'com.prayer.prayerapp',  # Unique identifier
        'LSUIElement': False,  # Hide app from Dock (important for menu bar apps)
        'CFBundleExecutable': 'app',  # Ensure the main app file is referenced
    },
    'iconfile': 'resources/kaaba.icns',  # Path to app's icon
}

setup(
    app=APP, # List of Python scripts to include
    data_files=DATA_FILES, # List of additional resources
    options={'py2app': OPTIONS}, # Options passed to py2app
    setup_requires=["py2app"], # Py2app is required to build this package
)
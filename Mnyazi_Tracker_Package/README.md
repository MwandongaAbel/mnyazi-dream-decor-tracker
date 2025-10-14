
Mnyazi Dream Decor Event Tracker
=================================

This package contains the source code and build scripts for the Windows desktop app
"Mnyazi Dream Decor Event Tracker". The app uses Firebase for cloud storage and
authentication. The package includes an automated build script to create a Windows .exe
using PyInstaller on a Windows machine.

IMPORTANT NOTES
---------------
- This ZIP contains source code, assets, and build instructions. Building the final
  installer/executable requires running the included build script on a Windows PC.
- You must create a Firebase project (Firestore + Authentication + Storage) and obtain
  credentials. See the section "Firebase Setup" below.
- If you prefer, I can produce a compiled .exe for you, but I need to run PyInstaller on a Windows environment. 
  For now, this package lets you build locally and is ready-to-use.

Firebase Setup
--------------
1. Go to https://console.firebase.google.com and create a new project.
2. Enable Authentication (Email/Password provider).
3. Create a Firestore database in production or test mode.
4. (Optional) Enable Cloud Storage if you want to upload photos.
5. In Project Settings, under "Your apps", register a Web app and copy the firebaseConfig object.
   Create a file named `firebase_config.json` in the `config` folder with the following fields:
   { "apiKey": "...", "authDomain": "...", "projectId": "...", "storageBucket": "...", "messagingSenderId": "...", "appId": "..." }

Building the Windows executable (on Windows)
--------------------------------------------
1. Install Python 3.10+ and add to PATH.
2. Open CMD in this package folder and run:
   python -m pip install -r requirements.txt
3. Customize config/firebase_config.json and (optionally) serviceAccount for admin operations.
4. Run the build script to create the .exe:
   build_installer.bat
5. The generated .exe will appear in the `dist` folder.

What is included in this package
--------------------------------
- main.py                 -> Tkinter app (client UI, login, bookings, reports)
- firebase_helper.py      -> helper functions to interact with Firebase
- requirements.txt        -> Python dependencies
- build_installer.bat     -> Windows batch file to build the executable with pyinstaller
- config/firebase_config.sample.json -> sample firebase config
- assets/logo.png         -> your uploaded logo
- README.md               -> this file

Need help?
-----------
Reply here and I can:
- Guide you through Firebase provisioning and configuration.
- Build the .exe for you if you want me to produce the final installer.

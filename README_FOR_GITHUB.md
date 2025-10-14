GitHub Actions Build & Release
------------------------------
This repository contains the Mnyazi Dream Decor Event Tracker app.
The workflow at .github/workflows/windows-build-and-release.yml will:
  - build the app using PyInstaller on windows-latest
  - create an Inno Setup installer using installer_script.iss
  - create a GitHub Release and upload the main.exe and installer as assets

How to use:
  1. Create a GitHub repo and push this project to the `main` branch.
  2. In the repo settings, leave Actions enabled (default) and ensure `GITHUB_TOKEN` is available.
  3. Push to `main` or manually run the workflow via the Actions tab -> "Run workflow".

Notes:
  - The workflow uses Chocolatey to install Inno Setup. If the runner fails to install, ensure choco is available.
  - Replace config/firebase_config.json with your Firebase config (do not commit secrets in public repos).

[Setup]
AppName=Mnyazi Dream Decor Tracker
AppVersion=1.0
DefaultDirName={autopf}\Mnyazi Dream Decor Tracker
DefaultGroupName=Mnyazi Dream Decor Tracker
OutputDir=Mnyazi_Tracker_Package\Output
OutputBaseFilename=Mnyazi_Tracker_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=Mnyazi_Tracker_Package\assets\app_icon.ico
UninstallDisplayIcon={app}\Mnyazi Dream Decor Tracker.exe

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Mnyazi Dream Decor Tracker"; Filename: "{app}\Mnyazi_Tracker_Package.exe"
Name: "{commondesktop}\Mnyazi Dream Decor Tracker"; Filename: "{app}\Mnyazi_Tracker_Package.exe"

[Run]
Filename: "{app}\Mnyazi_Tracker_Package.exe"; Description: "Launch Mnyazi Dream Decor Tracker"; Flags: nowait postinstall skipifsilent


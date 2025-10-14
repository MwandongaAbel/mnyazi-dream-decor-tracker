[Setup]
AppName=Mnyazi Dream Decor Event Tracker
AppVersion=1.0.0
AppPublisher=Mnyazi Dream Decor
DefaultDirName={autopf}\Mnyazi Dream Decor Event Tracker
DefaultGroupName=Mnyazi Dream Decor
OutputDir=Output
OutputBaseFilename=Mnyazi_Dream_Decor_Tracker_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=Mnyazi_Tracker_Package\assets\app_icon.ico
WizardStyle=modern
UninstallDisplayIcon={app}\main.exe

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "Mnyazi_Tracker_Package\assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Mnyazi Dream Decor Event Tracker"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Mnyazi Dream Decor Event Tracker"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "Launch Mnyazi Dream Decor Event Tracker"; Flags: nowait postinstall skipifsilent

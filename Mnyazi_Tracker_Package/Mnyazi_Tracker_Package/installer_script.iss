; ------------------------------------------------------
; Mnyazi Dream Decor Event Tracker - Installer Script
; ------------------------------------------------------
; Created by Abel Mwandonga Haro
; Motto: "Elegance in Every Detail. Stunning Decor for Every Occasion."
; ------------------------------------------------------

[Setup]
AppName=Mnyazi Dream Decor Event Tracker
AppVersion=1.0.0
AppPublisher=Mnyazi Dream Decor
AppPublisherURL=https://github.com/MwandongaAbel
AppSupportURL=https://github.com/MwandongaAbel
AppUpdatesURL=https://github.com/MwandongaAbel/mnyazi-dream-decor-tracker
DefaultDirName={autopf}\Mnyazi Dream Decor Event Tracker
DefaultGroupName=Mnyazi Dream Decor
OutputDir=Output
OutputBaseFilename=Mnyazi_Dream_Decor_Tracker_Setup
Compression=lzma
SolidCompression=yes
SetupIconFile=Mnyazi_Tracker_Package\assets\app_icon.ico
WizardStyle=modern
UninstallDisplayIcon={app}\main.exe

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "Mnyazi_Tracker_Package\assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Mnyazi Dream Decor Event Tracker"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Mnyazi Dream Decor Event Tracker"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "Launch Mnyazi Dream Decor Event Tracker"; Flags: nowait postinstall skipifsilent

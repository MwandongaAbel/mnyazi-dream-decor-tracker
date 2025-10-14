; ---------------------------------------------
; Mnyazi Dream Decor Tracker - Inno Setup Script
; ---------------------------------------------

[Setup]
AppName=Mnyazi Dream Decor Tracker
AppVersion=1.0.0
AppPublisher=Mnyazi Dream Decor
DefaultDirName={autopf}\Mnyazi Dream Decor Tracker
DefaultGroupName=Mnyazi Dream Decor
OutputDir=Mnyazi_Tracker_Package\Output
OutputBaseFilename=Mnyazi_Tracker_Installer
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin
DisableWelcomePage=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
; NOTE: Make sure this file exists before compiling!
Source: "Mnyazi_Tracker_Package\dist\MnyaziTracker.exe"; DestDir: "{app}"; Flags: ignoreversion

; If you have supporting files (like icons, configs, etc.), add them here
; Example:
; Source: "Mnyazi_Tracker_Package\data\*"; DestDir: "{app}\data"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Mnyazi Dream Decor Tracker"; Filename: "{app}\MnyaziTracker.exe"
Name: "{group}\Uninstall Mnyazi Dream Decor Tracker"; Filename: "{uninstallexe}"
Name: "{commondesktop}\Mnyazi Dream Decor Tracker"; Filename: "{app}\MnyaziTracker.exe"

[Run]
Filename: "{app}\MnyaziTracker.exe"; Description: "Launch Mnyazi Dream Decor Tracker"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"



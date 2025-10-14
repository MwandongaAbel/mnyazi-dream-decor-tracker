; Inno Setup Script for Mnyazi Dream Decor Tracker
[Setup]
AppName=Mnyazi Dream Decor Event Tracker
AppVersion=1.0
AppPublisher=Mnyazi Dream Decor
AppPublisherURL=https://github.com/MwandongaAbel/mnyazi-dream-decor-tracker
AppSupportURL=https://github.com/MwandongaAbel/mnyazi-dream-decor-tracker/issues
DefaultDirName={autopf}\Mnyazi Dream Decor Event Tracker
DefaultGroupName=Mnyazi Dream Decor
OutputBaseFilename=Mnyazi_Dream_Decor_Tracker_Setup
OutputDir=Output
SetupIconFile=assets\app_icon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Mnyazi Dream Decor Tracker"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Mnyazi Dream Decor Tracker"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "Launch Mnyazi Dream Decor Tracker"; Flags: nowait postinstall skipifsilent

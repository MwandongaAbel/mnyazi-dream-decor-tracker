; =============================================================
; Mnyazi Dream Decor Event Tracker Installer Script
; Elegance in Every Detail. Stunning Decor for Every Occasion.
; =============================================================

[Setup]
AppName=Mnyazi Dream Decor Event Tracker
AppVersion=1.0
AppPublisher=Mnyazi Dream Decor
AppPublisherURL=https://github.com/MwandongaAbel/mnyazi-dream-decor-tracker
DefaultDirName={autopf}\Mnyazi Dream Decor Event Tracker
DefaultGroupName=Mnyazi Dream Decor
UninstallDisplayIcon={app}\main.exe
Compression=lzma
SolidCompression=yes
OutputDir=Output
OutputBaseFilename=Mnyazi_Dream_Decor_Tracker_Setup
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64
SetupLogging=yes
DisableWelcomePage=no
DisableDirPage=no
DisableProgramGroupPage=no
DisableFinishedPage=no
SetupIconFile=assets\app_icon.ico
WizardImageFile=assets\installer_banner.bmp
WizardSmallImageFile=assets\installer_banner_small.bmp
WizardResizable=yes
BackColor=$E6D9F3
BackColor2=$FFFFFF
BackColorDirection=topbottom

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a desktop shortcut"; GroupDescription: "Additional icons:"; Flags: unchecked

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "Mnyazi_Tracker_Package\assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]
Name: "{group}\Mnyazi Dream Decor Event Tracker"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Mnyazi Dream Decor Event Tracker"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "Launch Mnyazi Dream Decor Event Tracker"; Flags: nowait postinstall skipifsilent

[Messages]
BeveledLabel=Mnyazi Dream Decor — Elegance in Every Detail
SetupAppTitle=Mnyazi Dream Decor Event Tracker Setup
SetupWindowTitle=Mnyazi Dream Decor — Event Tracker Installer

[Code]
procedure InitializeWizard();
begin
  MsgBox('Welcome to Mnyazi Dream Decor Event Tracker Setup!' + #13#13 +
         'Elegance in Every Detail. Stunning Decor for Every Occasion.' + #13#13 +
         'Click Next to begin the installation.', mbInformation, MB_OK);
end;


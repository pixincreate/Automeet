# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['E:/Coding/Python/My_Projects/GoogleMeetAutomation/Automeet.py'],
             pathex=['E:\\Coding\\Python\\My_Projects\\GoogleMeetAutomation\\Executables'],
             binaries=[('E:/Coding/Python/My_Projects/GoogleMeetAutomation/Executables/Drivers/chromedriver.exe', '.')],
             datas=[('E:\\Coding\\Python\\My_Projects\\GoogleMeetAutomation\\Executables\\stealth', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Automeet',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='E:\\Coding\\Python\\My_Projects\\GoogleMeetAutomation\\Executables\\Automeet.ico')

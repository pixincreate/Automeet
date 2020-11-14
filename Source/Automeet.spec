# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['drive:/path/to/source code'],
             pathex=['drive:\\path\\to\\save\\pixincreate spec file'],
             binaries=[('drive:/path/to/pixincreate chromedriver.exe', './selenium/webdriver'), ('drive:/path/to/pixincreate geckodriver-32.exe', './selenium/webdriver'), ('drive:/path/to/pixincreate geckodriver-64.exe', './selenium/webdriver')],
             datas=[],
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
          name='Automeet by PiXinCreate',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='drive:\\path\\to\\icon\\pixincreate Automeet.ico')

# -*- mode: python ; coding: utf-8 -*-


added_files = [
    ('app.ico', '.'),
    ('./character.py', '.'),
    ('./build.kv', '.'),
    ('./data', 'data'),
    ('./images', 'images')
]
a = Analysis(
    ['main.py'],
    pathex=['./.venv/Lib/site-packages'],
    binaries=[],
    datas=added_files,
    hiddenimports=['plyer.platforms.win.notification', 'plyer.platforms.win.filechooser'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DF Build Tool Debug',
    icon='app.ico',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='DF Build Tool Prepackaged Files',
)

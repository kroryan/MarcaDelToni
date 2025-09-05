@echo off
echo ============================================
echo    COMPILADOR SIMPLE - MARCA DEL TONI
echo ============================================
echo.
echo Compilando a .exe...

pyinstaller --onefile --windowed --name="MarcaDelToni" marca_de_agua_visible.py

if exist "dist\MarcaDelToni.exe" (
    echo.
    echo ✅ ¡LISTO! Tu .exe está en: dist\MarcaDelToni.exe
    echo.
    explorer dist
) else (
    echo ❌ Error en compilación
)

pause

@echo off
echo ============================================
echo    COMPILADOR DE MARCA DEL TONI A .EXE
echo ============================================
echo.
echo Compilando marca_de_agua_visible.py...
echo.

REM Crear el ejecutable con PyInstaller
pyinstaller --onefile --windowed --name="MarcaDelToni" --icon=icono.ico --add-data="*.py;." marca_de_agua_visible.py

REM Verificar si se creó correctamente
if exist "dist\MarcaDelToni.exe" (
    echo.
    echo ✅ ¡COMPILACIÓN EXITOSA!
    echo.
    echo 📁 El archivo .exe se encuentra en: dist\MarcaDelToni.exe
    echo 📏 Tamaño aproximado: 
    dir "dist\MarcaDelToni.exe" | find "MarcaDelToni.exe"
    echo.
    echo 🚀 ¿Quieres ejecutar el .exe ahora? (s/n)
    set /p respuesta=
    if /i "%respuesta%"=="s" (
        echo.
        echo 🎯 Ejecutando MarcaDelToni.exe...
        start "MarcaDelToni" "dist\MarcaDelToni.exe"
    )
) else (
    echo.
    echo ❌ Error en la compilación
    echo Revisa los mensajes anteriores para más detalles
)

echo.
echo 📋 Archivos generados:
echo    - dist\MarcaDelToni.exe (ejecutable final)
echo    - build\ (archivos temporales - se pueden borrar)
echo    - MarcaDelToni.spec (configuración de PyInstaller)
echo.
pause

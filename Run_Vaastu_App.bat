@echo off
set APP_DIR=%~dp0
set APP_DIR=%APP_DIR:~0,-1%

echo Starting Streamlit from:
echo %APP_DIR%
echo.

"%APP_DIR%\.venv\Scripts\python.exe" -m streamlit run "%APP_DIR%\main.py"

pause

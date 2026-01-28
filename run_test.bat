@echo off
REM Script pentru testarea configurației

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Running test_config.py...
python test_config.py

pause

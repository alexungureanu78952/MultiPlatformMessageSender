@echo off
REM Script pentru rularea aplicației cu virtual environment

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Running main.py...
python main.py

pause

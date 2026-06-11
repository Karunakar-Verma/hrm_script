@echo off

echo Installing requirements...
pip install -r requirements.txt

echo Setting PYTHONPATH...
cd %~dp0
set PYTHONPATH=%CD%

echo Running tests...
pytest tests --html=reports/report.html --self-contained-html -v

echo Done.
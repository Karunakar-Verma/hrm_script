@echo off

echo Installing requirements...
pip install -r requirements.txt

echo Running tests...
pytest --html=reports/report.html --self-contained-html

echo Done.
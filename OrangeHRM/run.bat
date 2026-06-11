@echo off

echo Installing requirements...
pip install -r requirements.txt

echo Setting PYTHONPATH...
cd %~dp0
set PYTHONPATH=%CD%

echo Running tests...
pytest tests --alluredir=allure_report

echo opening allure report..
allure serve allure_report

echo Done.
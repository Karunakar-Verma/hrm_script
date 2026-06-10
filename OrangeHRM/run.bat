@echo off

cd %WORKSPACE%
pytest -v OrangeHRM/tests --html=OrangeHRM/Reports/report.html --self-contained-html

pause
@echo off
echo Using PyPi
echo Use build for TestPyPi
timeout /t -1
cls
color 0c
echo Have you incremented the version number?
timeout /t -1
cls
color 0c
echo Have you incremented the version number?
timeout /t -1
cls
color 0f
hatch build
py -m twine check dist/*
IF %ERRORLEVEL% NEQ 0 goto error || py -m twine upload --repository pypi dist/*

:error
color c0
echo An error occoured!
echo Aborting.
timeout /t -1
color 07
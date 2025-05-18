@echo off
set /p domain=Enter your CDN domain (e.g., source.rachel.onl.ac): 
set /p delay=Enter header delay in seconds (e.g., 30): 
python test_header_delay.py %domain% --delay %delay%
pause
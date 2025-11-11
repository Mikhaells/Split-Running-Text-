@echo off
@REM echo Program untuk split Running Text ke dalam beberapa file
@REM echo.

@REM set /p shared_folder=Masukkan Path Shared Folder:  
@REM set /p filename=Masukkan nama file: 

echo.
echo Memproses...
@REM python RunningText.py "%shared_folder%" "%filename%"
python RunningText.py
pause
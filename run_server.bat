@echo off
set FLASK_ENV=development
set PORT=5001
set FLASK_DEBUG=True
set APP=forca-backend.app:create_app

echo -----------------------------------------------------



echo Executando a aplicacao: %APP% 
echo -----------------------------------------------------
 flask run -p %PORT%
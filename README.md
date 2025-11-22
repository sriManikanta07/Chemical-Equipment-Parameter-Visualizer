Desktop_frontend  ------ this is the Desktop Application Frontend
	
equipment_project ----- this the common server in Django (desktop + web versions)
	
webapp  ----------------- this is reack frontend for web application


Ater cloning repo for each :
   # install dependencies and requirement(in virtual environment recommended)
   # run them separetely using commonds given below
   # create a new user(register option)

Commands for (equipment_project)  :
   # git clone https://github.com/sriManikanta07/Chemical-Equipment-Parameter-Visualizer
   # cd Chemical-Equipment-Parameter-Visualizer
   # python -m venv venv
   # source venv/Scripts/activate  # (Windows)
   # Install dependencies
      pip install -r requirements.txt

   # run 
     (for migration)
     python manage.py makemigrations
     python manage.py migrate
     (to run server)
     python manage.py runserver 8080


Commands for (Desktop_frontend)  :
    # use same virtual environemen as of common server or install requirements
    # Install dependencies
       pip install -r requirements.txt

   # run 
      Python Desktop_frontend.py
   # it will open the window

Commands for (webapp)  :
   # cd webapp
   # install dependencies
      npm install
   # run app
      npm run dev
   # this will open application a brower window   
   # if now opening check port no. 5174 (should be free)

  
      
    


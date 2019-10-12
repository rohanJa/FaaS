# REST-api
Function as a Service and other docker related
It uses  docker to function.

[curl Commmands are provided](https://github.com/rohanJa/FaaS/blob/master/rest_api/curl%20request%20command)



An online biding project built using django framework.  

[Requirements](https://github.com/rohanJa/FaaS/blob/master/rest_api/requirements.txt)


Create virtual enviornment:-
    Step 1 :-
        Create a virtualenv using below command :-
            ```
            python3 -m virtualenv auction
            ```

To activate virtual enviornment:-
    ```
    source (name of virual enviornment)/bin/activate
    ```
To intiate directory with git :-
    
    Step 2.1 :-
        git init

    Step 2.2 :-
        git pull https://github.com/rohanJa/Faas.git
    
    Step 2.3 :-
        pip install -r requirements.txt
    

Now to intialize project:-

    Step 3.1 :-
        python manage.py makemigrations

    Step 3.2 :-
        python manage.py migrate


Now run the project :-

        '''
        python manage.py runserver 127.0.0.1:8000  
        '''
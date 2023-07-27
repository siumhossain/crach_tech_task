# crach_tech_task

### Project setup
* Create virtualenv
    * Activa virtualenv
      
      ```bash
      source v/bin/active #linux
      ```
* Install requirements
  
  ```bash
  pip install -r requirements.txt
  ```
* Run
  
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ```
### Db 
> I'm not able to provide sqlite db, where i created around 10 lac users, and 1 lac random question because of github large file ditection.
> But I'm providing db link using google drive, here is the link - https://drive.google.com/file/d/181vG-cP8TPkGA_fCPJTCnpE1fgaMRJZV/view?usp=sharing

you can generate user, random question etc by simple command, example:
* Create user by

  ```bash
  python manage.py generate_fake_data <number of users you want> #100000
  ```
* Create question

```bash
python manage.py generate_question <number of question you want> #200000
```
* Create favourite question database
```bash
python manage.py generate_fvrt_question <number of question you want> #200000
```
* Create read question database
```bash
python manage.py generate_read_question 10000
```

### URL endpoint
  * http://127.0.0.1:8000/api/v1/user-info/
    > get All user information

  * http://127.0.0.1:8000/api/v1/question-info/
    > retrive all question
    
    > Filter params
      * **?favorite=true** : retrive all favorite question
      * **?unfavorite=true** : retrive all unfavorite question
      * **?read=true** : retrive all read question
      * **?unread=true** : retrive all unread question

### Run Test
```bash
python manage.py test question
```


        
  



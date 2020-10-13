
How to run the program
1.	Download the file and unzip it or you can use git clone. 
2. Open visual studio code or any compatible IDE to run the code. (Visual Studio Code is recommended) 
3. Open IDE terminal. 
4. To load the program locate to the folder where the files are downloaded or git cloned from the IDE in the terminal.
5. Set environment variable with “source env/bin/activate”
6. Change directory to where manage.py file is. 
7. run "python manage.py runserver” in the command line 
8. Copy localhost path from the terminal to the browser.
9. Click {"users": "http://127.0.0.1:8000/users/"}
10. Now you can register, search and delete.

To register
1.	Pass json format as {“name”:”your_name”,”email”:”your_email”,”country”:”country_code”,”isbn”:”book_isbn”} and hit “POST”.

To search
1.	After the url “http://127.0.0.1:8000/users/” pass the user’s id to get details.

To delete
1.	After search for specific user hit “DELETE” button.

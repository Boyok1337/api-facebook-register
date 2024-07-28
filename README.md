# Facebook auto register

The project has low performance due to the use of free temporary mails, and also works without a proxy. To improve performance for business use, you should add a proxy and use a paid api to generate mail for Facebook accounts

## 👩‍💻 _Installation & Run_
### 🧠 Set up the environment 

### 📝 Set enviroment variable
- Copy and rename the **.env.sample** file to **.env** 
- Open the .env file and edit the environment variables 
- Set a password for new Facebook accounts
- Make sure the .env file is in .gitignore

 On Windows:
```python
python -m venv venv 
venv\Scripts\activate
 ```

 On UNIX or macOS:
```python
python3 -m venv venv 
source venv/bin/activate
 ```

### 🗃️ Install requirements 
```python
pip install requirements.txt
```

### 😄 Make POST request to this endpoint [http://localhost:8000/register-accounts/{count}](http://localhost:8000/register-accounts/{count})

## 📝 Contributing
If you want to contribute to the project, please follow these steps:
    1. Fork the repository.
    2. Create a new branch for your feature or bug fix.
    3. Make the necessary changes and commit them.
    4. Submit a pull request.

## 😋 _Enjoy it!_
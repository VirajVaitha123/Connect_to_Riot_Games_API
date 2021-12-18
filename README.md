# Connect_to_Riot_Games_API
Simple script to extract information from the Riot Games API

# Getting Started
![alt text](https://github.com/VirajVaitha123/Connect_to_Riot_Games_API/Images/main/riotlogo.png?raw=true)

#### Step 1: Create and activate Virtual Environment
Clone the repositary and ensure your terminal is pointing to this directory. (If not write CD <filepath-to-repo>)
 
Run the commands in your terminal below to create the virtual environment, install requirements and activate the virtual environment.

```
python -m venv env
pip install -r requirements.txt
env\Scripts\activate.bat
```

#### Step 2: Obtain API Key
Request a developer key by sending an application to:
https://developer.riotgames.com/


#### Step 3: Save the key as an environment variable
Follow the steps below to save the key with the name "X-Riot-Token" as an environment variable:
https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/

(Type environment variable in your windows search bar -> select environment variables in the system properties windows -> Add key value pair under system variables)

#### Step 4: run the main.py file
In your terminal run:

```
python main.py 
```

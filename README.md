In order to run the application you can follow the instructions below:

# Mac OS

## 1. Install Python and Pip

**Install Python**

Install brew, paste this in macOS Terminal prompt.
    
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Once brew is installed:
    
    $ brew install python3
    
You can check if the installation worked:
    
    $ python3 --version
    
The output should be similar to this:
    
    Python 3.8.1


**Install Pip**

Start with:

    $ sudo easy_install pip
    
Check that the installation worked:
    
    $ pip3 --version
    
The output should be similar to this:
    
    pip 20.0.1 from /Users/user_name/virtualenvironment/interface/lib/python3.7/site-packages/pip (python 3.7)
    
    
## 2. Requirements

Create a virtual environment:

    $ pip install virtualenv
    
    $ virtualenv my_venv
    
    $ source my_venv/bin/activate

Go to the repository folder and install the requirements:
    
    $ pip3 install -r requirements.txt
   

## 3. Run 

To run the program:
    
    $ python3 app.py
    
    
------------------------------


# Windows

## 1. Install Python and Pip

**Install Python**

Go to https://www.python.org/downloads/windows and download python's 3.7.6 version, happyhorsemeter doesn't work with python8 at the moment.

Execute the downloaded installer and follow the instructions :rotating_light:(**make sure you check the option "Add Python 3.7 to PATH"**).
If you don't check this option you will get an error when trying to run the commands below. The error is similar to this: "python" is not recognized as a command or an external command ...


You can check if the installation worked by opening the command prompt typing this:
    
    $ python --version
    
The output should be similar to this:
    
    Python 3.7.6
    

**Install Pip**

Start with:

    $ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    
    $ python get-pip.py
    
Check that the installation worked:
    
    $ pip --version
    
The output should be similar to this:
    
    pip 20.0.2 from /Users/user_name/virtualenvironment/interface/lib/python3.7/site-packages/pip (python 3.7)
    
    
## 2. Requirements

Create a virtual environment:

    $ pip install virtualenv
    
    $ python -m venv my_venv
    
    $ my_env\Scripts\activate.bat

Go to the repository folder and install the requirements:
    
    $ pip install -r requirements.txt
   

## 3. Run 

To run the program:
    
    $ python app.py


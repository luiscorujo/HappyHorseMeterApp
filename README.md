In order to run the application in **mac os** you need to do the following:

## Install Python and Pip

**Install Python**

Install brew, paste this in a macOS Terminal prompt.
    
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Once brew is installed:
    
    $ brew install python3
    
You can check if the installation worked:
    
    $ python3 --version
    
The output should be similar to this:
    
    Python 3.7.2


**Install Pip**

Start with:

    $ sudo easy_install pip
    
Check that the installation worked:
    
    $ pip --version
    
The output should be similar to this:
    
    pip 20.0.1 from /Users/user_name/virtualenvironment/interface/lib/python3.7/site-packages/pip (python 3.7)
    
    
## Requirements

Create a virtual environment:

    $ pip install virtualenv
    
    $ virtualenv my_venv
    
    $ source my_venv/bin/activate

Install the requirements:
    
    $ pip install -r requirements.txt
   

## Run 

To run the program, go to the repository folder:
    
    $ python3 app.py

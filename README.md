# Admin-Console

This python program is made to easily add files to a local copy of a website and then push them to shared FTP server. These scripts have been written to make website managgement easier. Scripts are writter in python2.

### Requirements 

Depended libraries can be installed using `pip` and `requirement.txt`.
    
    pip install -r requirements.txt
You can jump to operations if dependencies are installed by above command. If you face any problem try installing these libraries independently.

This application uses two third party python libraries : 
    
 1. `WxPython`  
 You can check them out [here](https://www.wxwidgets.org/).
      
      To install on MacOS or Windows
      
          `pip install -U wxPython`
      
      To install on Linux 
        
        Build WxPython using pip 
          
          pip install -U wxPython
        
        If you don't want to build, you can follow my article about installation [here](https://www.dragzon.com/wxpython-on-linux/)
 
 2. `ObjectListView`
    
    You can check that [here](http://objectlistview.sourceforge.net/python/)
      
      To install ObjectListView 
      
           pip install objectlistview
           
           
### Operations
Before running this application, provide path to all directories and files in config.py.
To run this application clone this repository and run main.py
  
    python2 main.py

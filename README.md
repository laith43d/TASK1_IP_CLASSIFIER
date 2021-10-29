GIZ Task 1 - IP address classifier

Task resolution process:

* Fork the repo
* Clone the forked repo to your local machine
* Resolve the task
* Commit your solution
* Push to GitHub
* create a pull request

Task 1:

Important Note: No third party packages or libraries are allowed!

Build a command line tool that receives an IP address in the format: x.x.x.x/x, and print the class of the IP address.

Class resolution should contain the following information:
1. IP address class (A, B, C, D, E)
2. IP address designation (Private, Public, Special)

References:

[https://www.meridianoutpost.com/resources/articles/IP-classes.php](https://www.meridianoutpost.com/resources/articles/IP-classes.php)

[https://github.com/laith43d/ipcalculator-LZ-](https://github.com/laith43d/ipcalculator-LZ-)


python main.py 127.0.0.1/24

Output: Class: A, Designation: Special


python main.py 192.168.1.1/24

Output: Class: C, Designation: Private
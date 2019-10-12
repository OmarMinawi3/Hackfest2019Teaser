<h1>Hackfest 2019 Teaser</h1>
This is a multi-layered challenge. Solving the first challenge will lead you to the next one.
<br><br>
It is not required for students to complete the entire teaser challenge. Successful candidates will be chosen based on their submitted documentation.<br><br>Ensure to document and explain your thought process/methodology, including the reasoning behind your selected methods and the intended goal. The document should describe your process in depth, and include a small paragraph as to why you should be selected/would like to attend HackFest.<br><br>

Please submit your documentation file as a pdf to the contacts below by <b>October 18th</b>. Ensure to CC all 3 Netsoc executives. 

<h3>Your Netsoc point of contacts are:
  <ul>
  <li>Omar Minawi: omar.minawi@ontariotechu.net</li>
  <li>Mario Woo: sungsuk.woo@ontariotechu.net</li>
  <li>Dante Cupelli: dante.cupelli@ontariotechu.net</li>
  </ul>
  </h3>  


<h2>Setup/Installation</h2>

This python3 program uses the cryptography.io library. Please install this using:
  ```
  pip install cryptography
  ```
  or
  ```
  pip3 install -r requirements.txt
  ```
Clone the repo using the following command:
  ```
  git clone https://github.com/OmarMinawi3/Hackfest2019Teaser.git
  ```

<h2>Usage</h2>

The first argument after the file name is the password. Here is an example:
```
python3 teaser2019.py netsoc
```
This should return the following:
```
A-Z, a-z, 0-9. L47????p6
Entered password:  netsoc
Valid: False
```

<h2>Note</h2>
<b> This issue has been fixed. Please re-download the repo, and use the teaser2019.py file instead of the .pyc file. </b>
Windows users should be able to use teaser2019.pyc. Linux users (tested on kali and CentOS), use the linux_teaser.pyc file. 
<br><br>
The following output is an error. Some mac users may see this. If so, spin up a kali vm for the time being to complete the challenge. 

```
RuntimeError: Bad magic number in .pyc file
```

If you still get the above error after running the code on a supported os, please email omar.minawi@ontariotechu.net. In your email, state your os, what commands you typed to run the file, what you have done so far to troubleshoot the issue, and what error you get. 

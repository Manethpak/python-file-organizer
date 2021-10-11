# Python - File Organizer

Python file organizer application. 
<a href="https://github.com/Manethpak/python-file-organizer/releases/download/organizer/File.Organizer.exe">Download App Here.</a>

---

## How to use
<ul>
    <li> pipenv is required to install neccessary package 
        <br/>
        <code>pip install pipenv</code> to install pipenv
        <br/>
    </li>
    <li>
        After you have pipenv installed <br />
        <code>pipenv install</code> to install the necessary package
        <br/>
    </li>
    <li>
        <code>pipenv --venv</code> to get virtual environment path for interpreter.
        <br/>
    </li>
    <li>
        <code>pipenv shell</code> to enter python virtual environment shell
        <br/>
    </li>
</ul>

## How to build into exe with pyinstaller

Pyinstaller is going to be installed from pipfile, you can run the command belong to build one.
<br/>
<code>pyinstaller --noconfirm --onefile -w src/main.py</code>
<br/>
Find your exe file in `dist` directory

---

### From me

I'm just doing this project for fun and learning purpose because I was too lazy to organize my own folder...
Then I thought why not spend 5hr building an app rather than spend 10 minute organizing my own folder XD.
At first I was like just gonna write a quick script, then I was like maybe I'll add a GUI onto it so I can use it later
and that how we got here.
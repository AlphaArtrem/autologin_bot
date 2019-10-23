# **Name**
Login_Bot
Autologin bot to brute-force using a csv file containing list of usernames/id's and passwords.

# **Description**
This is a automation script to pass multiple logins cridentials  on any webpage stored in a `.csv file`.

# **Prerequisites**
`Pyhton3` installed with `Selenium` on your system.
`Google Chrome` installed on system(it may differ in your case but a web browser supporting `Selenium`).
A `csv` file contaning login credentials.

# **Installing**
1. For Windows
    - `python3` [download link](https://www.python.org/downloads/windows/)
    - `Selenium` Open console and run the command`pip install selenium` 
    - In my case `ChromeDriver` [download link](https://sites.google.com/a/chromium.org/chromedriver/downloads)
2. For Mac
    - `python3 and pip`
       ```bash
          $ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
          $ brew install python3
          $ curl -O http://python-distribute.org/distribute_setup.py
          $ python distribute_setup.py
          $ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
          $ python get-pip.py
    - `Selenium with chromedriver`
         ```bash
          $ brew cask install chromedriver
          $ pip3 install selenium
3. For Linux(In my case Ubuntu)
    - `python3 and pip` Open terminal and type in the following commands
        ```bash
          $ python3 --version 
          $ sudo apt-get update
          $ sudo apt-get install python3.6
          $ sudo apt update
          $ sudo apt install python3-pip
          $ pip3 --version
    - `Selenium with chromedriver` Open console and run the following command
         ```bash
          $ sudo apt-get update
          $ sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4
          $ sudo apt-get install default-jdk
          $ sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
          $ sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
          $ sudo apt-get -y update
          $ sudo apt-get -y install google-chrome-stable
          $ wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
          $ unzip chromedriver_linux64.zip
          $ sudo mv chromedriver /usr/bin/chromedriver
          $ sudo chown root:root /usr/bin/chromedriver
          $ sudo chmod +x /usr/bin/chromedriver
          $ wget https://selenium-release.storage.googleapis.com/3.13/selenium-server-standalone-3.13.0.jar
          $ wget http://www.java2s.com/Code/JarDownload/testng/testng-6.8.7.jar.zip
          $ unzip testng-6.8.7.jar.zip
          $ xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone.jar
          $ chromedriver --url-base=/wd/hub
          
# **Contributing**
Please read [CONTRIBUTING.md](https://github.com/AlphaArtrem/autologin_bot/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
  
# **Disclaimer**
Strictly for educational purposes , do not use for malicious purposes or you will be solely responsible

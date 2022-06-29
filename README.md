

<h1 align="center">Chromepass</h1>

  <p align="center"> 
Chromepass is a python script to extract Chrome passwords on Windows, as well as deleting them to prevent malicious users from being able to access them. This tutorial will teach you how to extract and decrypt Google Chrome browser saved passwords using Python with the help of <a href="https://docs.python.org/3/library/sqlite3.html">sqlite3</a> and other modules. We will also make a quick script to protect ourselves from such attacks. 
  </p>

## About

We live in an internet age, and with the internet comes a lot of advantages and disadvantages. And as end-users of the internet, it is important that we protect ourselves online. We live in a age where by [social engineering attacks](https://www.imperva.com/learn/application-security/social-engineering-attack/) is the order of the day. Hackers are always on the rampage of stealing user's private information, and in turn use the stolen information for many malicious purpose.

Take a moment and guess how many passwords you've stored in your Google Accounts. 50, 100 or even more. How many of the login details are highly sensitive (could be easily exploited by hackers). 

Now, think of what hackers might be able to do if they get hold of such information. Every day, we hear stories of hackers performing [phising attacks](https://www.imperva.com/learn/application-security/phishing-attack-scam/), after which they used the stolen information in performing many kinds of [identity theft](https://www.investopedia.com/terms/i/identitytheft.asp) ranging from using you debit card
to purchase things online, taking hold of your social media accounts like Facebook, Instagram, etc. 

## Getting Started

Follow the installation steps to open project without error

#### Installation 

1. Download and extract the project
2. Download python 3.x and install on your PC. My pc is 64bit so i installed Python3(64bit). Set environmental variable for both `python` and `pip` or else you get command not found.
3. I've used virtual environment. It's not necessary, but using virtual environment is preferable. \
   Note: You can skip the 3rd step if you don't want virtual environment \
   (i) Make sure you've set your python path in environmental variable and then install

   ```sh
   python -m venv venv 
   ```
   (ii) I've already created it. So now you want to activate it. I'm using windows. so I used CMD. Now open the cmd of your current project folder. My project folder is chromepass.
   ```sh
   D:\buchii\chromepass> cd /venv/Scripts/activate

   After venv is activated

   (venv) D:\buchii\chromepass>
   ```
   (iii) Once you close the project, this command is user to open the venv again and the deactivation command is also given.

    ```sh
    D:\buchii\chromepass>workon venv

    If not working again, activate your venv

    (venv) D:\buchii\chromepass>

    For Deactivating,

    D:\buchii\chromepass> cd /venv/Scripts/deactivate
    ```
4. Install the following requirements by following this command. 
   ```sh
   D:\buchii\chromepass> pip install -r requirements.txt
   ```
6. To run the the code, use this command
   ```sh
   D:\buchii\chromepass>python chromepass.py
7. If you get any error, make sure you've done the following things 
   ```
   1. Python version should be 3.x.
   2. Settingup Environment variables.
   3. Installed all requirements without errors.
   4. I am using 64 bit. If you are using 32 Bit google it and fix it.
   5. Everything is done.
   ```

## Usuage

This script is very simple to use. After installing all the necessary requirements and running the `python chromepass.py` in your terminal. A new text file called `login_data.txt` will be created in your file directory. The `login_data.txt` file contains 
* **origin_url:** The name of the website 
* **username:** Your login username
* **password:** Your login password 
* **creation_date:** The date you created the account
* **last_used_date:** The date you last logged into the account

Depending on how long you've been saving passwords in Chrome, you might end up with a pretty long or pretty short list. 



## 📌 Disclaimer 📌

* ⚠️ Please run this script on your machine or on a machine you have permission to access, I do not take any responsibility for any misuse.

* ⚠️ This is just for educational purposes, so kindly treat it as one. 

## Contributions 

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated.**

1. Fork the Project
2. Clone into your local machine
3. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
4. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.




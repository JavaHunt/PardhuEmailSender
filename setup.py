from setuptools import setup, find_packages

setup(
  name = 'PardhuEmailSender',         # How you named your package folder (MyLib)
  packages = ['PardhuEmailSender'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This package will allow you to send bulk emails',   # Give a short description about your library
  long_description= """
  -- prerequisites

    Follow the below steps to enable your gmail account to send emails.. 
    This is necessary for sender only... No need to Follow the below steps for receiver email (client)
    Step 1 : Go to your email settings
    Step 2 : Click on the " Security " Tab 
    Step 3 : Turn on two step verification
    Step 4 : Click on app passwords which is under two step verification option 
    Step 5 : Give your email password and click on sign in
    Step 6 : Now you will see your email device app passwords if you have any....
    Step 7 : In the " select app " option menu, select Mail and in the " select device " option menu, select your OS (select 'Windows Computer' if you are windows system user)
    Step 8 : Click on Generate
    Step 9 : You will get 16 char long password, this is your mail account password. Use this password to send emails without interruption


    Please check all the prerequisites above and continue the process
""",
  author = 'Mallela Pardha Saradhi',                   # Type in your name
  author_email = 'pardhu9100@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/JavaHunt',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/JavaHunt/PardhuEmailSender/archive/refs/tags/1.0.tar.gz',    # I explain this later on
  
  keywords = ['Email', 'Email Bomber', 'Bulk mails', 'Gmail', 'Smtp', 'Email sender'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'email',
          'smtplib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
  ],
)
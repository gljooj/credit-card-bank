<h1> Authorizer </h1>

<p>
This Project was created with the objective of carry out banking transaction follow the rules proposed by the bank instituition</p>


<h2>How to Run</h2>

<h3> Preparing the environment</h3>
<p> How is nothing too complex the environment is more prepared for perform tests</p>

<p> Execute:</p>
(os & Linux)

1 - `virtualenv .venv` <br>
2 - `source .venv/bin/activate` <br>

(Windows)

1 - `python -m venv .venv` <br>
2 - `source .venv/Scripts/activate` <br>

3 - `pip install -r requirements.txt` <br>

<p>To execute the project you must execute on the root project the follow command:</p>

`python3 authorizator.py < operations` <br>

<p> To verify all the tests proposed you must 
  access the tests/test.py and execute the run(pytest) or use a framework (preference pycharm)</p>

<h1> Explaining the project</h1>

<h2> infrastructure/Authorizer.py</h2>
This file is the firs authorization layer, where the establishment/credit card machine have the freedom to know 
the status of client's credit card or know if the is a valid credit card.

<h1> infrastructure/Account.py</h1>

This file is the account layer, here the app execute the process of captures of credit card errors for example:
if have the limit to buy something, range buy or duplicate buy.

<h1> infrastructure/ToolsAccount.py</h1>
Este arquivo seria como um helper para o Account, nele tem algumas ferramentas de ajuda para o Account.
This File is a helper to the account, here have some helper tools for the Account 

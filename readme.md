<h1> Authorizer </h1>

<p>Esse projeto foi criado com o intuito de realizar verificações de transações bancárias de compras
seguindo as regras propostas pelo nubank</p>

<h2>How to Run</h2>

<h3> Preparando o ambiente</h3>
<p> Como não é algo tão complexo o ambiente ficou mais preparado para 
realizar os testes</p>

<p> Execute:</p>

1 - `virtualenv .venv` <br>
2 - `source .venv/bin/activate` <br>
2 - `pip install -r requirements.txt` <br>

<p>Para executar o projeto você deve executar na raiz do projeto o seguinte comando:</p>

`python3 authorizator.py < operations` <br>

<p> Para verificar todos os testes proposto você deve acessar em tests/test.py <br> 
e então executar o run (preferencia pycharm) </p>

<h1> Explicando o projeto</h1>

<h2> infrastructure/Authorizer.py</h2>
Este arquivo seria a camada de primeira autorização, onde o estabelecimento/maquininha tem liberdade em saber
o estado do cartão do cliente ou se aquele cartão é válido.

<h1> infrastructure/Account.py</h1>
Este arquivo seria a camadada de conta, já aqui o app executa os processos de capturas de erros internos
como por exemplo se tem limite ou não para aquela compra, range de compra e dupla compra.

<h1> infrastructure/ToolsAccount.py</h1>
Este arquivo seria como um helper para o Account, nele tem algumas ferramentas de ajuda para o Account.

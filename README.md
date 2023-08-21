# Turismo-Irrestrito

## Descrição 

  O objetivo deste projeto é desenvolver um site que apresente informações detalhadas sobre acessibilidade nos pontos turísticos do Brasil, incluindo recursos de acessibilidade específicos para facilitar o acesso de pessoas com deficiência física e mobilidade de locomoção reduzida. Essa iniciativa visa promover o turismo inclusivo no país, permitindo que todos possam desfrutar plenamente das atrações turísticas disponíveis.

### Desenvolvedores/Designs:

* [Aurilene Bagagi](https://github.com/AurileneBagagi)
* [Felipe Santana](https://github.com/FelipeSantanaC)
* [Moises Victor](https://github.com/grsmth)
* [Pablo Renato](https://github.com/pablorenato1)
* [Paulo Danilo](https://github.com/DanCostaDev)

### Scrum Master

* Débora Silva;
* Manussa Santos;

### Tecnologias Utilizadas:

* HTML e CSS;
* Python;
* Django;
* JavaScript;
* MySQL:

### Bibliotecas/Dependências Utilizando:
* django;
* django-cors-headers;
* djangorestframework;
* PyMySQL;
* mysqlclient;
* Cryptography;
* mysql.connector;

## Instruções para executar:
1. Instalar as dependências/bibliotecas;
2. Instalar o workbench MySQL (caso não tenha) e execute o script
3. no arquivo <code>Turismo-Irrestrito\authRst\authRst\settings.py</code> mude as configurações de login do MySQL Workbench
4. no terminal execute o comando: 
<code>python manage.py migrate</code> (reinicie o arquivo script se necessario)
5. execute o arquivo "local_load_data_script.py";
6.  no terminal execute o comando: <code>python manage.py runserver</code>
7. Abra no navegador o link fornecido no terminal.
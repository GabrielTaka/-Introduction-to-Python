
# PYTHON





<h3>INTRODUÇÃO</h3>

<p>O senso comum é que o Python é uma linguagem interpretada. Interpretado significa que não há um processo de compilação que traduz o código fonte em algum código nativo que o seu computador entende. A documentação do Python confirma isso, no entanto também menciona a presença de um compilador.</p>

<p>"Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler."</p>

<p>A linguagem vem ganhando muita popularidade ultimamente pois apresenta uma maneira simples, livre e agradável de se programar e tem se mostrado tão poderosa quanto linguagem robustas como JAVA.</p>

<br>

<h3>TIPOS PRIMITIVOs</h3>
<br>
<p>Tipos primitivos em toda linguagem de programação são basicamente os estilos de atribuição que uma variável pode receber pelo input do usuário.</p>

<ul>
 <li><b>Int:inteiro					%d</li>
  <li>Float:<b>número com ponto flutuante:	%f</li>
  <li>Bool:<b>True or False</li>
  <li>Str:<b>string 					%s</li>
</ul>

Em Python existem duas formas para exibir o valor de uma variável sendo eles:
<ul>
   Print (“{}”. format(variável))<li>

	<li>Print (“%tipo da variável” %variável) </li>
</ul>

Variável.isnumeric()
•	Verifica se o valor da variável é número.

Variável.isalpha()
•	Verifica se o valor da variável é letra.











3.	OPERADORES NUMÉRICOS

+
•	soma
-
•	subtração
*
•	multiplicação
/
•	divisão
//
•	divisão inteira
%
•	resto da divisão
**
•	exponenciação


4.	MÓDULOS

Import
•	Inclui uma biblioteca completa

From nome-da-biblioteca import nome-da-função
•	Faz com que seja incluído apenas uma função desejada da biblioteca definida.




Import math 
•	Biblioteca com funcionalidades matemáticas 

Ceil
•	Arredonda o número para “cima”

Floor
•	Arredonda um número para “baixo”

Pow
•	Potenciação de um número

Sqrt
•	Raiz quadrada

Factorial
•	Fatorial de um número.

Trunc
•	Exclui a parte decimal de um número

Hypot
•	Calcula o comprimento da hipotenusa

Cos
•	Calcula o comprimento o cosseno

Sin
•	Calcula o comprimento o seno

Tan
•	Calcula o comprimento a tangente

radians
•	Converte o ângulo em PI


Random
•	Biblioteca que sorteia, organiza, elementos de uma lista, variável.

Random.randint(de,até) ex: (1,10)
•	Sorteia um número de 1 a 10 como no exemplo.

Random.choice
•	Pega um elemento aleatório da lista

Random.shuffle
•	Embaralha a lista

Random.sort
•	Ordena uma lista 









5.	STRING

Variável = [índice:índice]
•	Pega o conteúdo entre os índices.
EX:
Variavel=[0:9]
•	A variável será exibida desde o primeiro indicie (0) até o índice anterior ao 9.

Variável=[índice:índice:num]
•	O terceiro incremento faz com que a variável seja exibida dentro dos índices pulando letras
EX:
Variável = [0:9:2]
•	Faz com que o conteúdo que está entre 0 e 9 seja exibido pulando uma letra

Variável=[:índice]
•	A variável é exibida desde o seu início até o índice solicitado.

Varável=[índice:]
•	A variável é exibida desde o índice solicitado até o final.


Len(variável)
•	Retorna o tamanho da string.

Variável.count(‘caractere’)
•	Conta quantas vezes o caractere solicitado apareceu.


Variável.find(‘caracteres’)
•	Encontra a string e indica em qual módulo está.

‘string’ in frase
•	Retorna true caso a string esteja contida em frase ou false caso negativo.


6.	TRANSFORMAÇÃO

Variável.replace(‘palavra na lista’,’palavra desejada’)
•	Troca a palavra

Variável.upper()
•	Transforma as letras da variável em maiúsculas.

Variável.captalize()
•	Transforma toda primeira letra da frase em maiúsculo.

Variavel.strip()
•	Remove os excessos de espaço no começo e no fim da string.

Variável.split()
•	Divide um conjunto de palavras.

‘-‘.join(variável)
•	Faz a junção de palavras

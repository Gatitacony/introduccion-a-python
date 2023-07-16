#Introduccion-a-python
Python es uno de los lenguajes de programación más populares del mundo. Es ampliamente utilizado en el desarrollo web y de juegos, análisis de datos, data science, machine learning y muchos más.

Salida 
El comando o instrucción print es la forma más sencilla de enviar un mensaje específico a la pantalla u otro dispositivo de visualización. 
Este mensaje o salida puede ser un número, un texto o el resultado de un cálculo.
La declaración print siempre va seguida de paréntesis que contiene la salida que queremos generar.

Los ordenadores tratan de forma diferente el texto y los número. al imprimir texto, debe encerrarlo entre comilla simples o dobles.

Datos numéricos
Operar con dato numèricos en python permite ralizar cálculos, automaticar fórmulas y resolver problemas numéricos como la optimización de rutas para la navegación autónoma de drones.
Para obtener el resultado de un cálculo, basta con introducir la operación matemática directamente en la declaración print.
Al igual que en matemáticas, utilizamos + y - para sumar y restar. La multiplicación se realiza mediante el simbolo * . La división se realiza mediante una barra diagonal /.

Tipos de datos Numéricos 
Indican a un ordenaro cómo interpretar, almacenar y operar con el valor.
Los tipos de datos numéricos más utilizados son: 
Integer: Un número entero, sin punto decimal, que puede ser positivo (1,2,3,...), negativo (-1,-2,-3,...) o cero.
Float: Un númeron que tiene decimales, también puede ser positivo (1,5 , 3,14 , 5,5) o negativo (-1,5 , -3,14).

Depurar
Los errores en el código también se conocen como bugs. Depurar (debugging) es el proceso de encontrar y corregir errores en el código. error en el codigo: print(100 x 100
correción: print(100 * 100)

Texto vs. Números
Un dato de texto se denomina cadena(string)

Concatenación 
Podenos unir dos cadenas, tambien conocido como concatenación.

Cadenas
Cualquier cosa entre comillas es una cadena, incluso los números. Los números entre comillas se tratan como datos de texto y no podrás realizar operaciones aritméticas con ellos.

Multiples líneas
Hay situaciones en las que puede que desees utilizar la orden print varias veces. Cada instrucción print imprime el texto en una nueva línea.

Múltiples salidas
El comando print puede tomar múltiples valores para imprimirlos en la misma línea. Esto puede hacerse separándolos con comas.

Separadores de salida
Al imprimir varias salidas, puedes personalizar el separador utilizando el parámetro sep.
El parámetro sep debe definirse siempre después de los valores de la orgen de impresión.

Puedes añadir comentarios a tu código para añadir anotaciones y explicaciones empezando por #

Conservar información en la memoria 
Los datos tienen diferentes formas. Si estás interesado en trabajar con una pieza de datos, necesitas encotrar una manera para que tu programa mantenga esta información en su memoria. Las variables nos permiten hacerlo. Las piezas de información pueden ser etiquetadas, almacenadas y accedidas con variables.
¿Qué es una variable?
Puedes pensar en una variable como una caja que contiene algo. Una variable tiene una etiqueta o name y contiene una value. Le permite almacenar un value asinándolo a un name. El nombre puede utilizarse para referirse al valor màs adelante en el programa.

Usando variables
Vamos crear una variable conectando el nombre y el valor utilzando un signo igual.
el siguiente ejemplo almacena el numero 15 en una variable llamada points.

Asignar a la variable 
Puedes asignar cualquier tipo de valor a tu variable. Tambien puedes utilizarla para realizar operaciones con ella. Una variable almacena el valor a lo largo del programa.

Reasignar variables
Las varisables pueden reasignarse tantas veces como sea necesario.

Nombres de variables
Puedes nombrar las variables de diferentes maneras. Puedes usar letras y guiones bajos. Puedes usar números siempre que no empieces el nombre de una variable con un número. No puedes utilizar caracteres especiales como % . Python es un lenguaje que distingue entre mayúsculas y minúsculas. Esto quiere decir que Lastname y lastname son dos nombres de variables diferentes.

Salida
Como has visto, puedes utilizar variables en la declaración print para mostrar sus valores. 
Si necesitas imprimir varias variables en la misma línea, puede separarlas con comas en la declaración print.

Interacción con el usuario
Muchos programas informáticos están diseñados para que otros usuarios puedan interactuar con ellos. Estos prgramas toman información de los usuarios. Por ejemplo, un juego puede pedir el nombre y la edad del usuario para utilizarlos durante la partida.

Input del usuario
El comando input() pregunta al usuario y devuelve lo introducido como una cadena. Aunque el usuario introduzca un número como entrada, se procesa como una cadena. El comando input() debe ir seguido de un paréntesis.

Input como número
Para convertirlo en un número, puede utilizae la función int().

Convertir a float
De manera similar a la función int(), la función float() convierte una cadena en un float

Convertir a cadena 
A veces puede ser necesario utilizar un número en una concatenación de cadenas. Para ello se utiliza la función str(), que convierte un número en una cadena.

Múltiples inputs
Puedes usar input() múltiples veces para tomar múltiples entradas de usuario.

Operadores In-Place
Los operacores In-place te permiten escribir código como 'x = x + 3' de forma más concisa, como 'x += 3'. Los operadores In-place puede utilizarse para cualquier operación numérica (+, - , *, /, %, **, //). También puedes utilizarlo para una concatenación de cadenas.

Boleanos
Ya hemos conocido las cadenas, los enteros y los floats. Añadamos Booleanos(Booleans) en la mezcla.
Los booleanos pueden tener dos valores: True y False. Podemos crear booleanos comparando valores mediante el operador igual == .
No confundir la asignación (un signo igual) con la comparación (dos signos iguales).
El tipo de dato booleano tiene uno de los dos valores posible: True y False.
Ten en cuenta que los valores deben comenzar con una letra mayúscula.

Comparadores
Los booleanos se crean al comparar valores. Python tiene una serie de operadores de comparación: igual a == , no igual a != , mayor que > , menor que < , mayor o igual que >= , menor o igual que <=. Los operadores de comparación también se denominan Operadores relacionales.
Los operadores mayor que y menor que también pueden utilizarse para comparar cadenas lexicográficamente (el orden alfabético de las palabras se basa en el orden alfabético de las letras que las componen).
Los valores True y False pueden representarse como enteros 1 y 0 respectivamente.

Declaraciones if
Una cosa que se puede hacer con los booleanos es utilizar declaraciones if para ejecutar un código basado en una determinada condición, por ejemplo, si el booleano se evalúa como True.
Una declaración if se ve asi:
if condition:     #condición
    statements    #declaraciones
Python usa sangría (ese espacio vacío al principio de una línea) para delimitar bloques de código.
Dependiendo de la lógica del programa la sangría puede ser obligatoria. Las declaraciones en if deben tener sangrías. Los dos puntos al final de la expresión en la declaración if son importantes, no los dejes fuera. Las declaraciones if pueden estar anidados, uno dentro de otro. La sangría se utiliza para definir el nivel de anidamiento.

Declaraciones else
La declaración else puede utilizarse para ejecutar algunas declaraciones cuando la condición de la declaración if es False.
Al igual que con las declaraciones if, el código dentro del bloque necesita ser sangrado. Los dos puntos al final de la palabra clave else es importante, no lo dejes de lado.
Cada bloque de declaración if sólo puede tener una declaración else.
Así que para que podamos hacer múltiples comprobaciones, necesitamos encadenar las declaraciones if y else.
La sangría determina a las declaraciones if/else a la que pertenecen los bloques de código.

Declaraciones elif
Demasiadas declaraciones if/else hacen tu código largo y díficil de leer.
La mejor manera de resolver esto es declaración elif(abreviatura de else if). Es un atajo para usar cuando se encadenan declaraciones if y else, hacer el código más corto y fácil de leer.

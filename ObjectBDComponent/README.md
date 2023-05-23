# component for zodb

<h2> Que es això </h2>
<p>Es tracta d'un component que crea una base de dades per zodb i és capaç d'inserir i recuperar dades dintre d'aquesta.</p>
  
  
  
  
  
  <h2> requisits </h2>
  <p>Versió de Python: python 3</p>
 <p>Cal recordar que per utilitzar-lo cal instal·lar zodb a dintre del projecte partint des de la base que ja es té instal·lat Python.</p>

```
pip install zodb
```

<h2> instalació </h2>
<p>Per utilitzar el component cal importar-lo des del lloc on l'utilitzarem</p>

```
from zodbComponent import zodbComponent
```
<h2>ús</h2> 

<h3>declarar el nom de la base de dades </h3>
<p>Abans de res cal declarar la vas de dades on es guardaran les dades</p>
  
```
z1 = zodbComponent("partides.fs") 
```

<h3>insertar </h3>
<p>Per inserir dades cal donar un string amb una string amb el nom de la taula i un objecte a inserir
</p>
  
```
zodb.insert('name_of_the_table',object_to_save) 
```


<h3>recuperar</h3>
<p>Per recuperar dades donem una string amb el nom de la taula
</p>
  
```
zodb.recuperar('name_of_the_table') 
```



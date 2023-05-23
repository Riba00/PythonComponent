# component for zodb

<h2> Que es això <h2>
<p>es tracta d'un component que crea una base de dades per zodb i es capaç de insertar i recuperar dades dintre d'aquesta  </p>
<h2> instalació <h2>
<p>per utilitzar el component cal importar-lo des del lloc on anem a utilitzar-lo </p>

```
from zodbComponent import zodbComponent
```
<h2>utització</h2> 

<h3>declarar el nom de la base de dades </h3>
<p>avans de res cal declarar la bas de dades on es guardaran les dades</p>
  
```
z1 = zodbComponent("partides.fs") 
```

<h3>insertar </h3>
<p>per insertar dades cal donar un string amb  una string amb el nom de la taula i un objecte a insertar 
</p>
  
```
zodb.insert('name_of_the_table',object_to_save) 
```


<h3>recuperar</h3>
<p>per recuperar dades donem una string amb el nom de la taula
</p>
  
```
zodb.recuperar('name_of_the_table') 
```



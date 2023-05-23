# component for zodb
## instalació 
<p>per utilitzar el component cal importar-lo des del lloc on anem a utilitzar-lo </p>

```
from zodbComponent import zodbComponent
```
<h2>utització</h2> 

<h3>declarar el nom de la base de dades </h3>
<p>avans de res cal declarar la bas de dades on es guardaran les dades  
</p>
<p>z1 = zodbComponent("partides.fs") 
</p>

<h3>insertar </h3>
<p>per insertar dades cal donar un string amb  una string amb el nom de la taula i un objecte a insertar 
</p>
<p>zodb.insert('name_of_the_table',object_to_save) 
</p>


<h3>recuperar</h3>
<p>per recuperar dades donem una string amb el nom de la taula
</p>
<p>zodb.recuperar('name_of_the_table') </p>



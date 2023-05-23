# component for zodb
## instalation 
<p>per utilitzar el component cal importarlo desde el lloc on anem a utilitzar-lo </p>
<p>from zodbComponent import zodbComponent</p>
<h2>usage</h2> 

<h3>declarar el nom de la base de dades </h3>
<p>avans de res cal declarar la bas de dades on es guardaran les dades  
</p>
<p>z1 = zodbComponent("partides.fs") 
</p>

<h3>insert </h3>
<p>per insertar dades cal donar un string amb  una string amb el nom de la taula i un objecte a insertar 
</p>
<p>zodb.insert('name_of_the_table',object_to_save) 
</p>


<h3>recuperar</h3>
<p>per recuperar dades donem una string amb el nom de la taula
</p>
<p>zodb.recuperar('name_of_the_table') </p>



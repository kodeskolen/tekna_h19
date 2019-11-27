# Plotting i repl.it

[repl.it](https://repl.it) er en alternativ kode-editor som lar deg kjøre Pythonkode i nettleseren.
Men, om du bruker repl.it så fungerer ikke `show` funksjonen i `pylab`. Istedenfor,
så må du lagre alle figurene du vil vise frem med `savefig` funksjonen. `savefig`
fungerer nesten likt som `show`, men den tar et argument: filnavn. Dette blir navnet
på bildet som lagres av figuren din.

Men, om du bruker savefig så vil ikke plottet rengjøres hver gang du viser det frem.
Dette kan bli problematisk om du ønsker å lage et plot, vise det frem, lage et nytt
plot og vise det frem. Derfor har jeg lagd denne funksjonen som får show til å 
virke i [repl.it](https://repl.it). hvis du vil bruke denne `show`-funksjonen så er det bare å kopiere den 
inn til like under der du importerer `pylab`.

````python
def show():
    savefig("plot.png")
    figure()  # Her lager vi en ny figur som neste plot blir laget i
````

Her er et eksempel hvor vi bruker denne funksjonen

````python
from pylab import *
def show():
    savefig("plot.png")
    figure()  # Her lager vi en ny figur som neste plot blir laget i

x = arange(1, 10, 0.1)
y = x**2

plot(x, y)
show()
````

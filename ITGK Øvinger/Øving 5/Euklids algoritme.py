#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
#     <li><a href="Lokale%20variabler.ipynb">Lokale variabler</a></li>
#     <li><a href="Globale%20variabler.ipynb">Globale variabler</a></li>
#     <li class="active"><a href="Euklids%20algoritme.ipynb">Euklids algoritme</a></li>
#     <li><a href="Primtall.ipynb">Primtall</a></li>
#     <li><a href="Multiplikasjon.ipynb">Multiplikasjon</a></li>
#         <li><a href="Den%20store%20sporreundersokelsen.ipynb">Den store spørreundersøkelsen</a></li>
#     <li><a href="Arbeidsdager.ipynb">Arbeidsdager</a></li>
#     <li><a href="Sekantmetoden.ipynb">Sekantmetoden</a></li>
#     <li><a href="Not%20quite%20Blackjack.ipynb">Not quite Blackjack</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Euklids algoritme
# 
# **Læringsmål:**
# - Funksjoner
# - Algoritmer
# - Løkker
# 
# **Starting Out with Python:**
# - Kap. 5.2-5.5
# 
# Et vanlig problem i matematikken er å finne den største felles divisoren av to tall. I denne oppgaven skal du lage en funksjon som finner dette tallet, og så bruke funksjonen til å forkorte brøker. 
# 
# Eksempelvis vil det største tallet som deler både 20 og 30 være 10, brøken 20/30 kan derfor forkortes til 2/3 ved å dele på 10 i både teller og nevner. 
# 
# Dette problemet kan løses ved hjelp av Euklids algoritme. Pseudokode for Euklids algoritme er som følger: 
# 
# ```
# Gitt inputparametere a og b, begge heltall.
# Gjenta så lenge b ikke er 0:
#     Tilegn den nåværende verdien av b til en ny variabel gammel_b.
#     Tilegn til b resten etter a dividert på b.
#     Tilegn til a verdien av gammel_b.
# Returner a som resultat av algoritmen
# ```

# ## a)

# Lag en funksjon `gcd` (Greatest Common Divisor) som tar inn to tall, utfører Euklids algoritme, og returnerer den største felles divisoren. For eksempel skal `gcd(30,10)` returnere svaret `10`
# 
# ***Skriv funksjonen `gcd` i kodeblokken under og test at den funker som den skal***

# In[5]:


def gcd(a,b):
    while b:
        a, b = b, a%b
    return a
gcd(30,10)


# ## b)
# 
# Du skal nå bruke gcd-funksjonen til å forkorte brøker. 
# 
# Lag en funksjon reduce_fraction som tar inn to positive heltall `a` og `b` og bruker gcd-funksjonen definert i forrige deloppgave for å finne største felles divisor `d`. 
# 
# Funksjonen skal returnere `a/d` og `b/d`.
# 
# ***Skriv funksjonen `reduce_fraction` i kodeblokken under***

# In[8]:


def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def reduce_fraction(a,b):
    s=(a/gcd(a,b))
    t=(b/gcd(a,b))
    u=print(f'{s:.0f}/{t:.0f}')
    return u

reduce_fraction(5, 10)
reduce_fraction(4, 2)
reduce_fraction(42 , 13)


# Under finner du testkode for å sjekke at funksjonen din fungerer som den skal (husk å trykke `ctrl + enter` i kodeblokken med funksjonen din før du kjører denne)

# In[ ]:


# TESTKODE FOR reduce_fraction
print ("%d/%d" % reduce_fraction (5, 10))
print ("%d/%d" % reduce_fraction (4, 2))
print ("%d/%d" % reduce_fraction (42 , 13))


# Hvis din versjon av `reduce_fraction` fungerer som den skal vil du få følgende output fra testkoden:
# 
# ```
# 1/2
# 2/1
# 42/13
# ```

# #### Tips

# - For å returnere to variabler fra en funksjon separerer man returverdiene med komma: `return var_a, var_b`
# 
# - Man kan også tilegne verdier til to variabler på samme kodelinje, dette gjøres ved å skrive: `a, b = funksjon_med_to_returverdier()` der funksjonen kalles.

#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving6.ipynb">Øving 6</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Generelt%20om%20lister.ipynb">Generelt om lister</a></li>
#     <li ><a href="Lett%20og%20blandet.ipynb">Lett og blandet</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Vektorer.ipynb">Vektorer</a></li>
#     <li ><a href="Lister%20og%20lokker.ipynb">Lister og løkker</a></li>
#     <li class="active"><a href="Teoridelen%20paa%20eksamen.ipynb">Teoridelen på eksamen</a></li>
#     <li><a href="Gangetabell%20og%20lister.ipynb">Gangetabell og lister</a></li>
#     <li ><a href="Lotto.ipynb">Lotto</a></li>
#     <li ><a href="Tannfeen.ipynb">Tannfeen</a></li>
#         <li><a href="Chattebot.ipynb">Chattebot</a></li>
#     <li ><a href="Matriseaddisjon.ipynb">Matriseaddisjon</a></li>
#     <li ><a href="Intro%20til%20numpy-arrays.ipynb">Intro til numpy-arrays</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Teoridelen på eksamen
# 
# **Læringsmål:**
# 
# * Lister
# * funksjoner
# 
# **Starting Out with Python:**
# 
# * Kap. 7
# 
# I denne oppgaven skal du sammenligne to lister og studere hvor like de er hverandre. 
# 
# 25% av eksamen er flervalgsoppgaver, og her skal vi anta at det alltid vil være 20 oppgaver. Riktige svar for oppgavene er som følger:

# Riktige svar|- |- |-
# ---|---|---|---
# 1.A|6.A|11.D|16.A
# 2.C	|7.B|	12.A|	17.B
# 3.B|	8.A	|13.C	|18.A
# 4.D	|9.C|	14.C|	19.C
# 5.A	|10.A|	15.B|	20.D
# 

# **a)** 
# Lag en liste *fasit* som inneholder de korrekte svarene.
# 
# ***Skriv svaret ditt i boksen under.***

# In[8]:


fasit=['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'C', 'D']


# **b)**
# Lag en funksjon `sjekk_svar` som tar inn studentens_svar som argument. studentens_svar er en liste som inneholder en students svar på oppgavene. Ved å sammenligne studenten sine svar med de riktige svarene, skal funksjonen returnere hvor mange prosent av oppgavene studenten klarte. 
# 
# Eksempel på kjøring:
# 
# ```python
# print(sjekk_svar(['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'A', 'C'])) # Gir 90% riktig
# print(sjekk_svar(fasit)) # Gir 100% riktig
# ```
# 
# ***Skriv svaret ditt i boksen under.***

# In[9]:


def sjekk_svar(svar):
    s=0
    for i in range(0,20):
        if svar[i]==fasit[i]:
            s+=5
    print(f'{s}% riktig')

print(sjekk_svar(['A', 'C', 'B', 'D', 'A', 'A', 'B', 'A', 'C', 'A', 'D', 'A', 'C', 'C', 'B', 'A', 'B', 'A', 'A', 'C'])) # Gir 90% riktig
print(sjekk_svar(fasit)) # Gir 100% riktig


# Har du gjort det på riktig måte skal koden under gi 20% riktig. Trykk på blokka under og trykk `ctrl + enter` for å kjøre den.

# In[10]:


print(sjekk_svar(['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']))


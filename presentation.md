# Les idiomes en Python 2.7

<small>Traduction libre de &laquo; Writing idiomatic python &raquo; de [@jeffknupp](https://twitter.com/jeffknupp)</small>

---

# Idiomes ?

* du grec &laquo; *idios* &raquo; signifiant &laquo; *propre* &raquo;, &laquo; *spécial* &raquo;

---

# Idiomes ?

* *idioma* (pour le latin), idiotisme, qui est une forme ou locution propre à une langue, restant impossible à traduire littéralement dans une autre langue de structure analogue ex: anglicisme.

* *idiôma* (en grec), particularité propre à une langue

---

# Pourquoi ?

* Du code cryptique peut être rédigé par des programmeurs de tous les niveaux, et ce, peu importe le langage de programmation

---

# Comment peut-on mieux se comprendre ?

En écrivant du code idiomatique.

---

# Comment apprendre les idiomes en python ?

* Écrire du code et se faire réviser par nos collègues plus expérimentés
* Lire le code de nos collègues plus expérimentés
* Lire le bouquin de Jeff Knupp :)

---

# ```Si``` logique

---

## Comparaisons chaînées

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    if x <= y and y <= z:
        return True

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    if x <= y <= z:
        return True

---

## Éviter de tout mettre sur une même ligne

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    name = 'Bernard'
    address = 'Québec, CA'

    if name: print(name)
    print(address)

---

## Éviter de tout mettre sur une même ligne (partie 2)

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    name = 'Bernard'
    address = 'Québec, CA'

    if name:
        print(name)
    print(address)

---

## Vérifier la valeur d'une même variable avec un *ou* logique

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    is_generic_name = False
    name = 'Tom'

    if name == 'Tom' or name == 'Dick' or name == 'Harry':
        is_generic_name = True

---

## Vérifier la valeur d'une même variable avec un *ou* logique

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    is_generic_name = False
    name = 'Tom'

    if name in ("Tom", "Dick", "Harry"):
        is_generic_name = True

---

## Éviter les comparaisons directes avec ```True```, ```False```, ```None```

## Pourquoi ?

    !python
    None == False
    0 == False
    [] == False # liste vide
    {} == False # dict vide

---

## Éviter les comparaisons directes avec ```True```, ```False```, ```None```

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    def empty_list(a=[]):
        # la liste "a" est vide
        if len(a) == 0:
            return True
        return False

---

## Éviter les comparaisons directes avec ```True```, ```False```, ```None```

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    def empty_list(a=[]):
        # la liste "a" est vide
        if not a:
            return True
        return False

---

## Éviter les comparaisons directes avec ```True```, ```False```, ```None```

<h3><i class="fa fa-thumbs-up"></i> <i class="fa fa-thumbs-up"></i></h3>

    !python
    def empty_list(a=[]):
        # la liste "a" est vide
        return not a

---

## Bonus: ```Si``` ternaire

    !python
    a = []
    is_empty = False if a else True

---

# Boucle ```for``` et ```while```

---

## Utiliser ```in``` pour boucler dans une liste

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    index = 0

    while index < len(alphabet):
        print alphabet[index]
        index += 1

---

## Utiliser ```in``` pour boucler dans une liste

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for letter in alphabet:
        print letter

---

## Utiliser la fonction ```enumerate``` pour avoir un compteur dans une boucle

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    index = 0

    for letter in alphabet:
        print("{}, {}".format(index, letter))
        index += 1

---

## Utiliser la fonction ```enumerate``` pour avoir un compteur dans une boucle

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    for index, letter in enumerate(alphabet):
        print("{}, {}".format(index, letter))

---

## Utiliser le ```else``` du ```for```

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    for user in users:
        has_invalid_email = False

        for email in user.emails:
            if email_is_invalid(email):
                has_invalid_email = True
                print("Possède un courriel invalide !")
                break

        if not has_invalid_email:
            print("Ces courriels sont valides !")

---

## Utiliser le ```else``` du ```for```

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    for user in users:
        for email in user.emails:
            if email_is_invalid(email):
                print("Possède un courriel invalide !")
                break
        else:
            print("Ces courriels sont valides !")

---

# Plein d'autres trucs au hasard !

---

## Créer un ```path``` menant à un répertoire/fichier

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    path = "../foo/" + username + "/Documents"

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    import os.path as op
    path = op.join("..", "foo", username, "Documents")

---

## Retourner une valeur par défaut lorsqu'une clé n'existe pas dans un dictionnaire

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    a_string = ""
    if key in my_dict:
        # do something
        a_string = my_dict[key]
    else:
        a_string = "une valeur par défaut"

---

## Retourner une valeur par défaut lorsqu'une clé n'existe pas dans un dictionnaire

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    a_string = my_dict.get()

---

## Utiliser des ```list comprehensions``` pour des boucles simples de transformation



---

# Recommandations pour apprendre les idiomes d'un langage de programmation

* Lire le PEP8
* Lire le code de module existant et populaire
* Demandez à un ami/collègue de vous réviser

---

# Questions ?

## Commentaires/Bashing ?

---

# Merci !

* Je pars pour montréal et j'apporte: un bouquin pour la route
* Fruit que je mangerai éternellement: Melon d'eau
* bernardchhun.com

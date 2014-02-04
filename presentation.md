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
* Lire et appliquer le PEP8
* Lire le code de modules existants et populaires
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

## Éviter de tout mettre sur une même ligne

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    name = 'Bernard'
    address = 'Québec, CA'

    if name:
        print(name)
    print(address)

---

## Vérifier toutes les valeurs possibles d'une variable

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    is_generic_name = False
    name = 'Tom'

    if name == 'Tom' or name == 'Dick' or name == 'Harry':
        is_generic_name = True

---

## Vérifier toutes les valeurs possibles d'une variable

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

## Standard de nommmage des class/functions/variables

    !python
    class UneClasseGigantesqueEtJavaesque:
        pass

    une_variable = "foo"

    def une_fonction():
        pass

    UNE_CONSTANTE = 60 * 60

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
        a_string = my_dict[key]
    else:
        a_string = "une valeur par défaut"

---

## Retourner une valeur par défaut lorsqu'une clé n'existe pas dans un dictionnaire

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    a_string = my_dict.get(key, "une valeur par défaut")

---

## Utiliser des ```list comprehensions``` pour des boucles simples de transformation

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    # additionner 5 à tous les chiffres de la liste "a"
    a = range(0, 10)
    b = []

    for index, item in enumerate(a):
        b[index] = item + 5

    a = b

---

## Utiliser des ```list comprehensions``` pour des boucles simples de transformation

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    # additionner 5 à tous les chiffres de la liste "a"
    a = range(0, 10)
    a = [x + 5 for x in a]

---

## Utiliser des ```generator expressions``` au lieu des ```list comprehensions``` pour les listes avec une longueur non connu

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    # 500 millions de users = ouch
    for name in [user.name.upper() for user in users]:
        print name

---

## Utiliser des ```generator expressions``` au lieu des ```list comprehensions``` pour les listes avec une longueur non connu

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    # 500 millions de users = no hay problema senor !
    for name in (user.name.upper() for user in users):
        print name

---

## Utiliser des ```dict comprehensions``` pour créer des dictionnaires à partir d'une liste d'éléments

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    user_email = {}
    for user in users_list:
        if user.email:
            user_email[user.name] = user.email

---

## Utiliser des ```dict comprehensions``` pour créer des dictionnaires à partir d'une liste d'éléments

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    user_email = {user.name: user.email
                  for user in users_list if user.email}

---

## Ouverture/fermeture de fichier

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    f = open("un_fichier.txt", "r")
    print f
    f.close()

---

## Ouverture/fermeture de fichier

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    with open("un_fichier.txt", "r") as f:
        print f
    # close implicite à la sortie du with !

---

## Utiliser la fonction ```join``` pour concaténer des chaînes de caractères à partir d'une ```list```

<h3><i class="fa fa-thumbs-down"></i></h3>

    !python
    loved = ["python", "books", "fruits", "latte"]
    loved_string = ""
    for i in loved:
        loved_string += i + " and "

    print("I love {} !".format(loved_string))
    # I love python and books and fruits and latte and !

---

## Utiliser la fonction ```join``` pour concaténer des chaînes de caractères à partir d'une ```list```

<h3><i class="fa fa-thumbs-up"></i></h3>

    !python
    loved = ["python", "books", "fruits", "latte"]
    print("I love {} !".format(" and ".join(loved)))
    # I love python and books and fruits and latte !


---

# Questions ?

## Commentaires/Bashing ?

---

# Merci !

* Je pars pour montréal et j'apporte: un bouquin pour la route
* Fruit que je mangerai éternellement: Melon d'eau
* bernardchhun.com

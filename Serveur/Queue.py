from DatabaseHandler import DatabaseHandler


dbName = input("Give a database name: ")
db = DatabaseHandler(dbName) #Connexion a la base de donnée

l = db.getIDs(2) #récupération des ID

if len(l) > 0: #Boucle simple pour permettre à l'utilisateur d'accepter ou non d'ajouter une question proposée à la base générale (à la table TB1).

    for i in l:

        print(db.searchQuestion(i, 2))
        a = input("Is this question right ? (0/1) \n")

        if int(a) == 0:

            db.deleteQuestion(i, 2)

        elif int(a) == 1:

            q = db.searchQuestion(i, 2)[0]
            a1 = db.searchQuestion(i, 2)[1]
            a2 = db.searchQuestion(i, 2)[2]

            db.addQuestion(q, a1, a2, 1)
            db.deleteQuestion(i, 2)

        else:

            print("Please, answer with 0 or 1.")

else:

    print("There is not question in table 2.")


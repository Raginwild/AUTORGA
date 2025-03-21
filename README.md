# AUTORGA

Bienvenue, 

Ceci est le dépôt d'un script d'automatisation de la classification des fichiers, 
Ce script marche avec tous les environnements et utilise des bibliothèques python natives

Pour l'utiliser il vous suffit de modifier les deux premiers chemins (fichier source et fichier de destination) et le reste se fera tout seul en lançant le script. 

Par exemple : 
J'ai mon dossier A contenant 10 fichiers avec différentes extensions
> Je lance le script
Les fichiers comme le fichier xx.txt seront déplacés et renommés vers un dossier correspondant à son extension:
> Le fichier xx.txt sera maintenant nommé source_datecre_xx.txt et se retrouvera dans le dossier "Texte"(généré automatiquement) du chemin de destination.

Ce script peut servir : 
A automatiser le tri et l'enregistrement des fichiers téléchargé au quotidien en le paramétrant dans les tâches automatiques de l'OS au lancement. 
Fini les fichiers volants dans des dossiers.    

+ Pour les utilisateurs de Windows : voici comment le rajouter au planificateur de tâche


1. **Ouvrir le Planificateur de tâches :**  
   - Cliquez sur le bouton **Démarrer** et tapez « **Planificateur de tâches** ».  
   - Sélectionnez l'application **Planificateur de tâches** dans les résultats.

2. **Créer une nouvelle tâche :**  
   - Dans le volet de droite, cliquez sur **Créer une tâche**.  
   - Une fenêtre « Créer une tâche » s'ouvre.

3. **Configurer l’onglet Général :**  
   - **Nom de la tâche :** Donnez un nom explicite, par exemple « **Trier fichiers Téléchargements** ».  
   - **Description (facultatif) :** Ajoutez une description pour rappeler la fonction de la tâche.  
   - **Exécuter avec les privilèges élevés :** Cochez cette option si votre script nécessite des droits d’administrateur.
   - **Configurer pour :** Choisissez votre version de Windows dans le menu déroulant.

4. **Définir un déclencheur :**  
   - Passez à l’onglet **Déclencheurs** et cliquez sur **Nouveau…**.  
   - Dans la fenêtre qui s’ouvre, sous « **Commencer la tâche** », sélectionnez **À l’ouverture de session** ou **Au démarrage** selon votre préférence.  
   - Vous pouvez spécifier si le déclenchement s’applique à tous les utilisateurs ou à un utilisateur en particulier.  
   - Cliquez sur **OK** pour valider.

5. **Ajouter une action :**  
   - Rendez-vous dans l’onglet **Actions** et cliquez sur **Nouveau…**.  
   - Dans le champ **Action**, assurez-vous que **Démarrer un programme** est sélectionné.  
   - **Programme/script :** Entrez le chemin vers l’exécutable Python (par exemple, `C:\Python39\python.exe`).  
   - **Ajouter des arguments (facultatif) :** Indiquez le chemin complet vers votre script Python, par exemple :  
     ```
     C:\Users\VotreNomUtilisateur\Documents\Scripts\trier_fichiers.py
     ```
     Vous pouvez également ajouter d'autres arguments si nécessaire.  
   - Cliquez sur **OK**.

6. **Configurer les Conditions et Paramètres (facultatif) :**  
   - **Onglet Conditions :** Vous pouvez définir si la tâche doit s’exécuter uniquement si l’ordinateur est alimenté par le secteur ou si d’autres conditions sont remplies.  
   - **Onglet Paramètres :** Vous pouvez spécifier des options supplémentaires, comme « Arrêter la tâche si elle s’exécute trop longtemps » ou « Autoriser l’exécution à la demande ».  
   - Ces options sont utiles pour peaufiner le comportement de votre tâche.

7. **Valider et enregistrer la tâche :**  
   - Une fois toutes les informations renseignées, cliquez sur **OK** pour enregistrer la tâche.  
   - Si une invite de contrôle de compte d’utilisateur apparaît, confirmez l’opération.

Après avoir configuré votre tâche, le Planificateur de tâches exécutera automatiquement votre script Python au démarrage de votre session Windows. Assurez-vous que le chemin vers Python et votre script est correct et que Python est bien installé sur votre système.

Ce procédé vous permettra d’automatiser le tri de vos fichiers dès l’ouverture de session, sans intervention manuelle.
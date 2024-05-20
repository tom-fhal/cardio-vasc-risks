# Présentation du projet

Ce projet vise à mettre en œuvre une **régression logistique** pour analyser une variable binaire (VRAI/FAUX, 0/1 ou OUI/NON) en fonction d’une variable explicative quantitative. La régression logistique est utilisée pour prédire des variables binaires, et non des variables continues.

Dans le domaine de la médecine préventive, ce projet permet de donner des conseils d’hygiène de vie et de proposer un accompagnement dans le dépistage de maladies, plus spécifiquement, dans la prévention des risques cardio-vasculaires.

La régression logistique est une technique d’analyse statistique qui permet de prédire l’issue d’une variable cible catégorielle à partir d’une ou plusieurs variables prédictives. Elle est idéale pour les situations où la variable à prédire est de type binaire, comme “oui ou non”, “présent ou absent”, ou “succès ou échec”.

## Fonctionnement de la Régression Logistique

La régression logistique s’appuie sur une fonction mathématique particulière, la fonction logistique ou sigmoïde, pour convertir les valeurs prédites par un modèle linéaire en probabilités comprises entre 0 et 1. Cette fonction a la forme caractéristique d’un “S” et est exprimée par la formule suivante :

$$ f(x) = \frac{1}{1 + e^{-x}} $$

<img width="400" alt="Capture d’écran 2024-05-20 à 8 08 36 PM" src="https://github.com/tom-fhal/cardio-vasc-risks/assets/115147247/7c37f4e6-8264-449f-aa42-b403941ae2db">

Ici, \( e \) représente la base des logarithmes naturels, et \( x \) est la somme pondérée des variables prédictives.

### Estimation des Coefficients

Pour estimer les coefficients de la régression logistique, on utilise la méthode du maximum de vraisemblance. Cette approche consiste à trouver les valeurs des coefficients qui rendent la probabilité d’observer les données collectées la plus élevée possible.

### Interprétation des Coefficients

Les coefficients en régression logistique sont souvent interprétés en termes de rapport de cotes (odds ratio).

Par exemple, un coefficient de 0.5 signifie que si la variable prédictive augmente d’une unité, les chances que l’événement se produise augmentent de 50%.

### Application Pratique

Une fois le modèle ajusté, il peut être utilisé pour prédire la probabilité qu’une nouvelle observation appartienne à une certaine catégorie.

Cela est extrêmement utile pour la prise de décision basée sur les données. Dans le domaine de la santé, par exemple, un modèle de régression logistique pourrait servir à prédire la probabilité qu’un patient développe une maladie en fonction de divers facteurs de risque.

En résumé, la régression logistique est un outil puissant pour la modélisation et la prédiction dans des domaines variés, allant de la médecine à la finance, en passant par les sciences sociales. Elle transforme une analyse linéaire en une probabilité, offrant ainsi une interprétation directe et pratique des résultats.

## Exemples Concrets de Régression Logistique

### Prédiction de Maladies

Imaginons un hôpital qui souhaite prédire si un patient est susceptible de développer une maladie cardiaque. Les médecins pourraient utiliser un modèle de régression logistique en prenant en compte des variables telles que l’âge, le sexe, le niveau de cholestérol, et la pression artérielle. Si le modèle prédit une probabilité élevée, cela pourrait indiquer un risque accru de maladie cardiaque.

### Maintenance Prédictive

Dans le secteur industriel, la régression logistique peut aider à prévoir des pannes d’équipement. Par exemple, en analysant l’ancienneté, le modèle de la machine, et les heures de fonctionnement, on peut estimer la probabilité qu’une machine nécessite une maintenance ou soit sur le point de tomber en panne.

### Credit Scoring

Les banques utilisent souvent la régression logistique pour évaluer la solvabilité des clients. En intégrant des données telles que les revenus, l’historique de crédit, et l’emploi, le modèle peut prédire la probabilité qu’un client rembourse un prêt.

## Approfondissement Mathématique

Pour mieux comprendre la fonction sigmoïde, considérons un exemple simple avec une seule variable prédictive \( x \). La fonction sigmoïde peut être visualisée comme suit :

$$ f(x) = \frac{1}{1 + e^{-x}} $$

Si \( x \) représente, par exemple, le niveau de cholestérol d’un patient, et que le modèle a appris que des niveaux élevés de cholestérol sont associés à un risque accru de maladie cardiaque, alors pour un niveau de cholestérol donné, disons \( x = 240 \), la fonction sigmoïde nous donnera la probabilité que ce patient ait une maladie cardiaque.

### Interprétation des Résultats

Lorsque nous obtenons les résultats d’une régression logistique, il est important de savoir les interpréter correctement. Prenons l’exemple des cotes mentionnées précédemment. Si le coefficient pour le niveau de cholestérol est de 0.2, cela signifie que pour chaque augmentation de 1 unité de cholestérol, les cotes de développer une maladie cardiaque augmentent de \( e^{0.2} \approx 1.22 \) fois, soit une augmentation d'environ 22%.

## Construction du modèle

Pour construire le modèle de régression logistique, nous suivrons les étapes suivantes :

1. **Pré-traitement des données** : Analyse des données manquantes, aberrantes et les doublons à l’aide de divers outils. Les données doivent avoir du sens dans un contexte médical.
2. **Visualisation et analyse des données** : Utilisation des librairies Matplotlib, Seaborn ou Plotly pour visualiser et analyser les données.
3. **Construction du modèle avec Scikit-Learn** : Réalisation d’une régression logistique du cas d’étude présenté ci-dessus avec les outils de la librairie Scikit-Learn. Test et modification des différents hyper-paramètres.
4. **Construction du modèle sans librairies existantes** : Réalisation d’une régression logistique du cas d’étude présenté ci-dessus avec votre propre classe python sans utiliser de librairies existantes.
5. **Évaluation des résultats** : Évaluation des résultats avec des mesures de qualité d’un algorithme de classification supervisée.
6. **Utilisation de plusieurs métriques d’évaluation** : Matrice de confusion, l’accuracy, le recall, rapport de classification, etc. Détermination de la métrique la plus adaptée à ce cas d’étude.
7. **Prédiction** : Donner une prédiction pour si Arthur, 53 ans, fumeur, sportif, 175 cm, 85 kg, avec un taux de cholestérol au-dessus de la normale et un taux de glucose normal, une tension artérielle systolique dans la moyenne et une pression sanguine diastolique correspondant à la moyenne du 3e quartile (50%-75%) du jeu de données, est un sujet à risques cardio-vasculaire.

# Conclusion

Ce projet permet de mettre en œuvre une régression logistique pour prédire les risques cardio-vasculaires.

Il permet également de comprendre l’importance de la préparation des données, de la visualisation des données, de la construction du modèle et de l’évaluation des résultats.

Il offre également une opportunité d’apprendre à construire un modèle de régression logistique sans utiliser de librairies existantes. Enfin, il permet de faire une prédiction sur un cas réel.

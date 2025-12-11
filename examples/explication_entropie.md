# Explication détaillée du calcul de l'entropie

## Vue d'ensemble

La fonction `calculerEntropie(motTest, candidats)` mesure **l'incertitude** ou la **quantité d'information** qu'apporte un mot test. Plus l'entropie est élevée, plus le mot est efficace pour réduire l'espace de recherche.

## 🎯 Objectif

Trouver le mot qui divise le mieux l'ensemble des candidats possibles, c'est-à-dire celui qui permet d'éliminer le plus de possibilités, quelle que soit la réponse obtenue.

## 📊 Étapes du calcul

### **1. Partitionnement**

```javascript
let partitions = {};

candidats.forEach(candidat => {
    let pattern = genererPattern(motTest, candidat);
    if (!partitions[pattern]) {
        partitions[pattern] = [];
    }
    partitions[pattern].push(candidat);
});
```

**Ce qui se passe :**
- Pour chaque candidat possible, on calcule quel serait le pattern de réponse si ce candidat était le mot secret
- Les candidats sont regroupés par pattern identique
- Exemple : si `motTest = "SALER"` et qu'on teste contre les mots `SALON`, `SAPIN`, `SACHE`...
  - `SALON` → pattern `"==_?_"` (S bien placé, A bien placé, L absent, O mal placé, N absent)
  - `SAPIN` → pattern `"==___"` 
  - Les mots avec le même pattern sont regroupés ensemble

**Structure des partitions :**
```javascript
partitions = {
    "==_?_": ["SALON", "SABOT"],  // 2 mots
    "==___": ["SAPIN", "SACHE"],  // 2 mots
    "===__": ["SALER"],           // 1 mot
    // etc.
}
```

### **2. Calcul de l'entropie de Shannon**

```javascript
let entropie = 0;
let n = candidats.length;  // Nombre total de candidats

Object.values(partitions).forEach(groupe => {
    let p = groupe.length / n;  // Probabilité de ce pattern
    if (p > 0) {
        entropie -= p * Math.log2(p);
    }
});
```

**Formule mathématique :**

$$H = -\sum_{i=1}^{k} p_i \log_2(p_i)$$

Où :
- $H$ = entropie (en bits)
- $p_i$ = probabilité du pattern $i$ (= nombre de mots dans le groupe / nombre total de candidats)
- $k$ = nombre de patterns différents

**Exemple concret :**

Supposons 8 candidats répartis ainsi :
- Pattern A : 4 mots → $p_A = 4/8 = 0.5$
- Pattern B : 2 mots → $p_B = 2/8 = 0.25$
- Pattern C : 2 mots → $p_C = 2/8 = 0.25$

Calcul :
```
H = -(0.5 × log₂(0.5) + 0.25 × log₂(0.25) + 0.25 × log₂(0.25))
H = -(0.5 × (-1) + 0.25 × (-2) + 0.25 × (-2))
H = -(-0.5 - 0.5 - 0.5)
H = 1.5 bits
```

## 💡 Interprétation

### Entropie élevée (bon mot) ✅

- Les candidats sont répartis uniformément dans beaucoup de partitions
- Exemple : 8 candidats → 8 patterns différents (1 mot par pattern) → $H = 3$ bits
- **Le mot divise efficacement l'espace de recherche**

### Entropie faible (mauvais mot) ❌

- Les candidats sont concentrés dans peu de partitions
- Exemple : 8 candidats → 1 seul pattern (tous ensemble) → $H = 0$ bits
- **Le mot n'apporte presque aucune information**

## 🔄 Utilisation dans le solveur

La fonction `meilleurMot()` teste tous les candidats et choisit celui avec l'**entropie maximale** :

```javascript
function meilleurMot(candidats) {
    if (candidats.length === 1) {
        return candidats[0];
    }

    let meilleur = null;
    let maxEntropie = -1;

    candidats.forEach(mot => {
        let entropie = calculerEntropie(mot, candidats);
        if (entropie > maxEntropie) {
            maxEntropie = entropie;
            meilleur = mot;
        }
    });

    return meilleur;
}
```

## 📚 Fondements théoriques

C'est une stratégie **optimale** basée sur la **théorie de l'information de Claude Shannon**, qui garantit de trouver le mot en un minimum d'essais en moyenne.

### Avantages de cette approche

1. **Optimale en moyenne** : Minimise le nombre d'essais attendu
2. **Basée sur la théorie de l'information** : Solide fondement mathématique
3. **Prédictive** : Anticipe toutes les réponses possibles
4. **Équitable** : Ne favorise aucun pattern particulier

### Complexité algorithmique

- Pour $n$ candidats et $m$ mots à tester
- Complexité : $O(m \times n)$ pour trouver le meilleur mot
- En pratique, $m = n$ (on teste tous les candidats)
- Donc : $O(n^2)$ par itération

## 🎮 Application pratique dans Sutom

1. **Démarrage** : L'algorithme charge tous les mots correspondant aux critères (première lettre + longueur)
2. **Première proposition** : Calcule l'entropie de chaque mot candidat et propose celui avec la plus haute entropie
3. **Après chaque réponse** : 
   - Filtre les candidats selon le pattern obtenu
   - Recalcule l'entropie sur les candidats restants
   - Propose le nouveau meilleur mot
4. **Convergence** : Continue jusqu'à trouver le mot ou n'avoir plus qu'un candidat

## 📊 Exemple de progression

```
Étape 1: 1000 candidats → Entropie max = 8.5 bits → Propose "SALER"
Réponse: "==_?_" → 50 candidats restants

Étape 2: 50 candidats → Entropie max = 4.2 bits → Propose "SAINT"
Réponse: "===__" → 3 candidats restants

Étape 3: 3 candidats → Entropie max = 1.5 bits → Propose "SABOT"
Réponse: "=====" → Mot trouvé !
```

Chaque étape réduit drastiquement l'espace de recherche grâce à la maximisation de l'information obtenue.

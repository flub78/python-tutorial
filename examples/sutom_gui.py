#!/usr/bin/env python3
import sys
import math
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from collections import defaultdict

def charger_dictionnaire(fichier, premiere_lettre, longueur):
    """Charge les mots du dictionnaire correspondant aux critères"""
    mots = []
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            for ligne in f:
                mot = ligne.strip().upper()
                if len(mot) == longueur and mot[0] == premiere_lettre:
                    mots.append(mot)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de charger le dictionnaire: {e}")
    return mots

def generer_pattern(mot_test, mot_solution):
    """Génère le pattern de réponse pour un mot test vs une solution"""
    pattern = ['_'] * len(mot_test)
    lettres_solution = list(mot_solution)
    
    # D'abord les bien placées
    for i in range(len(mot_test)):
        if mot_test[i] == mot_solution[i]:
            pattern[i] = '='
            lettres_solution[i] = None
    
    # Puis les mal placées
    for i in range(len(mot_test)):
        if pattern[i] == '_' and mot_test[i] in lettres_solution:
            pattern[i] = '?'
            lettres_solution[lettres_solution.index(mot_test[i])] = None
    
    return ''.join(pattern)

def calculer_entropie(mot_test, candidats):
    """Calcule l'entropie d'un mot test sur les candidats restants"""
    partitions = defaultdict(list)
    for candidat in candidats:
        pattern = generer_pattern(mot_test, candidat)
        partitions[pattern].append(candidat)
    
    entropie = 0
    n = len(candidats)
    for groupe in partitions.values():
        p = len(groupe) / n
        entropie -= p * math.log2(p) if p > 0 else 0
    return entropie

def meilleur_mot(candidats):
    """Trouve le mot avec la meilleure entropie"""
    if len(candidats) == 1:
        return candidats[0]
    
    meilleur = None
    max_entropie = -1
    
    for mot in candidats:
        entropie = calculer_entropie(mot, candidats)
        if entropie > max_entropie:
            max_entropie = entropie
            meilleur = mot
    
    return meilleur

def filtrer_candidats(candidats, mot_test, reponse):
    """Filtre les candidats selon la réponse reçue"""
    return [c for c in candidats if generer_pattern(mot_test, c) == reponse]


class SutomGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sutom - Aide à la résolution")
        self.root.geometry("800x600")
        
        self.fichier_dict = None
        self.candidats = []
        self.historique = []
        self.essai = 0
        self.mot_actuel = None
        self.reponse_actuelle = []
        self.boutons_lettres = []
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        # Frame de configuration
        config_frame = ttk.LabelFrame(self.root, text="Configuration", padding=10)
        config_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Sélection du fichier
        ttk.Label(config_frame, text="Dictionnaire:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.fichier_label = ttk.Label(config_frame, text="Aucun fichier sélectionné", foreground="gray")
        self.fichier_label.grid(row=0, column=1, sticky=tk.W, padx=5)
        ttk.Button(config_frame, text="Parcourir...", command=self.choisir_fichier).grid(row=0, column=2, padx=5)
        
        # Première lettre
        ttk.Label(config_frame, text="Première lettre:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.premiere_lettre_var = tk.StringVar()
        ttk.Entry(config_frame, textvariable=self.premiere_lettre_var, width=5).grid(row=1, column=1, sticky=tk.W, padx=5)
        
        # Nombre de lettres
        ttk.Label(config_frame, text="Nombre de lettres:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.longueur_var = tk.StringVar(value="6")
        ttk.Entry(config_frame, textvariable=self.longueur_var, width=5).grid(row=2, column=1, sticky=tk.W, padx=5)
        
        # Bouton démarrer
        ttk.Button(config_frame, text="Démarrer", command=self.demarrer).grid(row=3, column=0, columnspan=3, pady=10)
        
        # Frame de proposition actuelle
        self.prop_frame = ttk.LabelFrame(self.root, text="Proposition actuelle", padding=10)
        self.prop_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.info_label = ttk.Label(self.prop_frame, text="Configurez le jeu et cliquez sur Démarrer", font=("Arial", 10))
        self.info_label.pack(pady=5)
        
        # Frame pour les lettres avec menu contextuel
        self.lettres_frame = ttk.Frame(self.prop_frame)
        self.lettres_frame.pack(pady=10)
        
        # Bouton valider
        self.valider_btn = ttk.Button(self.prop_frame, text="Valider et continuer", command=self.valider_reponse, state=tk.DISABLED)
        self.valider_btn.pack(pady=5)
        
        # Légende des couleurs
        legende_frame = ttk.LabelFrame(self.root, text="Légende", padding=10)
        legende_frame.pack(fill=tk.X, padx=10, pady=5)
        
        legende_container = ttk.Frame(legende_frame)
        legende_container.pack()
        
        # Bien placée (rouge)
        bien_placee = tk.Frame(legende_container, bg='#D32F2F', width=30, height=30, relief=tk.RAISED, bd=2)
        bien_placee.pack(side=tk.LEFT, padx=5)
        tk.Label(legende_container, text="Bien placée (=)", font=("Arial", 10)).pack(side=tk.LEFT, padx=(0, 15))
        
        # Mal placée (jaune)
        mal_placee = tk.Frame(legende_container, bg='#C9B458', width=30, height=30, relief=tk.RAISED, bd=2)
        mal_placee.pack(side=tk.LEFT, padx=5)
        tk.Label(legende_container, text="Mal placée (?)", font=("Arial", 10)).pack(side=tk.LEFT, padx=(0, 15))
        
        # Absente (gris)
        absente = tk.Frame(legende_container, bg='#787C7E', width=30, height=30, relief=tk.RAISED, bd=2)
        absente.pack(side=tk.LEFT, padx=5)
        tk.Label(legende_container, text="Absente (_)", font=("Arial", 10)).pack(side=tk.LEFT, padx=(0, 15))
        
        # Indication d'interaction
        tk.Label(legende_container, text="→ Clic gauche: changer l'état | Clic droit: menu", 
                font=("Arial", 9, "italic"), foreground="gray").pack(side=tk.LEFT, padx=(20, 0))
        
        # Frame de l'historique
        historique_frame = ttk.LabelFrame(self.root, text="Historique des propositions", padding=10)
        historique_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Tableau de l'historique
        columns = ("Essai", "Mot", "Réponse", "Candidats restants")
        self.tree = ttk.Treeview(historique_frame, columns=columns, show="headings", height=10)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(historique_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def choisir_fichier(self):
        """Ouvre un dialogue pour choisir le fichier dictionnaire"""
        fichier = filedialog.askopenfilename(
            title="Sélectionner le fichier dictionnaire",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        if fichier:
            self.fichier_dict = fichier
            self.fichier_label.config(text=fichier, foreground="black")
    
    def demarrer(self):
        """Démarre une nouvelle partie"""
        if not self.fichier_dict:
            messagebox.showerror("Erreur", "Veuillez sélectionner un fichier dictionnaire")
            return
        
        premiere_lettre = self.premiere_lettre_var.get().strip().upper()
        if not premiere_lettre or len(premiere_lettre) != 1:
            messagebox.showerror("Erreur", "Veuillez entrer une seule lettre")
            return
        
        try:
            longueur = int(self.longueur_var.get())
            if longueur < 3 or longueur > 15:
                raise ValueError()
        except:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre de lettres valide (3-15)")
            return
        
        # Charger les candidats
        self.candidats = charger_dictionnaire(self.fichier_dict, premiere_lettre, longueur)
        
        if not self.candidats:
            messagebox.showerror("Erreur", "Aucun mot trouvé avec ces critères")
            return
        
        # Réinitialiser
        self.historique = []
        self.essai = 0
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        messagebox.showinfo("Prêt", f"{len(self.candidats)} mots possibles trouvés")
        self.proposer_mot()
    
    def proposer_mot(self):
        """Propose un nouveau mot"""
        if not self.candidats:
            messagebox.showinfo("Terminé", "Aucun mot ne correspond aux réponses données")
            return
        
        self.essai += 1
        self.mot_actuel = meilleur_mot(self.candidats)
        
        self.info_label.config(text=f"Essai {self.essai} - {len(self.candidats)} candidat(s) restant(s)")
        
        # Afficher le mot avec boutons cliquables
        for widget in self.lettres_frame.winfo_children():
            widget.destroy()
        
        self.boutons_lettres = []
        self.reponse_actuelle = ['_'] * len(self.mot_actuel)
        
        for i, lettre in enumerate(self.mot_actuel):
            btn = tk.Button(
                self.lettres_frame, 
                text=lettre, 
                font=("Arial", 24, "bold"),
                width=3,
                height=1,
                bg="lightgray",
                relief=tk.RAISED,
                bd=3
            )
            btn.grid(row=0, column=i, padx=3)
            btn.bind("<Button-3>", lambda e, idx=i: self.afficher_menu(e, idx))
            btn.bind("<Button-1>", lambda e, idx=i: self.cycle_state(idx))
            self.boutons_lettres.append(btn)
        
        self.valider_btn.config(state=tk.NORMAL)
    
    def afficher_menu(self, event, index):
        """Affiche le menu contextuel pour une lettre"""
        menu = tk.Menu(self.root, tearoff=0)
        menu.add_command(label="✓ Bien placée (=)", command=lambda: self.set_etat(index, '='))
        menu.add_command(label="? Mal placée (?)", command=lambda: self.set_etat(index, '?'))
        menu.add_command(label="✗ Absente (_)", command=lambda: self.set_etat(index, '_'))
        menu.post(event.x_root, event.y_root)
    
    def cycle_state(self, index):
        """Change l'état de la lettre par cycle (_->?->=->_)"""
        etats = ['_', '?', '=']
        etat_actuel = self.reponse_actuelle[index]
        nouvel_etat = etats[(etats.index(etat_actuel) + 1) % 3]
        self.set_etat(index, nouvel_etat)
    
    def set_etat(self, index, etat):
        """Définit l'état d'une lettre"""
        self.reponse_actuelle[index] = etat
        
        # Mettre à jour l'affichage
        couleurs = {
            '=': '#D32F2F',  # Rouge (bien placée)
            '?': '#C9B458',  # Jaune (mal placée)
            '_': '#787C7E'   # Gris (absente)
        }
        
        self.boutons_lettres[index].config(
            bg=couleurs[etat],
            fg="white",
            activebackground=couleurs[etat]
        )
    
    def valider_reponse(self):
        """Valide la réponse et continue"""
        reponse = ''.join(self.reponse_actuelle)
        
        # Ajouter à l'historique
        self.tree.insert("", tk.END, values=(
            self.essai,
            self.mot_actuel,
            reponse.replace('=', '✓').replace('?', '?').replace('_', '✗'),
            len(self.candidats)
        ))
        
        # Vérifier si gagné
        if reponse == '=' * len(self.mot_actuel):
            messagebox.showinfo("Gagné!", f"🎉 Mot trouvé en {self.essai} essai(s): {self.mot_actuel}")
            self.valider_btn.config(state=tk.DISABLED)
            return
        
        # Filtrer les candidats
        self.candidats = filtrer_candidats(self.candidats, self.mot_actuel, reponse)
        
        if not self.candidats:
            messagebox.showwarning("Aucun candidat", "Aucun mot ne correspond. Vérifiez vos réponses.")
            self.valider_btn.config(state=tk.DISABLED)
            return
        
        # Proposer le mot suivant
        self.proposer_mot()


def main():
    root = tk.Tk()
    app = SutomGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()

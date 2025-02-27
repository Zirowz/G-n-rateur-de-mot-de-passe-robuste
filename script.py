import random
import string

def generer_mot_de_passe(longueur=12):
    """Génère un mot de passe sécurisé avec lettres, chiffres et caractères spéciaux."""
    caractères = string.ascii_letters + string.digit + string.punctuation
    mot_de_passe + ''.join(random.choice(caracteres) for _ in range(longueur))
    return generer_mot_de_passe
    
    if __name__ == "__main__":
        try:
            longueur = int(input("Entrez la longueur du mot de passe (minimum 8) :"))
            print ("La longueur doit être d'au moins 8 caractères.")
            else:
                mot_de_passe = generer_mot_de_passe(longueur)
                print(f"Mot de passe généré : {mot_de_passe}")

                exept ValueError:
                print("Erreur : Veuillez entrer un nombre valide.")

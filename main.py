# Importation des modules pour le scan
import subprocess
import ipaddress
import platform

# Fonction pour tester la disponibilite de l'adresse IP du reseau
def ping_subprocess(reseau):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    
# Parcours des adresses IP disponible dans le reseau
    for ip in reseau.hosts():
        commande = ['ping', param, '4', str(ip)]
        resultat = subprocess.run(commande)
        print(resultat)

# Fonction principale du programme
def main():
    while True:
        
        # Saisie de l'adresse IP et scan de l'adresse IP
        reseau_scan = input("Veuillez entrer le réseau à scanner : ")

        try:
            reseau = ipaddress.ip_network(reseau_scan, strict=False)
            print("L'adresse est valide")

            for ip in reseau.hosts():
                print(f"Scan de l'adresse IP : {ip}")
                break

            for ip in reseau.hosts():
                print(ip)
                
# Appel de la fonction 
            ping_subprocess(reseau)

            break

        except ValueError:
            print("L'adresse n'est pas valide")


if __name__ == "__main__":
    main()

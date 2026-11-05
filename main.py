import subprocess
import ipaddress
import platform


def ping_subprocess(reseau):
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    for ip in reseau.hosts():
        commande = ['ping', param, '1', str(ip)]
        resultat = subprocess.run(commande)
        print(resultat)


def main():

    while True:
        reseau_scan = input("Veuillez entrer le réseau à scanner : ")

        try:
            reseau = ipaddress.ip_network(reseau_scan, strict=False)
            print("L'adresse est valide")

            for ip in reseau.hosts():
                print(f"Scan de l'adresse IP : {ip}")
                break

            for ip in reseau.hosts():
                print(ip)

            ping_subprocess(reseau)

            break

        except ValueError:
            print("L'adresse n'est pas valide")


if __name__ == "__main__":
    main()
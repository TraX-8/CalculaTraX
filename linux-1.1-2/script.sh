#!/bin/bash
if [ "$EUID" -ne 0 ]; then
	echo "Ce script doit être exécuté en tant qu'administrateur. Ajoutez 'sudo' avant la commande d'exécution."
	zenity --error --title "Erreur d'installation" --text "Vous devez exécuter ce script en tant qu'administrateur."
	exit 1
fi
echo "Script lancé en tant qu'Administrateur. Installation en cours..."
install() {
	(
	echo "10" ; mkdir -p /usr/lib/trax-software
	echo "# Création des dossiers d'installation (1)"; sleep 1
	echo "20"; mkdir -p /usr/lib/trax-software/calculatrax/
	echo "# Création des dossiers d'installation (2)"; sleep 1
	echo "60"; cp -r . /usr/lib/trax-software/calculatrax
	echo "# Installation des fichiers"; chmod -R 755 /usr/lib/trax-software && sleep 2
	echo "75"; cp CalculaTraX.desktop /usr/share/applications
	echo "# Installation des raccourcis"; chmod 755 /usr/share/applications/CalculaTraX.desktop && sleep 1
	echo "85"; chmod +x calculatrax
	echo "# Installation des raccourcis"; sleep 0.5
	echo "95"; cp calculatrax /usr/bin
	echo "# Installation des raccourcis"; chmod 755 /usr/bin/calculatrax && sleep 1
	echo "98"; update-desktop-database --quiet /usr/share/applications/
	echo "# Finalisation de l'installation et rechargement de la base de données"; sleep 1
	echo "100"; echo "Installation finalisée"
	echo "# Installation terminée."; sleep 3
	) |
	zenity --progress \
		--title="Installation de l'application" \
		--text="Initialisation de l'installeur..." \
		--percentage=0
	if [ "$?" = -1 ] ; then
        zenity --error \
          --text="Installation annulée."
	fi
}
if zenity --question --text="Voulez-vous continuer ?"
then
	install
	rm /usr/lib/trax-software/calculatrax/script.sh
else
	zenity --warning --title "Annulation" --text "Installation annulée."
fi

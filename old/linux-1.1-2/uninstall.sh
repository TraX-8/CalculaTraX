#!/bin/bash
if [ "$EUID" -ne 0 ]; then
	echo "Ce script doit être exécuté en tant qu'administrateur. Ajoutez 'sudo' avant la commande d'exécution."
	zenity --error --title "Erreur de désinstallation" --text "Vous devez exécuter ce script en tant qu'administrateur."
	exit 1
fi
echo "Script lancé en tant qu'Administrateur. Désinstallation en cours..."
install() {
	(
	echo "20"; rm -rf /usr/lib/trax-software/calculatrax/
	echo "# Suppression des dossiers d'installation"; sleep 1
	echo "75"; rm /usr/share/applications/CalculaTraX.desktop
	echo "# Désinstallation des raccourcis"; sleep 1
	echo "95"; rm /usr/bin/calculatrax
	echo "# Suppression des raccourcis"; sleep 1
	echo "98"; update-desktop-database --quiet /usr/share/applications/
	echo "# Finalisation de la désinstallation et rechargement de la base de données"; sleep 1
	echo "100"; echo "Désinstallation finalisée"
	echo "# Désinstallation terminée."; sleep 3
	) |
	zenity --progress \
		--title="Désinstallation de l'application" \
		--text="Initialisation du désinstalleur..." \
		--percentage=0
	if [ "$?" = -1 ] ; then
        zenity --error \
          --text="Désinstallation annulée."
	fi
}
if zenity --question --text="Voulez-vous continuer ?"
then
	install
else
	zenity --warning --title "Annulation" --text "Désinstallation annulée."
fi

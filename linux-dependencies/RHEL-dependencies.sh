#!/bin/bash
if [ "$EUID" -ne 0 ]; then
	echo "Ce script doit être exécuté en tant qu'administrateur. Ajoutez 'sudo' avant la commande d'exécution."
	exit 1
fi
echo "Script lancé en tant qu'Administrateur. Installation des paquets nécessaires pour distribution RHEL (Fedora, etc)"
sudo dnf install zenity python3-tkinter -y

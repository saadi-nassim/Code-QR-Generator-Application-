# Code-QR-Generator-Application- Sous Linux - Python 3.12.3


Application QR Code Wi-Fi

Un petit projet réalisé à la fac que j’ai un peu pimpé pour le rendre plus pratique et stylé.

Fonctionnalités

- Génération d'un QR Code Wi-Fi à partir du nom du réseau et du mot de passe wifi.
- Choix personnalisé des couleurs de fond et de texte du QR Code à partir d'une palette de couleurs pop-up.
- Affichage du nom du réseau et du mot de passe comme texte cliquable pour faciliter la copie dans le presse-papiers.
- Sauvegarde automatique du QR Code dans un fichier PNG.

Prérequis
Avant de commencer, vous devez avoir installé Python sur votre machine ainsi que les dépendances nécessaires.

### Dépendances Python

Les bibliothèques suivantes sont requises pour faire fonctionner l'application :

- Tkinter (pour l'interface graphique)
- Pillow (pour la manipulation des images et des polices)
- qrcode (pour générer les QR Codes)

### Installation des dépendances

1. Créez un environnement virtuel Python (optionnel mais recommandé) :
   ```bash
   python3 -m venv my_env
   ```

2. Activez l'environnement virtuel :
   ```
   source my_env/bin/activate
   ```
3. Faites un upgrade de pip :
   ```
   python3 -m pip install --upgrade pip
   ```
4. Installez les dépendances nécessaires :
   ```bash
   pip install tkinter pillow qrcode
   ```

### Lancer l'application

1. Téléchargez le fichier Python `QR_CODE_APPLICATION.py`.
2. Lancez-le depuis le terminal avec la commande suivante :
   ```bash
   python3 QR_CODE_APPLICATION.py
   ```

L'application graphique s'ouvrira alors. Vous pourrez entrer les informations suivantes :

- **Nom du Wi-Fi** : Le nom de votre réseau.
- **Mot de passe Wi-Fi** : Le mot de passe wifi. 
- **Couleur du texte** : Choix de la couleur du texte du QR Code.
- **Couleur de fond** : Choix de la couleur de fond du QR Code.

Une fois ces informations saisies, cliquez sur le bouton **"Générer le QR Code"**. L'application générera et affichera un QR Code que vous pouvez enregistrer en cliquant dessus. Vous pourrez également copier le SSID et le mot de passe en cliquant dessus.

### Générer un exécutable

Pour créer un exécutable autonome (sans besoin d'installer Python), vous pouvez utiliser **PyInstaller**. Voici les étapes :

1. Installez PyInstaller dans votre environnement virtuel :
   ```bash
   pip install pyinstaller
   ```

2. Générez l'exécutable :
   ```bash
   pyinstaller --onefile --windowed QR_CODE_APPLICATION.py
   ```

3. Après l'exécution de PyInstaller, vous trouverez l'exécutable dans le dossier `dist`. Vous pouvez désormais distribuer cet exécutable sans avoir besoin de Python.

Generer le fichier reuirements 

```
pip freeze > requirements.txt
```
Dossier de sortie

- Le fichier généré sera un exécutable appelé `QR_CODE_APPLICATION.exe` (sur Windows), ou un fichier exécutable sur macOS/Linux sans extension `.exe`.
- Le QR Code généré sera enregistré sous le nom `wifi_qr_<wifi_name>.png`.

Capture d'écran
Voici une capture d'écran de l'application pour mieux comprendre à quoi elle ressemble :

![Capture d’écran du 2025-04-11 12-03-12](https://github.com/user-attachments/assets/67e99975-191f-4ef3-a3eb-0e7d58787962)


Le résultst : 

![wifi_qr_XXX_SFR_5GHZ](https://github.com/user-attachments/assets/c0d6a8cd-72be-4c9e-8f60-a5bd61b8f789)


Auteur
Développé par Nassim SAADI (Projet personnel)

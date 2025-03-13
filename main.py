import os
import shutil
from datetime import datetime
import urllib.parse

# Chemins à adapter selon votre environnement
source_folder = r"C:\Users\Athle\Downloads\test1"
destination_folder = r"C:\Users\Athle\Documents\FichiersTriesTwo"

print("Existe :", os.path.exists(source_folder))
files = os.listdir(source_folder)
print("Nombre de fichiers trouvés :", len(files))

# (Optionnel) Dictionnaire pour trier par type de fichier
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Texte": [".doc", ".docx", ".txt", ".odt"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"],
    "PowerBI" : [".pbix"],
    "Excel" : [".xlsx","xls"],
    "PDF" : [".pdf"],
    "Presentations":[".ppt", ".pptx"],
    "Scripts" : [".py"],
    "Executables" : [".exe"]
}

def creer_dossier(chemin):
    """Crée le dossier s'il n'existe pas déjà."""
    if not os.path.exists(chemin):
        os.makedirs(chemin)

def get_creation_date(filepath):
    """
    Récupère la date de création du fichier et la formate en AAAAMMJJ_HHMMSS.
    Sur Windows, os.path.getctime renvoie bien la date de création.
    """
    t = os.path.getctime(filepath)
    return datetime.fromtimestamp(t).strftime("%Y%m%d_%H%M%S")

def get_file_source(filepath):
    """
    Tente de récupérer la source de téléchargement en lisant l'ADS Zone.Identifier.
    Si trouvé, extrait le domaine du HostUrl (exemple : google.com).
    Sinon, retourne "Inconnu".
    """
    try:
        ads_path = filepath + ":Zone.Identifier"
        with open(ads_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        for line in content.splitlines():
            if line.startswith("HostUrl="):
                url = line.split("=", 1)[1].strip()
                # Extraire le domaine de l'URL
                parsed = urllib.parse.urlparse(url)
                domain = parsed.netloc
                return domain if domain else "Inconnu"
        return "Inconnu"
    except Exception:
        return "Inconnu"

def generate_new_filename(filepath):
    """
    Génère un nouveau nom de fichier incluant la source de téléchargement et la date de création.
    Exemple : google_20250307_101530.jpg
    """
    _, ext = os.path.splitext(os.path.basename(filepath))
    date_str = get_creation_date(filepath)
    source = get_file_source(filepath)
    filename =  os.path.basename(filepath) #plus flexible qu utiliser split
    return f"{source}_{date_str}{ext}_{filename}"

def trier_fichiers():
    """
    Parcourt le dossier source, renomme chaque fichier en y intégrant sa source et sa date de création,
    puis le déplace vers le dossier de destination. En cas de doublon, un compteur est ajouté.
    """
    for filename in os.listdir(source_folder):
        chemin_source = os.path.join(source_folder, filename)
        
        # Ignorer les dossiers
        if os.path.isdir(chemin_source):
            continue

        match=0

        # Creation du chemin vers le dossier cible en fonction du type de fichier
        file_ext = os.path.splitext(filename)[-1].lower()
        for _key,_ext in file_types.items():
            if file_ext in _ext:
                filedestfold=os.path.join(destination_folder,_key)
                match=1
                break

        if not match :
                filedestfold=os.path.join(destination_folder,'Autres')
        
        creer_dossier(filedestfold)
        
        new_filename = generate_new_filename(chemin_source)
        destination_path = os.path.join(filedestfold, new_filename)
        
        # Gestion des doublons : ajouter un compteur si le nom existe déjà
        counter = 1
        base, ext = os.path.splitext(new_filename)
        while os.path.exists(destination_path):
            new_filename = f"{base}_{counter}{ext}"
            destination_path = os.path.join(filedestfold, new_filename)
            counter += 1
        
        try:
            shutil.move(chemin_source, destination_path)
            print(f"Déplacé {filename} vers {destination_path}")
        except Exception as e:
            print(f"Erreur lors du déplacement de {filename} : {e}")

if __name__ == "__main__":
    trier_fichiers()

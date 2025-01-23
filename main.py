# Importation des bibliothèques nécessaires
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


print("Démarrage du script...")
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Temp\\chrome-data")
options.add_argument("--log-level=3")


# Demander à l'utilisateur s'il veut activer le mode headless
headless_choice = input("Voulez-vous activer le mode headless ? (oui/non) : ").strip().lower()
if headless_choice in ['oui', 'yes', 'y']:
    # Mode headless (n'affiche pas la fenêtre du navigateur)
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")  
    options.add_argument("--disable-dev-shm-usage")
    print("Mode headless activé.")
else:
    print("Mode headless désactivé. Une fenêtre de navigateur s'ouvrira.")

spam = input("Que voulez vous spam ?\n\n")
print(f"Ok, '{spam}' sera envoyer en boucle hahahaha")

# Initialisation du driver Selenium
driver = webdriver.Chrome(options=options)

# Accéder à WhatsApp Web
driver.get("https://web.whatsapp.com")

# Dézoomer la page (Ctrl + -) environ 6 fois pour une vue réduite à ~25%
actions = ActionChains(driver)
for _ in range(6):
    actions.key_down(Keys.CONTROL).send_keys('-').key_up(Keys.CONTROL).perform()

print()
print("Veuillez scanner le QR code pour vous connecter à WhatsApp Web...")
input("Une fois ceci fait, appuyez sur 'Entrée'")
time.sleep(2)


try:
    # Demander à l'utilisateur de saisir le nom du contact
    contact = input("\nEntrez le nom de votre contact\n\n")
    # Attendre qu'une conversation non lue apparaisse
    unread_chat = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, f"//span[@title='{contact}']"))
    )
    unread_chat.click()
    print(f"Chat avec '{contact}' cliqué avec succès.")


except Exception as e:
    prblm = input("Un problème est survenu, voulez-vous avoir la raison ? (oui/non)\n\n").strip().lower()
    if prblm in ["oui", "y", "yes"]:
        print(e)
    else:
        print("Problème ignoré.")
    


time.sleep(2.5)


# Envoi de la réponse sur WhatsApp
message_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))

)

message_box.click()
start_time = time.time()  # Enregistrer l'heure de début

spam_number = 0


while True:
    actions.send_keys(f"{spam}{Keys.ENTER}").perform()
    spam_number += 1

    if spam_number % 50 == 0:

        elapsed_time = time.time() - start_time
        elapsed_minutes, elapsed_seconds = divmod(int(elapsed_time), 60)  # Convertir en minutes et secondes
        
        print(f"\n{spam_number} spams envoyés en {elapsed_minutes}m et {elapsed_seconds}s!\n")

        actions.send_keys(f"{spam_number} spams envoyés en {elapsed_minutes}m et {elapsed_seconds}s!{Keys.ENTER}").perform()
        start_time = time.time()  # Enregistrer l'heure de début

    
    time.sleep(random.uniform(0.1, 0.8))  # Pause aléatoire entre 100ms et 800ms

    


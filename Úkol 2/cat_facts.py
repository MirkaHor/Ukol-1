import requests
import json

# Funkce pro získání 10 náhodných faktů o kočkách
def get_cat_facts():
    try:
        # Získání faktů s krátkým timeoutem
        response = requests.get("https://cat-fact.herokuapp.com/facts", timeout=0.001)
        response.raise_for_status()  # Zkontrolovat, zda byl request úspěšný
    except requests.exceptions.Timeout:
        print("Jsme příliš nedočkaví.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"Došlo k chybě při komunikaci s API: {e}")
        return []
    
    facts_data = response.json()
    facts = [fact["text"] for fact in facts_data[:10]]  # Extrahovat prvních 10 faktů
    return facts

# Funkce pro uložení faktů do souboru JSON
def save_facts_to_json(facts, filename):
    numbered_facts = [f"{i+1}. {fact}" for i, fact in enumerate(facts)]
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(numbered_facts, file, ensure_ascii=False, indent=4)

# Hlavní část programu
if __name__ == "__main__":
    facts = get_cat_facts()
    if facts:
        save_facts_to_json(facts, "kocici_fakta.json")
        print("Fakta byla úspěšně uložena do souboru kocici_fakta.json.")
    else:
        print("Nepodařilo se získat žádná fakta o kočkách.")

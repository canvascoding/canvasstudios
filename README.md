# Canvas Studios 👟✨

**Color Your Story. Handgemalte Premium-Sneaker aus Deutschland.**

Canvas Studios macht aus weißen Ledersneakern Kunstwerke. Jeder Schuh wird von Hand bemalt – kein Sneaker gleicht dem anderen. Wir starten mit einer limitierten ersten Kollektion ("The First 100") und bauen die Brand Schritt für Schritt auf: authentisch, hochwertig und mit Liebe zum Detail.

## 🚀 Status: Launch 2025
Wir befinden uns aktuell in der Pre-Launch Phase. 
*   **Batch 1:** 100 Paare, 100 Unikate.
*   **Release:** Q1 2025
*   **Colorways:** Sunset Orange, Crimson Fire, Sage Fresh, Terra Earth, Navy Night.

## 🎨 Brand Identity
*   **Handmade Craftsmanship:** Jeder Sneaker wird von uns selbst in Deutschland handbemalt.
*   **Premium Quality:** Hochwertiges Leder trifft auf professionelle Veredelung.
*   **Individual Expression:** 100 Paare. 100 Unikate. Dein Sneaker, deine Story.

## 📱 Connect with us
Bleibe auf dem Laufenden über unsere Reise und verpasse nicht den ersten Drop:

*   **Instagram:** [@canvasstudios.store](https://instagram.com/canvasstudios.store) (Brand)
*   **TikTok:** [@canvasstudios.store](https://tiktok.com/@canvasstudios.store) (Brand)
*   **Webseite:** [canvasstudios.store](https://canvasstudios.store)

---

## 🛠 Entwicklung
Dieses Repository enthält die aktuelle Teaser-Webseite sowie die Newsletter-Infrastruktur für Canvas Studios.

### Technologie-Stack
*   **Frontend:** Vanilla HTML5, CSS3, JavaScript
*   **Hosting:** GitHub Pages
*   **Newsletter-Backend:** n8n Webhook-Integration
*   **E-Mail-Marketing:** Sendy-optimierte Templates

### Projektstruktur
```
canvasstudios_website/
├── index.html              # Hauptseite mit Hero, Newsletter & Gallery
├── subscribed.html         # Erfolgsseite nach Newsletter-Bestätigung
├── confirm-email.html      # Infoseite für Double Opt-In
├── already-subscribed.html # Seite für bereits registrierte Nutzer
├── unsubscribed.html       # Bestätigung der Abmeldung
├── reconsent-success.html  # GDPR Re-consent Bestätigung
├── impressum.html          # Impressum/Rechtliches
├── style.css               # Custom CSS (Responsive, Animations, Blobs)
├── assets/                 # Optimierte Assets (JPG/PNG) & Logos
├── newsletter_templates/   # Sendy-optimierte HTML E-Mail Templates
└── CNAME                   # Custom Domain (canvasstudios.store)
```

### Key Features
*   **Seamless UX:** Newsletter-Anmeldung via AJAX mit integrierter Double Opt-In Anleitung im Popup.
*   **Performance:** Alle Lifestyle-Bilder sind für das Web optimiert (JPG conversion & resizing).
*   **Sendy Integration:** Professionelle E-Mail-Templates mit dynamischen Tags ([Email], [unsubscribe], [current_year]).
*   **Dynamic Content:** Automatisierte Copyright-Jahreszahlen auf allen Seiten.
*   **Responsive Design:** Mobile-first Grid-Gallery und flüssige Animationen.

### Lokale Vorschau
Einfach die `index.html` in einem beliebigen Browser öffnen.

---
&copy; 2025-heute Canvas Studios. Alle Rechte vorbehalten.
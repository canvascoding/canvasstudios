# Canvas Studios Website Context

## Project Overview
**Canvas Studios** is a premium sneaker brand specializing in hand-painted, unique leather sneakers ("The First 100"). This project contains the static website for their pre-launch phase, primarily focused on brand presentation and newsletter lead generation.

*   **Type:** Static Website (HTML/CSS/JS)
*   **Hosting:** GitHub Pages
*   **Domain:** `canvasstudios.store` (configured via `CNAME`)

## Technology Stack
*   **Frontend:** Vanilla HTML5, CSS3, JavaScript (ES6+).
*   **Styling:** Custom CSS with CSS Variables, Flexbox/Grid, and media queries for responsiveness. No external CSS frameworks (like Bootstrap/Tailwind) are used.
*   **Fonts:** DM Sans (Headings), Inter (Body), Amatic SC (Accents/Handwritten). Hosted via Google Fonts.
*   **Icons:** Inline SVGs.
*   **Backend Integration:** The newsletter form submits data via AJAX (`fetch`) to an **n8n webhook** (`https://n8n.canvas.holdings/webhook/...`).
*   **Email Marketing:** Sendy is used for email campaigns; templates are stored in `newsletter_templates/`.

## Directory Structure
*   `index.html`: The main landing page. Contains the Hero section, Newsletter form, Values, Gallery, and Footer.
*   `style.css`: The primary stylesheet. Handles layout, typography, animations (blobs, fade-ins), and responsive overrides.
*   `assets/`: Contains all static media.
    *   `logos/`: Brand logos (PNGs).
    *   `*.jpg/*.png`: Optimized lifestyle and product images.
*   `newsletter_templates/`: HTML templates for transactional and campaign emails (Sendy-compatible).
*   `*.html`: Auxiliary pages for the subscription lifecycle:
    *   `confirm-email.html`: Double Opt-In instruction page.
    *   `subscribed.html`: Success page after confirmation.
    *   `already-subscribed.html`: Message for existing subscribers.
    *   `unsubscribed.html`: Unsubscribe confirmation.
    *   `reconsent-success.html`: GDPR re-consent success.
    *   `impressum.html`: Legal notice (Imprint).

## Key Features & Implementation Details
1.  **Newsletter Subscription:**
    *   **Form:** Located in the Hero section (`#newsletterForm`).
    *   **Logic:** Javascript intercept `submit` event -> Client-side validation -> `fetch` POST to n8n webhook.
    *   **UX:** Shows a loading state -> Displays a custom Popup modal (success or error) without reloading the page.
    *   **GDPR:** Includes a mandatory marketing consent checkbox.

2.  **Visual Effects:**
    *   **Blobs:** CSS-animated background blobs (`.blob-1`, `.blob-2`) defined in `style.css`.
    *   **Scroll Reveal:** `IntersectionObserver` in `index.html` triggers `.visible` class on `.scroll-reveal` elements.
    *   **Animations:** CSS `@keyframes` for fade-ins and pulse effects.

3.  **Responsive Design:**
    *   **Mobile-First:** Default styles target mobile devices.
    *   **Desktop:** `@media (min-width: 901px)` handles layout shifts (e.g., Grid Gallery columns, Hero layout).

## Development Workflow
Since this is a static site, no build process is required.

1.  **Edit:** Modify `index.html` or `style.css` directly.
2.  **Preview:** Open `index.html` in any web browser.
3.  **Deploy:** Push changes to the `main` branch. GitHub Pages automatically serves the content.

## Common Tasks
*   **Update Content:** Edit text directly in `index.html`.
*   **Change Styles:** Modify variables in `:root` of `style.css` for global color/font changes.
*   **Newsletter Logic:** Modify the `<script>` block at the bottom of `index.html` to change webhook URLs or popup behavior.

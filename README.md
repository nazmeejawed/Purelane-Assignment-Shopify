# Purelane — Shopify OS 2.0 Theme Implementation

> **Troopod Developer Assessment Submission**  
> **Live Store Preview:** [https://purelane-f06sviua.myshopify.com](https://purelane-f06sviua.myshopify.com)  
> **GitHub Repository:** [https://github.com/nazmeejawed/Purelane-Assignment-Shopify](https://github.com/nazmeejawed/Purelane-Assignment-Shopify)  
> **Theme ID:** `188977152311`

---

## 🌟 Overview

This repository contains the complete **Shopify Online Store 2.0 Theme** built for **Purelane**, converted from a high-fidelity animated single-page prototype (`purelane-homepage.html`).

The implementation translates static design mockups into modular, merchant-editable Shopify Liquid sections while maintaining 100% visual fidelity, 60 FPS hardware-accelerated animations, and responsive layouts across all devices.

---

## ✨ Key Features & Interactive Cinematics

### 🌊 1. Mint Water Background (`purelane-scenes.liquid`)
* Fixed multi-layered background featuring animated SVG caustics (`feTurbulence`, `feDisplacementMap`), sunlit light shafts, rising bubbles, and subtle ambient vignettes.
* Smooth depth transitions matching section attributes (`data-scene`).

### 📦 2. Interactive Hero Stage & Bottle Carousel (`purelane-hero.liquid`)
* **Auto-slide Loop:** Automatically flips through product bundle stages every 3.5 seconds.
* **Hover Interactivity:** Pauses auto-rotation on mouse enter so users can read pricing details, with subtle bottle lift animations (`translateY(-6px) scale(1.02)`).
* **Manual Control:** Clickable pagination dots and stage click triggers for instant slide jumps.
* **Smooth CTA Navigation:** Linked "Shop Now" and "How It Works" buttons to smooth-scroll to `#shop` and `#proof`.

### 📍 3. Vertical Progress Rail (`layout/theme.liquid`)
* Floating right-side progress indicator displaying section-by-section dot navigation (`#top` ➔ `#ingredients` ➔ `#how` ➔ `#proof` ➔ `#combos` ➔ `#bundles` ➔ `#shop` ➔ `#signup`).
* Real-time viewport sync utilizing `getBoundingClientRect()` at a 50% viewport trigger.
* Clicking any dot smooth-scrolls directly to that target section.

### ⚡ 4. Fast 60 FPS Scroll Reveals (`.rv`)
* Ultra-fast `0.22s` springy pop-up reveals (`translate3d` + `scale(0.98)` ➔ `scale(1)`).
* Eager 350px `rootMargin` pre-triggering so cards and sections pop up instantly as the user scrolls.

### 🛍️ 5. Floating Glass Navigation (`purelane-header.liquid` & `purelane-ticker.liquid`)
* **Ticker:** Positioned at the top (`position: absolute`) so it naturally scrolls out of view.
* **Floating Header:** Glassmorphic navigation pill (`position: fixed`) that smoothly transitions from `top: 48px` to `top: 12px` when scrolling down (`scrollY > 40`).

---

## 📂 Theme Directory Structure

```text
.
├── assets/                  # CSS stylesheets, JS scripts, and SVG icon snippets
├── config/                  # Theme settings & scheme configuration
├── layout/
│   └── theme.liquid         # Main layout containing progress rail, scroll observer & global scripts
├── sections/                # Modular Liquid sections with custom merchant schemas:
│   ├── purelane-scenes.liquid       # Fixed mint water background & caustics
│   ├── purelane-ticker.liquid       # Announcement bar ticker
│   ├── purelane-header.liquid       # Floating glass header navigation
│   ├── purelane-hero.liquid         # Hero banner with bottle stage carousel
│   ├── purelane-reviews.liquid      # Customer reviews ticker & stats
│   ├── purelane-ingredients.liquid  # Sourced from nature grid
│   ├── purelane-proof.liquid        # Clinical proof stats & rotator
│   ├── purelane-combos.liquid       # Curated combo bundle cards
│   ├── purelane-bundles.liquid      # Tiered bundle builder (Starter, Popular, Whole Home)
│   ├── purelane-shop.liquid         # Bestsellers product grid
│   ├── purelane-range.liquid        # Shelf range overview
│   ├── purelane-whybundles.liquid   # Feature value props
│   ├── purelane-categories.liquid   # Bundle categories grid
│   ├── purelane-trust.liquid        # Trust badge bar
│   ├── purelane-signup.liquid       # Newsletter signup card
│   └── purelane-footer.liquid       # Storefront footer
├── snippets/                # Reusable theme components
├── templates/
│   └── index.json           # Home page section order & block configuration
├── purelane-homepage.html   # Original reference prototype
└── README.md                # Project documentation
```

---

## 📝 Assessment Submission Questions

### 1. Metafields & Metaobjects Statement
> **"No custom metafields or metaobjects were created. The implementation primarily uses Shopify's native product data and editable theme section settings."**

### 2. Flagged Prototype Issues & Technical Solutions
* **Monolithic Single File:** Refactored ~1,700 lines of monolithic static HTML into 13+ modular Liquid sections with full merchant schemas (`{% schema %}`).
* **Fragile Scroll Tracking:** Replaced fragile `offsetTop` loops with viewport-relative `getBoundingClientRect()` tracking for reliable step-by-step progress rail dot highlighting.
* **GPU Render Lag:** Removed heavy CSS `filter: blur(7px)` transitions and replaced them with lightweight `translate3d` hardware-accelerated spring transforms (`0.22s`).
* **Page Load Jump:** Enforced `history.scrollRestoration = 'manual'` and initial `scrollTo(0, 0)` to guarantee the page always loads at the top hero section.

---

## 🛠️ Local Development & Shopify CLI Setup

### Prerequisites
* [Node.js](https://nodejs.org/) (v18+)
* [Shopify CLI](https://shopify.dev/docs/apps/tools/cli) (`npm install -g @shopify/cli`)

### Commands

```bash
# Clone the repository
git clone https://github.com/nazmeejawed/Purelane-Assignment-Shopify.git
cd Purelane-Assignment-Shopify

# Start local development server with live preview
shopify theme dev --store=purelane-f06sviua.myshopify.com

# Push theme updates to live theme
shopify theme push --store=purelane-f06sviua.myshopify.com --theme=188977152311 --allow-live
```

---

*Made with ❤️ for Purelane / Troopod Developer Assessment.*

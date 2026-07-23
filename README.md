# TechPanda Search Demo (Django + DRF + Bootstrap)

A simple demo project inspired by https://itechpanda.com/ — a software training institute
website. It has a Bootstrap 5 front end with a search bar, backed by a Django REST
Framework API that searches only the website's own stored content. If nothing matches,
the API returns an empty result set and the front end shows **"No result found"**.

## Project structure

```
techpanda_project/
├── manage.py
├── requirements.txt
├── techpanda_project/       # Django project settings/urls
├── search/                  # DRF app: model, serializer, search API, admin
│   └── management/commands/load_website_data.py   # seeds website content
└── templates/
    └── index.html           # Bootstrap front end with the search bar
```

## How it works

- `search.models.WebsiteContent` stores searchable items (courses, about us,
  placement, contact, blogs, FAQs) with a title, category, description, keywords and URL.
- `GET /api/search/?q=<term>` (open to all users, no login required) searches the
  `title`, `description` and `keywords` fields (case-insensitive) and returns matches.
  If keyword search finds nothing, it optionally falls back to an **AI-powered search**
  (see below) before giving up and returning `"count": 0, "results": []`.
- `templates/index.html` is the home page: as you type in the search box, a dropdown
  list of matching results appears **below the search box** (live, as-you-type, with a
  short debounce) — or **"No result found"** if nothing matches. The page also shows a
  browse grid of all content below the search section.
- Clicking a result in the dropdown (or a card in the browse grid) redirects to
  `/course/<id>/`, a dedicated detail page (`templates/detail.html`) showing the full
  description, category, page reference and related items for that entry.
- The navbar tabs (**Home, Courses, About Us, Placement, Contact, Blogs**) each redirect
  to a real page with information for that section, via `/category/<name>/`:
  - **Courses** has several items, so it shows a list/grid page (`category_list.html`)
    to pick from.
  - **About Us, Placement, Contact and Blogs** each map to a single content item, so the
    tab goes straight to that item's detail page.

## AI-powered search fallback (optional)

`search/ai_search.py` adds an optional LLM fallback: if keyword search finds zero
matches, the query and the full content catalog (titles, categories, descriptions)
are sent to Claude, which picks any items that genuinely answer the query — **using
only the website's own content, never outside knowledge**. If nothing fits, it
still returns "No result found."

**To enable it:**
```bash
pip install -r requirements.txt        # now includes the anthropic SDK
export ANTHROPIC_API_KEY="your-api-key-here"   # Windows (cmd): set ANTHROPIC_API_KEY=your-key
```
Get a key at https://console.anthropic.com.

**If you don't set the key**, the app runs exactly as before — the AI fallback
silently disables itself and you just get "No result found" for non-matching
queries, with zero extra cost or dependency issues.

The search response now also includes an `ai_suggested` boolean, and the front end
shows a small "AI found this for you" note above results that came from the fallback,
so it's clear to the user (and to you, in a demo) when AI stepped in versus plain
keyword matching.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows

pip install -r requirements.txt

python manage.py migrate
python manage.py load_website_data     # seeds the search content
python manage.py createsuperuser       # optional, for /admin/

# optional - enables the AI search fallback, see above
export ANTHROPIC_API_KEY="your-api-key-here"

python manage.py runserver
```

Then open http://127.0.0.1:8000/ in your browser and try searching for terms like
`python`, `aws`, `placement`, `contact`, `data science`, or `faq`.

## API endpoints

| Method | Endpoint              | Description                                       |
|--------|------------------------|----------------------------------------------------|
| GET    | `/`                    | Home page: live search dropdown + browse grid      |
| GET    | `/category/<name>/`    | Nav tab page (course/about/placement/contact/blog) |
| GET    | `/course/<id>/`        | Detail page for a single course/content item       |
| GET    | `/api/search/?q=...`   | Search website content (JSON), open to all users   |
| GET    | `/api/content/`        | List all stored website content (debugging)        |
| GET    | `/admin/`              | Django admin to manage content items                |

## Notes

- This is a simplified demo, not a scrape or clone of itechpanda.com — the content is
  written in original wording, based on the general information publicly shown on the
  site (course names, institute focus, placement support, contact details, FAQs).
- To add more searchable content, use `/admin/` or edit
  `search/management/commands/load_website_data.py` and re-run
  `python manage.py load_website_data`.

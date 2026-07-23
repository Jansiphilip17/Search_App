# TechPanda Search App

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



## API endpoints

| Method | Endpoint              | Description                                       |
|--------|------------------------|----------------------------------------------------|
| GET    | `/`                    | Home page: live search dropdown + browse grid      |
| GET    | `/category/<name>/`    | Nav tab page (course/about/placement/contact/blog) |
| GET    | `/course/<id>/`        | Detail page for a single course/content item       |
| GET    | `/api/search/?q=...`   | Search website content (JSON), open to all users   |
| GET    | `/api/content/`        | List all stored website content (debugging)        |
| GET    | `/admin/`              | Django admin to manage content items                |


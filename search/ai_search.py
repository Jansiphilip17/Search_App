"""
LLM-powered search fallback.

Only runs when the normal keyword search (SearchAPIView) finds zero matches.
It hands the user's query + the full website content catalog to Claude and
asks it to pick items that genuinely answer the query -- using ONLY the
provided content, never outside knowledge. If nothing fits, it returns [].
"""

import json
import os


def ai_search_fallback(query, items_queryset):
    """
    Returns a list of WebsiteContent ids that Claude judges to be a good
    match for `query`, based only on the given queryset. Returns an empty
    list if no API key is configured, the call fails, or nothing matches.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return []  # AI fallback silently disabled if no key is set

    try:
        from anthropic import Anthropic
    except ImportError:
        return []  # anthropic package not installed

    catalog = [
        {
            "id": item.id,
            "title": item.title,
            "category": item.category,
            "description": item.description,
        }
        for item in items_queryset
    ]

    system_prompt = (
        "You are a search assistant for the TechPanda website. You will be given a "
        "user's search query and a JSON list of every piece of content available on "
        "the website. Decide whether any of these items genuinely answer the query, "
        "using ONLY the provided list -- never outside knowledge, and never invent "
        "content that isn't in the list. If one or more items are a good match, "
        "respond with ONLY a JSON array of their integer ids, e.g. [3, 7]. If nothing "
        "in the list is a good match, respond with an empty JSON array: []. "
        "Return ONLY the JSON array and nothing else -- no explanation, no markdown."
    )

    user_message = f'User search query: "{query}"\n\nWebsite content:\n{json.dumps(catalog)}'

    try:
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        raw_text = response.content[0].text.strip()
        raw_text = raw_text.replace("```json", "").replace("```", "").strip()
        ids = json.loads(raw_text)
        if not isinstance(ids, list):
            return []
        return [int(i) for i in ids if isinstance(i, (int, float))]
    except Exception:
        # Any API error, timeout, or bad response -> fail gracefully to "no results"
        return []

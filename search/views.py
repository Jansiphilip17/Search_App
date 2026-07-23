from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WebsiteContent
from .serializers import WebsiteContentSerializer
from .ai_search import ai_search_fallback


def home_view(request):
    """Renders the Bootstrap home page with the live search bar plus a browse grid."""
    items = WebsiteContent.objects.all()
    return render(request, "index.html", {"items": items})


def course_detail_view(request, pk):
    """Renders a detail page for a single website content item (e.g. a course)."""
    item = get_object_or_404(WebsiteContent, pk=pk)
    related = WebsiteContent.objects.filter(category=item.category).exclude(pk=pk)[:3]
    return render(request, "detail.html", {"item": item, "related": related})


def category_view(request, category):
    """
    Renders info for a nav tab (Home, Courses, About Us, Placement, Contact, Blogs).

    If the category has exactly one content item (About Us, Placement, Contact, Blogs),
    it goes straight to that item's detail page. If it has several items (Courses),
    it shows a list/grid of them to choose from.
    """
    valid_categories = dict(WebsiteContent.CATEGORY_CHOICES)
    if category not in valid_categories:
        from django.http import Http404
        raise Http404("Unknown category")

    items = WebsiteContent.objects.filter(category=category)

    if items.count() == 0:
        from django.http import Http404
        raise Http404("No content found for this category")

    if items.count() == 1:
        item = items.first()
        related = WebsiteContent.objects.exclude(pk=item.pk)[:3]
        return render(request, "detail.html", {"item": item, "related": related})

    return render(
        request,
        "category_list.html",
        {"items": items, "category": category, "category_label": valid_categories[category]},
    )


class SearchAPIView(APIView):
    """
    GET /api/search/?q=<query>

    Searches only within the website's own content (title, description,
    keywords). Open to all users - no authentication required.

    Returns:
        200 with {"query": ..., "count": N, "results": [...]}   when matches found
        200 with {"query": ..., "count": 0, "results": []}      when nothing matches
                                                                  (frontend shows "No result found")
    """

    def get(self, request):
        query = request.query_params.get("q", "").strip()

        if not query:
            return Response({"query": query, "count": 0, "results": [], "ai_suggested": False})

        matches = WebsiteContent.objects.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(keywords__icontains=query)
        ).distinct()

        ai_suggested = False

        if not matches.exists():
            ai_ids = ai_search_fallback(query, WebsiteContent.objects.all())
            if ai_ids:
                matches = WebsiteContent.objects.filter(pk__in=ai_ids)
                ai_suggested = True

        serializer = WebsiteContentSerializer(matches, many=True)

        return Response(
            {
                "query": query,
                "count": matches.count(),
                "results": serializer.data,
                "ai_suggested": ai_suggested,
            }
        )


class ContentListAPIView(APIView):
    """GET /api/content/ - lists all website content (useful for debugging / browsing)."""

    def get(self, request):
        items = WebsiteContent.objects.all()
        serializer = WebsiteContentSerializer(items, many=True)
        return Response(serializer.data)

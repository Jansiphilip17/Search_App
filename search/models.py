from django.db import models


class WebsiteContent(models.Model):
    """
    Stores a searchable piece of content from the TechPanda website
    (course pages, about us, placement, contact, FAQs, etc.)
    """

    CATEGORY_CHOICES = [
        ("home", "Home"),
        ("course", "Course"),
        ("about", "About Us"),
        ("placement", "Placement"),
        ("contact", "Contact"),
        ("blog", "Blogs"),
        ("faq", "FAQ"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="course")
    description = models.TextField()
    keywords = models.CharField(
        max_length=500,
        help_text="Comma separated keywords to help the search engine match this content",
        blank=True,
    )
    url = models.CharField(max_length=300, blank=True, help_text="Relative/absolute page link")

    class Meta:
        ordering = ["category", "title"]

    def __str__(self):
        return self.title

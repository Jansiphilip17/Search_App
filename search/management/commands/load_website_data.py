from django.core.management.base import BaseCommand

from search.models import WebsiteContent

DATA = [
    {
        "title": "About TechPanda",
        "category": "home",
        "description": (
            "TechPanda is a software training institute based in Chennai that provides "
            "job-oriented IT courses along with placement assistance. Training is offered "
            "across several Chennai locations including T.Nagar, Velachery, Sholinganallur, "
            "Tambaram, Anna Nagar, as well as Kochi, with a focus on real-time projects and "
            "hands-on learning."
        ),
        "keywords": "techpanda, software training institute, chennai, it courses, placement assistance",
        "url": "/index.html",
    },
    {
        "title": "Data Analyst Course",
        "category": "course",
        "description": (
            "A job-oriented Data Analyst training program covering practical data analysis "
            "skills, real-time projects and tools used by working data analysts."
        ),
        "keywords": "data analyst, data analytics, course, training",
        "url": "/course/data-analyst-course-chennai.html",
    },
    {
        "title": "Data Science & AI Engineer Course",
        "category": "course",
        "description": (
            "Training program for Data Science and AI Engineering roles, combining "
            "statistics, machine learning and real-world project work."
        ),
        "keywords": "data science, ai engineer, artificial intelligence, machine learning, course",
        "url": "/course/data-science-course-chennai.html",
    },
    {
        "title": "Generative AI Engineer Course",
        "category": "course",
        "description": (
            "A course focused on Generative AI concepts and tools, designed to prepare "
            "learners for roles building AI-driven applications."
        ),
        "keywords": "generative ai, gen ai, course, engineer",
        "url": "/course/generative-ai-course-chennai.html",
    },
    {
        "title": "Data Engineering & Analytics Course",
        "category": "course",
        "description": (
            "Covers data pipelines, data engineering tools and analytics practices used to "
            "prepare data for analysis at scale."
        ),
        "keywords": "data engineering, data engineer, analytics, course",
        "url": "/course/data-engineering-course-chennai.html",
    },
    {
        "title": "ETL Testing Engineer Course",
        "category": "course",
        "description": (
            "A training program on ETL (Extract, Transform, Load) testing practices used in "
            "data warehousing and reporting projects."
        ),
        "keywords": "etl testing, etl, data warehouse, course",
        "url": "/course/etl-testing-course-chennai.html",
    },
    {
        "title": "AWS Cloud & DevOps Engineer Course",
        "category": "course",
        "description": (
            "A course covering AWS cloud services and DevOps practices, aimed at preparing "
            "learners for cloud engineering and DevOps roles."
        ),
        "keywords": "aws, cloud, devops, course, engineer",
        "url": "/course/aws-devops-course-chennai.html",
    },
    {
        "title": "Java Application Developer Course",
        "category": "course",
        "description": (
            "Training in Java application development, covering core concepts used to build "
            "job-ready development skills."
        ),
        "keywords": "java, application developer, programming, course",
        "url": "/course/java-selenium-course-chennai.html",
    },
    {
        "title": "Test Automation Engineer Course",
        "category": "course",
        "description": (
            "A course on automated software testing tools and techniques for aspiring test "
            "automation engineers."
        ),
        "keywords": "test automation, software testing, selenium, course",
        "url": "/course/java-selenium-course-chennai.html",
    },
    {
        "title": "Python Application Developer Course",
        "category": "course",
        "description": (
            "Covers Python programming fundamentals through to application development, with "
            "real-time project work."
        ),
        "keywords": "python, application developer, programming, course",
        "url": "/course/python-course-chennai.html",
    },
    {
        "title": "Full Stack Test Automation Engineer Course",
        "category": "course",
        "description": (
            "A combined training track covering full stack development concepts alongside "
            "test automation skills."
        ),
        "keywords": "full stack, test automation, course, engineer",
        "url": "/course.html",
    },
    {
        "title": "About Us",
        "category": "about",
        "description": (
            "TechPanda helps students, freshers, graduates and working professionals build "
            "careers in IT through job-oriented training in Data Analytics, Python, AWS "
            "DevOps, Data Science, Data Engineering, ETL Testing, Generative AI and Software "
            "Testing. The institute offers both online and classroom training across Chennai."
        ),
        "keywords": "about techpanda, about us, institute, chennai",
        "url": "/about-us.html",
    },
    {
        "title": "Placement Assistance",
        "category": "placement",
        "description": (
            "Placement support includes resume building, LinkedIn profile optimization, mock "
            "interviews, technical interview preparation and job referrals, aimed at helping "
            "students become job-ready."
        ),
        "keywords": "placement, placement assistance, jobs, interview preparation, resume",
        "url": "/placement-training-chennai.html",
    },
    {
        "title": "Contact Us",
        "category": "contact",
        "description": (
            "TechPanda can be reached by phone at +91 98846 78282 or by email at "
            "admin@itechpanda.com. The main training center is located in T.Nagar, Chennai, "
            "with additional presence in Velachery, Sholinganallur, Tambaram, Anna Nagar and "
            "Kochi. Working hours are Monday to Saturday, 9 AM to 7 PM."
        ),
        "keywords": "contact, phone number, email, address, location",
        "url": "/contact-us.html",
    },
    {
        "title": "Blogs",
        "category": "blog",
        "description": (
            "The blogs section shares articles related to IT careers, course guidance and "
            "industry trends relevant to students preparing for a career in technology."
        ),
        "keywords": "blogs, articles, career guidance, it trends",
        "url": "/blogs.html",
    },
    {
        "title": "FAQ: Best software training institute in Chennai",
        "category": "faq",
        "description": (
            "TechPanda is positioned as a software training institute in Chennai offering "
            "job-oriented IT courses, real-time projects, expert trainers and placement "
            "assistance across programs like Data Analytics, Python, AWS DevOps, Data "
            "Science, ETL Testing, Data Engineering and Generative AI."
        ),
        "keywords": "faq, best institute, software training, chennai",
        "url": "/index.html#faq",
    },
    {
        "title": "FAQ: Best IT course for freshers",
        "category": "faq",
        "description": (
            "Popular course choices for freshers include Data Analyst, Python Development, "
            "AWS DevOps, Data Science, ETL Testing and Generative AI, based on current demand "
            "and job opportunities."
        ),
        "keywords": "faq, freshers, best course, beginners",
        "url": "/index.html#faq",
    },
    {
        "title": "FAQ: Does TechPanda provide placement assistance",
        "category": "faq",
        "description": (
            "Yes, placement assistance is provided and includes resume building, LinkedIn "
            "profile optimization, mock interviews, technical interview preparation and job "
            "referrals."
        ),
        "keywords": "faq, placement assistance, yes, support",
        "url": "/index.html#faq",
    },
    {
        "title": "FAQ: Can non-IT students join",
        "category": "faq",
        "description": (
            "Courses are designed to accommodate beginners and non-IT graduates, with "
            "structured learning, practical training and mentor support to help build the "
            "skills needed for an IT career."
        ),
        "keywords": "faq, non-it, beginners, career change",
        "url": "/index.html#faq",
    },
    {
        "title": "FAQ: Why choose TechPanda",
        "category": "faq",
        "description": (
            "TechPanda emphasizes practical learning through real-time projects, an "
            "industry-aligned curriculum, expert trainers, small batch sizes and placement "
            "assistance."
        ),
        "keywords": "faq, why choose techpanda, reasons",
        "url": "/index.html#faq",
    },
    {
        "title": "FAQ: Placement timeline after course completion",
        "category": "faq",
        "description": (
            "Placement timelines vary depending on the course, skill level and job market "
            "demand. Completing projects, attending mock interviews and following placement "
            "guidance can improve the chances of a faster placement."
        ),
        "keywords": "faq, placement timeline, how long, job market",
        "url": "/index.html#faq",
    },
]


class Command(BaseCommand):
    help = "Loads sample TechPanda website content into the database for the search feature."

    def handle(self, *args, **options):
        WebsiteContent.objects.all().delete()
        objs = [WebsiteContent(**item) for item in DATA]
        WebsiteContent.objects.bulk_create(objs)
        self.stdout.write(self.style.SUCCESS(f"Loaded {len(objs)} website content items."))

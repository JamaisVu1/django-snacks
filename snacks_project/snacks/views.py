from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/en/8/82/Takis_logo.png?20230715002532",
                "title": "Takis",
                "description": "Takis are a brand of rolled corn tortilla chips known for their intense flavor and spicy kick, available in various fiery flavors.",
                "reference_url": "https://en.wikipedia.org/wiki/Takis_(snack)"
            }
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'
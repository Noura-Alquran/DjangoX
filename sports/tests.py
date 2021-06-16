from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Sport


class SportsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Mohammad", email="Mohammed@email.com", password="pwd"
        )

        self.sport = Sport.objects.create(
            player_name="Noura", coach_s_name=self.user,description="No info" 
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.sport), "Noura")

    def test_sport_content(self):
        self.assertEqual(f"{self.sport.player_name}", "Noura")
        self.assertEqual(f"{self.sport.coach_s_name}", "Mohammed@email.com")
        self.assertEqual(self.sport.description,"No info")


    def test_sport_list_view(self):
        response = self.client.get(reverse("sport_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Noura")
        self.assertTemplateUsed(response, "sports/sport-list.html")

    def test_sport_detail_view(self):
        response = self.client.get(reverse("sport_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response,"coach_s_name:Mohammed@email.com")
        self.assertTemplateUsed(response, "sports/sport-detail.html")

    def test_sport_create_view(self):
        response = self.client.post(
            reverse("sport_create"),
            {
                "player_name": "Mona",
                "coach_s_name": self.user.id,
                "description": "good player",
            }, follow=True
        )

        self.assertRedirects(response, reverse("sport_detail", args="2"))
        self.assertContains(response, "Mona")



    def test_sport_update_view_redirect(self):
        response = self.client.post(
            reverse("sport_update", args="1"),
            {"player_name": "Updated player_name","coach_s_name":self.user.id,"description":"New description"}
        )

        self.assertRedirects(response, reverse("sport_detail", args="1"))

    def test_sport_delete_view(self):
        response = self.client.get(reverse("sport_delete", args="1"))
        self.assertEqual(response.status_code, 200)
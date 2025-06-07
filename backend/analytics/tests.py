from django.test import TestCase, Client

# Create your tests here.

client = Client()
response = client.get('/analytics/rating/', {
    'start': '2024-01-01 00:00:00',
    'end': '2025-12-31 23:59:59'
})
print(response.json())

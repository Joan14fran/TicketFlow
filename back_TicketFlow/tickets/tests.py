from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Ticket, Category

# Obtenemos el modelo de usuario personalizado (CustomUser)
User = get_user_model()

class TicketFlowSystemTest(APITestCase):

    def setUp(self):
        """
        Configuración inicial que se ejecuta antes de cada prueba.
        Creamos un usuario y una categoría para poder probar los tickets.
        """
        self.user = User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword123',
            role='client'
        )
        
        self.category = Category.objects.create(
            name='Soporte General',
        )

        self.health_url = reverse('health_check') # /api/health/
        self.ticket_list_url = reverse('ticket-list') # /api/tickets/tickets/

    def test_health_check(self):
        """
        Prueba 1: Verificar que el endpoint de salud responda correctamente.
        """
        response = self.client.get(self.health_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'ok')

    def test_create_ticket_authenticated(self):
        """
        Prueba 2: Verificar que un usuario autenticado puede crear un ticket.
        """
        self.client.force_authenticate(user=self.user)
        
        data = {
            'title': 'Error en la impresora',
            'description': 'No imprime a color',
            'priority': 'media',
            'category': self.category.id
        }
        
        response = self.client.post(self.ticket_list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
        self.assertEqual(Ticket.objects.get().title, 'Error en la impresora')
        self.assertEqual(Ticket.objects.get().created_by, self.user)

    def test_create_ticket_unauthenticated(self):
        """
        Prueba 3: Verificar que la seguridad funciona (usuario no logueado NO puede crear tickets).
        """
        data = {
            'title': 'Intento de hackeo',
            'description': 'No debería pasar',
            'priority': 'alta',
            'category': self.category.id
        }
        
        response = self.client.post(self.ticket_list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
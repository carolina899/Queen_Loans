from django.test import TestCase

# Create your tests here. 
# tests.py
from django.test import TestCase
from .models import Loans  

class QueenLoansTestCase(TestCase):
    def setUp(self):
        # Crear préstamos de prueba en Queen Loans
        Loans.objects.create(titular="Alice", saldo=1000)
        Loans.objects.create(titular="Bob", saldo=500)

    def test_deposito(self):
        """Verifica que los clientes de Queen Loans pueden abonar a su préstamo"""
        alice = Loans.objects.get(titular="Alice")
        alice.depositar(250)  # Método que aumenta el saldo del préstamo
        self.assertEqual(alice.saldo, 1250)

    def test_retiro(self):
        """Verifica que los clientes de Queen Loans pueden retirar o usar crédito"""
        bob = Loans.objects.get(titular="Bob")
        bob.retirar(200)  # Método que disminuye el saldo del préstamo
        self.assertEqual(bob.saldo, 300)

    def test_retiro_saldo_insuficiente(self):
        """No se puede usar más crédito del disponible en Queen Loans"""
        bob = Loans.objects.get(titular="Bob")
        with self.assertRaises(ValueError):
            bob.retirar(600)

    def test_str(self):
        """Verifica la representación en string de los préstamos de Queen Loans"""
        alice = Loans.objects.get(titular="Alice")
        self.assertEqual(str(alice), "Alice - $1000")
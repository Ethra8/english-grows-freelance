import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_countries.fields import CountryField

from individual_services.models import IndivService
from profiles.models import UserProfile


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile,
                                     on_delete=models.CASCADE,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES,
                              default='pending')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added.
        """
        result = self.lineitems.aggregate(Sum('lineitem_total'))
        order_total_sum = result['lineitem_total__sum'] or 0
        self.order_total = order_total_sum
        self.grand_total = self.order_total  # Adjust this if needed

    def send_confirmation_email(self):
        """
        Send order confirmation email to the user.
        """
        subject = f"Order Confirmation - {self.order_number}"
        message = render_to_string('checkout/order_confirmation_email.html', {
            'order': self,
            'order_number': self.order_number,
            'full_name': self.full_name,
            'grand_total': self.grand_total,
        })
        plain_message = strip_tags(message)
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = self.email

        send_mail(subject, plain_message, from_email, [to_email],
                  html_message=message)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already and update totals.
        """
        # Generate order number if this is a new order (no primary key yet)
        if not self.pk:
            self.order_number = self._generate_order_number()

        # Save the order first to ensure it's in the database
        super().save(*args, **kwargs)

        # Update totals based on related line items
        self.update_total()

        # Save the updated totals
        super().save(*args, **kwargs)

        # Note: Do not send email or change status here!

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    service = models.ForeignKey(IndivService, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.service.price * self.quantity
        super().save(*args, **kwargs)

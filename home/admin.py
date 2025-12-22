from django.contrib import admin, messages
from django_summernote.admin import SummernoteModelAdmin

from .models import CompanyContact, Subscription, EmailTemplate
from .utils import send_email_campaign


admin.site.register(CompanyContact)


@admin.action(description="Send Email Campaign")
def trigger_email_campaign(modeladmin, request, queryset):
    for template in queryset:
        send_email_campaign(template.id)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_subscribed')


@admin.register(EmailTemplate)
class EmailTemplateAdmin(SummernoteModelAdmin):

    # Display ID, name, and subject
    list_display = ('name', 'subject', 'id')
    actions = ['send_campaign']
    summernote_fields = ('content',)

    def send_campaign(self, request, queryset):
        # Loop through selected templates and send email campaigns
        for template in queryset:
            success = send_email_campaign(template.id)
            if success:
                self.message_user(request, f"Campaign\
                '{template.name}' sent successfully.")
            else:
                self.message_user(
                    request,
                    f"Failed to send campaign '{template.name}'.",
                    level=messages.ERROR
                )

    send_campaign.short_description = "Send Email Campaign"

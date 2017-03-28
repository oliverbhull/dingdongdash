from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.sites.admin import SiteAdmin

from allauth.account.admin import EmailAddressAdmin
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken
from organizations.admin import OrganizationUserAdmin, OrganizationOwnerAdmin
from organizations.models import Organization, OrganizationUser
from schedule.models import CalendarRelation, Rule, Occurrence, Event
from schedule.admin import CalendarAdminOptions

from .models import Button, ButtonAction, Phone


##
# Core Admin
##
class ButtonAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ('serial_number', 'organization',)

        return super(ButtonAdmin, self).get_readonly_fields(request, obj)

    def get_queryset(self, request):
        if not request.user.is_superuser:
            organization_user = OrganizationUser.objects.filter(user=request.user)
            organizations = Organization.objects.filter(organization_users=organization_user)
            return Button.objects.filter(organization__in=organizations)

        return Button.objects.all()


admin.site.register(Button, ButtonAdmin)


class ButtonActionAdmin(admin.ModelAdmin):
    pass


admin.site.register(ButtonAction, ButtonActionAdmin)


class PhoneAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if(request.user.is_staff):
            return Phone.objects.all()
        return Phone.objects.filter(user=request.user)


admin.site.register(Phone, PhoneAdmin)


##
# Removals and Modifications of Third Party Models
##

# Function and Base class for all modified ModelAdmin
def get_model_perms(self, request):
    if not request.user.is_staff:
        return {}

    return {
        'add': self.has_add_permission(request),
        'change': self.has_change_permission(request),
        'delete': self.has_delete_permission(request),
    }


class DDDModelAdmin(admin.ModelAdmin):
    pass


CalendarAdminOptions.get_model_perms = get_model_perms
DDDModelAdmin.get_model_perms = get_model_perms
EmailAddressAdmin.get_model_perms = get_model_perms
GroupAdmin.get_model_perms = get_model_perms
SiteAdmin.get_model_perms = get_model_perms
UserAdmin.get_model_perms = get_model_perms


admin.site.unregister(CalendarRelation)
admin.site.register(CalendarRelation, DDDModelAdmin)

admin.site.unregister(Event)
admin.site.register(Event, DDDModelAdmin)

admin.site.unregister(Rule)
admin.site.register(Rule, DDDModelAdmin)

admin.site.unregister(Occurrence)
admin.site.register(Occurrence, DDDModelAdmin)

admin.site.unregister(Organization)


class OrganizationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organization, OrganizationAdmin)

OrganizationAdmin.get_model_perms = get_model_perms
OrganizationUserAdmin.get_model_perms = get_model_perms
OrganizationOwnerAdmin.get_model_perms = get_model_perms


admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)

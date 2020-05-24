import requests


from django.contrib.auth import get_permission_codename
from django.contrib import admin


PERMISSION_API = "http://permission.sso.com/has_perm?user={}&perm_code={}"


class PostAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        opts = self.opts
        codename = get_permission_codename('add', opts)
        perm_code = "%s.%s" %(opts.app_label, codename)
        resp = requests.get(PERMISSION_API.format(request.user.username, perm_code))
        if resp.status_code == 200:
            return True
        else:
            return False

from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.tier == "admin"
        )


class IsPremium(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.tier in ["premium", "admin"]
        )
    
class IsStandard(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.tier in ["standard", "premium", "admin"]
        )
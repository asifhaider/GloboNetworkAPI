# -*- coding:utf-8 -*-
'''
@author: William Vedroni da Silva
@organization: S2it
@copyright: 2014 globo.com todos os direitos reservados.
'''
from networkapi.admin_permission import AdminPermission
from networkapi.auth import has_perm

from rest_framework.permissions import BasePermission


class Read(BasePermission):

    def has_permission(self, request, view):
        return has_perm(
            request.user,
            AdminPermission.POOL_MANAGEMENT,
            AdminPermission.READ_OPERATION
        )


class Write(BasePermission):

    def has_permission(self, request, view):
        return has_perm(
            request.user,
            AdminPermission.POOL_MANAGEMENT,
            AdminPermission.WRITE_OPERATION
        )


class ScriptRemovePermission(BasePermission):

    def has_permission(self, request, view):
        return has_perm(
            request.user,
            AdminPermission.POOL_REMOVE_SCRIPT,
            AdminPermission.WRITE_OPERATION
        )


class ScriptCreatePermission(BasePermission):

    def has_permission(self, request, view):
        return has_perm(
            request.user,
            AdminPermission.POOL_CREATE_SCRIPT,
            AdminPermission.WRITE_OPERATION
        )


class ScriptAlterPermission(BasePermission):

    def has_permission(self, request, view):
        return has_perm(
            request.user,
            AdminPermission.POOL_ALTER_SCRIPT,
            AdminPermission.WRITE_OPERATION
        )

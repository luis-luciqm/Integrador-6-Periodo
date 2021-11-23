from rolepermissions.roles import AbstractUserRole

class Usuario(AbstractUserRole):
    available_permission = {}

class Empresa(AbstractUserRole):
    available_permissions = {}


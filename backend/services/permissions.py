import asyncio
from core.config import settings
from repositories import get_roles_repository, get_permissions_repository

class RBACService:
    def __init__(self, roles_repo=None, perms_repo=None):
        self.roles_repo = roles_repo if roles_repo is not None else get_roles_repository()
        self.perms_repo = perms_repo if perms_repo is not None else get_permissions_repository()

    async def seed(self):
        if not settings.rbac.auto_create_missing:
            return

        # Собираем все уникальные разрешения из настроек (без "*")
        all_permission_names = set()
        for role_config in settings.rbac.roles.values():
            for perm in role_config.permissions:
                if perm != "*":
                    all_permission_names.add(perm)

        # Получаем уже существующие разрешения по именам
        existing_perms = await self.perms_repo.get_permissions_by_names(list(all_permission_names))
        existing_perm_names = {perm["name"] for perm in existing_perms}

        # Формируем список разрешений для создания
        perms_to_create = []
        for perm_name in all_permission_names:
            if perm_name not in existing_perm_names:
                perms_to_create.append({
                    "name": perm_name,
                    "description": "",
                    "category": "general"
                })

        # Создаем отсутствующие разрешения
        if perms_to_create:
            created_perms = await self.perms_repo.bulk_create_permissions(perms_to_create)
            print(f"Созданы разрешения: {[perm['name'] for perm in created_perms]}")

        # Обработка каждой роли из настроек
        for role_name, role_config in settings.rbac.roles.items():
            existing_role = await self.roles_repo.get_role_by_name(role_name)
            if existing_role:
                print(f"Роль '{role_name}' уже существует")
                continue

            # Если роль имеет разрешение "*" - привязываем все разрешения
            if "*" in role_config.permissions:
                perms = await self.perms_repo.get_permissions_by_names(list(existing_perm_names))
            else:
                perms = await self.perms_repo.get_permissions_by_names(role_config.permissions)

            # Создаем роль, оборачивая идентификаторы разрешений в словарь {"id": ...}
            role_data = {
                "name": role_name,
                "is_default": role_config.is_default,
                "permissions": [{"id": perm["id"]} for perm in perms] if perms else []
            }
            created_role = await self.roles_repo.create_role(role_data)
            print(f"Создана роль: {created_role['name']}")


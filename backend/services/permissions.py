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

        # --- Этап 1. Работа с разрешениями ---
        # Собираем все уникальные разрешения из настроек (без "*")
        all_permission_names = set()
        for role_config in settings.rbac.roles.values():
            for perm in role_config.permissions:
                if perm != "*":
                    all_permission_names.add(perm)

        # Получаем уже существующие разрешения по именам
        existing_perms = await self.perms_repo.get_permissions_by_names(list(all_permission_names))
        existing_perm_names = {perm["name"] for perm in existing_perms}

        # Формируем список разрешений для создания, если их ещё нет в БД
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

        # --- Этап 2. Создание ролей (без наследования) ---
        created_roles = {}  # Словарь для хранения созданных ролей по имени
        for role_name, role_config in settings.rbac.roles.items():
            existing_role = await self.roles_repo.get_role_by_name(role_name)
            if existing_role:
                print(f"Роль '{role_name}' уже существует")
                created_roles[role_name] = existing_role
                continue

            # Обработка разрешений для роли
            if "*" in role_config.permissions:
                # Если роль имеет разрешение "*", выбираем все разрешения из БД
                perms = await self.perms_repo.list()
            else:
                perms = await self.perms_repo.get_permissions_by_names(role_config.permissions)

            role_data = {
                "name": role_name,
                "is_default": role_config.is_default,
                # Оборачиваем идентификатор разрешения в словарь {"id": ...}
                "permissions": [{"id": perm["id"]} for perm in perms] if perms else [],
                # Сначала наследование оставляем пустым – обновим позже
                "parent_roles": []
            }
            created_role = await self.roles_repo.create_role(role_data)
            created_roles[role_name] = created_role
            print(f"Создана роль: {created_role['name']}")

        # --- Этап 3. Обработка наследования ролей ---
        for role_name, role_config in settings.rbac.roles.items():
            if role_config.inherits:
                parent_links = []
                for parent_name in role_config.inherits:
                    parent_role = created_roles.get(parent_name)
                    if parent_role:
                        parent_links.append({"id": parent_role["id"]})
                if parent_links:
                    # Обновляем роль, задавая поле parent_roles
                    updated_role = await self.roles_repo.update(created_roles[role_name]["id"], {"parent_roles": parent_links})
                    created_roles[role_name] = updated_role
                    print(f"Обновлена роль '{role_name}' с наследованием: {role_config.inherits}")

    async def list_all_roles(self):
        return await self.roles_repo.get_all_roles(include_permissions=True)

from core.config import settings
from typing import Set

class RBACInitializationService:
    def __init__(self, roles_repository, permissions_repository):
        self.roles_repo = roles_repository
        self.permissions_repo = permissions_repository
    
    async def initialize(self) -> None:
        if not await self._is_initialized():
            await self._create_missing_permissions()
            await self._create_roles_with_permissions()

    async def _is_initialized(self) -> bool:
        roles = await self.roles_repo.list()
        permissions = await self.permissions_repo.list()
        return len(roles) > 0 and len(permissions) > 0

    async def _create_missing_permissions(self) -> None:
        required_permissions: Set[str] = set()
        for role_config in settings.rbac.roles.values():
            required_permissions.update(role_config.permissions)
        required_permissions.discard("*")
        
        existing_permissions = await self.permissions_repo.list()
        existing_names = {p["name"] for p in existing_permissions}
        missing_permissions = required_permissions - existing_names
        
        if missing_permissions:
            await self.permissions_repo.create_many(
                [{"name": name, "description": f"Auto: {name}"} for name in missing_permissions]
            )

    async def _create_roles_with_permissions(self) -> None:
        all_permissions = await self.permissions_repo.list()
        permission_map = {p["name"]: {"id": str(p["id"])} for p in all_permissions}

        for role_name, role_config in settings.rbac.roles.items():
            if await self.roles_repo.retrieve_by_field("name", role_name):
                continue

            permissions = []
            if "*" in role_config.permissions:
                permissions = [{"id": str(p["id"])} for p in all_permissions]
            else:
                for perm_name in role_config.permissions:
                    if perm_name not in permission_map:
                        if settings.rbac.auto_create_missing:
                            new_perm = await self.permissions_repo.create({
                                "name": perm_name,
                                "description": f"For role {role_name}"
                            })
                            permission_map[perm_name] = {"id": str(new_perm["id"])}
                        else:
                            continue
                    permissions.append(permission_map[perm_name])

            await self.roles_repo.create({
                "name": role_name,
                "description": role_config.description or role_name,
                "permissions": permissions,
                "is_default": role_config.is_default,
                "inherits": role_config.inherits
            })

def get_rbac_init_service(roles_repo, permissions_repo):
    return RBACInitializationService(roles_repo, permissions_repo)
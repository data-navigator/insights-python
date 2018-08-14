# coding=utf-8

from typing import List, Any


class UserMembership:
    username: str
    member_type: str
    applications: int


class Group:
    id: str
    title: str
    is_invitation_only: bool
    owner: str
    description: None
    snippet: str
    tags: List[str]
    phone: None
    sort_field: str
    sort_order: str
    is_view_only: bool
    thumbnail: str
    created: int
    modified: int
    access: str
    capabilities: List[Any]
    is_fav: bool
    is_read_only: bool
    protected: bool
    auto_join: bool
    notifications_enabled: bool
    provider: None
    provider_group_name: None
    user_membership: UserMembership
    collaboration_info: dict

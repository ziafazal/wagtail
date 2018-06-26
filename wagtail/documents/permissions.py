from wagtail.core.permission_policies.collections import (
    CollectionOwnershipPermissionPolicy,
    CollectionPermissionPolicy,
)
from wagtail.documents.models import Document, get_document_model

permission_policy = CollectionOwnershipPermissionPolicy(
    get_document_model(),
    auth_model=Document,
    owner_field_name='uploaded_by_user'
)

collection_permission_policy = CollectionPermissionPolicy(Document)

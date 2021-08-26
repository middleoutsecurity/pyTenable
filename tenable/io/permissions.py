'''
permissions
===========

The following methods allow for interaction into the Tenable.io
:devportal`permissions <permissions-1>` API endpoints.

Methods available on ``tio.permissions``:

.. rst-class:: hide-signature
.. autoclass:: PermissionsAPI

    .. automethod:: change
    .. automethod:: list
'''
from typing import Dict, List
from .base import TIOEndpoint

class PermissionsAPI(TIOEndpoint):
    _path = 'permissions'

    def change(
            self,
            otype: str,
            id: int,
            *acls: Dict
    ) -> None:
        '''
        Modify the permission of a specific object.

        :devportal:`permissions: change <permissions-change>`

        Args:
            otype (str):
                The type of object to change.
            id (int):
                The unique identifier of the object.
            *acls (dict):
                ACL dictionaries inform Tenable.io how to handle permissions of
                the various objects within Tenable.io.  Please refer to the
                `permissions documentation`_ for more details.

        Returns:
            :obj:`None`:
                The object permissions were successfully changed.

        .. _permissions documentation:
            https://developer.tenable.com/docs/permissions
        '''
        # Check to make sure all of the ACLs are dictionaries.
        for item in acls:
            self._check('acl', item, dict)

            # validate inputs and make the API call.
            self._check('otype', otype, str)
            self._check('id', id, int)
            self._api.put(f'{self._path}/{otype}/{id}', json={'acls': acls})

    def list(
            self,
            otype: str,
            id: int
    ) -> List:
        '''
        List the permissions of a specific object.

        :devportal:`permissions: list <permissions-list>`

        Args:
            otype (str):
                The type of object being queried.
            id (int):
                The unique identifier of the object.

        Returns:
            :obj:`list`:
                The permission recourse record listings for the specified object.
        '''
        # validate inputs and make the API call.
        self._check('otype', otype, str)
        self._check('id', id, int)
        return self._api.get(f'{self._path}/{otype}/{id}').json()['acls']

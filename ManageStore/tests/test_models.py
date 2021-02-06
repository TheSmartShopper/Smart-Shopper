from unittest import TestCase

from ManageStore.models import Store


class TestStore(TestCase):
    def test_save(self):
        store = Store.objects.create(
            name='store1',
            description='Description',
            image='http://placehold.it/900x400',
            type='test',
            state=True,
            start_hours='08:00:00',
            close_hours='23:00:00',
        )
        store.save()

        self.assertTrue(isinstance(store, Store))

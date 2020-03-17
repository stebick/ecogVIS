from ecogvis.functions.subDialogs import SelectChannelsDialog
from unittest import TestCase

class SelectChannelsDialogTest(TestCase):
 
    def setUp(self):
        stringlist = ['a','b']
        checked = ['True','False']
        self.dialog = SelectChannelsDialog(stringlist, checked)

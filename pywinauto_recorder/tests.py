# -*- coding: utf-8 -*-

import unittest

from recorder_fn import *


class TestEntryMethods(unittest.TestCase):

	def test_get_entry_elements(self):
		entry_list = [
						'Name:::Type#[0,0]%(2,-24)', '::Type#[0,0]%(2,-24)', 'Name:::#[0,0]%(2,-24)',
						'Name:::Type#[0,0]', '::Type#[0,0]', 'Name:::#[0,0]',
						'Name:::Type', '::Type', 'Name:::',
						'Name::Type', '::Type', 'Name::'
					]
		for i, entry in enumerate(entry_list):
			str_name, str_type, y_x, dx_dy = get_entry(entry)
			print get_entry(entry)
			if i % 3 == 0:
				if i < 9:
					self.assertEqual(str_name, 'Name:')
				else:
					self.assertEqual(str_name, 'Name')
				self.assertEqual(str_type, 'Type')
			if i % 3 == 1:
				self.assertEqual(str_name, '')
				self.assertEqual(str_type, 'Type')
			if i % 3 == 2:
				if i < 9:
					self.assertEqual(str_name, 'Name:')
				else:
					self.assertEqual(str_name, 'Name')
				self.assertEqual(str_type, None)
			if i < 3:
				self.assertEqual(dx_dy, (2, -24))
			else:
				self.assertEqual(dx_dy, None)
			if i < 6:
				self.assertEqual(y_x, [0,0])
			else:
				self.assertEqual(y_x, None)


	def test_fake(self):
		self.assertEqual(None, None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
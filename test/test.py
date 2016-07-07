import unittest
import os


class BotTest(unittest.TestCase):
    def test_languages(self):
        from bot import osmbot_blueprint
        print os.getcwd()
        lang_dirs = os.listdir('../bot/locales')
        for lang_dir in lang_dirs:
            self.assertTrue(lang_dir in osmbot_blueprint.avaible_languages.values())

if __name__ == '__main__':
    unittest.main()

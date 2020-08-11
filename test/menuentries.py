import unittest
import joymenu.menuentries as sut


class ParserTests(unittest.TestCase):
    def setUp(self) -> None:
        yaml_content = '''menu-entries:
  - title: Steam link
    icon: ./steam-link.png
    selected_icon: ./selected-steam-link.png
    script: .steam-link.sh
  - title: Turn on Gamer PC
    icon: ./gamer-pc.png
    selected_icon: ./selected-gamer-pc.png
    script: .wake-gamer.sh
  - title: Kodi
    icon: ./kodi.png
    selected_icon: ./selected-kodi.png
    script: ./kodi.sh
  - title: Stremio
    icon: ./stremio.png
    selected_icon: ./selected-stremio.png
    script: ./stremio.sh'''
        with open("joymenu.yaml", "w") as file:
            file.write(yaml_content)

    def test_parsing(self):
        try:
            file = sut.Parser()
        except Exception:
            self.fail("Some exception was raised")

    def test_parsing_default_config(self):
        expected = "[[t=Steam link,i=./steam-link.png,s=.steam-link.sh], [t=Turn on Gamer PC,i=./gamer-pc.png,s=.wake-gamer.sh], [t=Kodi,i=./kodi.png,s=./kodi.sh], [t=Stremio,i=./stremio.png,s=./stremio.sh]]"
        file = sut.Parser()
        self.assertEqual(file._entries.__repr__(), expected)


if __name__ == '__main__':
    unittest.main()

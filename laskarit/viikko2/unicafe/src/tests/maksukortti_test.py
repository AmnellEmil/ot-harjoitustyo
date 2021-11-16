import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti),"saldo: 1.1")

    def test_saldo_vahenee_oikein_jos_saldo_riittaa(self):
        self.maksukortti.lataa_rahaa(100)
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")

    def test_saldo_ei_muutu_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(str(self.maksukortti),"saldo: 0.1")

    def test_true_jos_rahaa_tarpeeksi(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.ota_rahaa(100),True)

    def test_false_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(self.maksukortti.ota_rahaa(200),False)



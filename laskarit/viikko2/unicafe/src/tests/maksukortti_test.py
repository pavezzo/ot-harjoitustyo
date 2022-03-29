import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")

    def test_saldo_vahenenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_palauttaa_true_jos_rahaa_on(self):
        totta = self.maksukortti.ota_rahaa(5)
        self.assertEqual(totta, True)

    def test_palauttaa_false_jos_rahat_ei_riita(self):
        valhe = self.maksukortti.ota_rahaa(11)
        self.assertEqual(valhe, False)

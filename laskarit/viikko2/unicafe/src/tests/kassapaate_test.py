import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_lounaiden_maara_oikein(self):
        self.assertEqual(100000, self.kassapaate.kassassa_rahaa)
        self.assertEqual(0, self.kassapaate.edulliset)
        self.assertEqual(0, self.kassapaate.maukkaat)


    def test_syo_edullisesti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_rahat_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_rahat_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_rahat_ei_riita(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 2.0")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_rahat_ei_riita(self):
        kortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 3.0")
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_lataaminen_kasvattaa_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_lataaminen_negativiinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)











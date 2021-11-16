import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
        
    def test_luotu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        
    def test_edullinen_riittaa_kateinen(self):
        vaihto=self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+240)
        self.assertEqual(vaihto,10)
        
    def test_edullinen_ei_riita_kateinen(self):
        vaihto=self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(vaihto,100)
        
    def test_maukas_riittaa_kateinen(self):
        vaihto=self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+400)
        self.assertEqual(vaihto,100)
        
    def test_maukas_ei_riita_kateinen(self):
        vaihto=self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(vaihto,300)
        
    def test_riittaa_kortilla_edullisesti(self):
        kortti=Maksukortti(1000)
        edullisesti=self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(edullisesti,True)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_riittaa_kortilla_maukkaasti(self):
        kortti=Maksukortti(1000)
        maukkaasti=self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(maukkaasti,True)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        
    def test_ei_riita_kortilla_edullisesti(self):
        kortti=Maksukortti(100)
        edullisesti=self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(edullisesti,False)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)  
        
    def test_ei_riita_kortilla_maukkaasti(self):
        kortti=Maksukortti(100)
        maukkaasti=self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(maukkaasti,False)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        
    def test_lattaaminen_toimii(self):
        kortti=Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(kortti,-1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(str(kortti),"saldo: 1.0")
        self.kassapaate.lataa_rahaa_kortille(kortti,1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000+1000)
        self.assertEqual(str(kortti),"saldo: 11.0")
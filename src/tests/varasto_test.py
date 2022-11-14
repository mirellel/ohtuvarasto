import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_ottaminen_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        liikaa=self.varasto.ota_varastosta(12)

        #pitäisi palauttaa kaikki_mita_voidaan eli 10
        self.assertAlmostEqual(liikaa, 10)

    def test_laitetaan_liikaa(self):
        self.varasto.lisaa_varastoon(12)

        #saldon pitäisi olla 10
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_otetaan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(3)
        neg = self.varasto.ota_varastosta(-1)

        #pitäisi palauttaa 0
        self.assertAlmostEqual(neg, 0)

    def test_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-3)

        #pitäisi palauttaa 5
        self.assertAlmostEqual(self.varasto.saldo, 5)
    
    def test_alkutilavuus_negatiivinen(self):
        neg_varasto = Varasto(-2)

        #tilavuuden pitäisi olla 2
        self.assertAlmostEqual(neg_varasto.tilavuus, 2)

    def test_oikea_alkusaldo(self):
        self.varasto2 = Varasto(10, -10)
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_oikea_printti(self):
        self.varasto.lisaa_varastoon(3)
        oikea = f"saldo = 3, vielä tilaa 7"
        self.assertEqual(str(self.varasto), oikea)  
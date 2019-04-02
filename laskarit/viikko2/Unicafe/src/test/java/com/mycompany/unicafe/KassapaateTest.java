package com.mycompany.unicafe;

import static org.hamcrest.CoreMatchers.is;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

public class KassapaateTest {

    Kassapaate kassapaate;
    Maksukortti kortti;

    @Before
    public void setUp() {
        this.kassapaate = new Kassapaate();
        this.kortti = new Maksukortti(1000);
    }

    @Test
    public void aloitusRahaOnOikein() {
        assertThat(kassapaate.kassassaRahaa(), is(100000));
    }

    @Test
    public void alussaMyydytLounaatOnOikein() {
        int lounaitaMyyty = kassapaate.edullisiaLounaitaMyyty()
                + kassapaate.maukkaitaLounaitaMyyty();
        assertThat(lounaitaMyyty, is(0));
    }

    @Test
    public void kateisostoEdullisestiKassanRahaKasvaa() {
        kassapaate.syoEdullisesti(500);
        assertThat(kassapaate.kassassaRahaa(), is(100240));
    }

    @Test
    public void kateisostoEdullisestiVaihtoraha() {
        assertThat(kassapaate.syoEdullisesti(500), is(260));
    }

    @Test
    public void kateisostoEdullisestiLounaidenMaaraKasvaa() {
        kassapaate.syoEdullisesti(500);
        assertThat(kassapaate.edullisiaLounaitaMyyty(), is(1));
    }

    @Test
    public void kateisostoEdullisestiRahaEiRiitaVaihtoraha() {
        assertThat(kassapaate.syoEdullisesti(100), is(100));
    }

    @Test
    public void kateisostoEdullisestiRahaEiRiitaLounaidenMaara() {
        kassapaate.syoEdullisesti(100);
        assertThat(kassapaate.edullisiaLounaitaMyyty(), is(0));
    }

    @Test
    public void kateisostoEdullisestiRahaEiRiitaKassanSaldoEiMuutu() {
        kassapaate.syoEdullisesti(100);
        assertThat(kassapaate.kassassaRahaa(), is(100000));
    }

    @Test
    public void kateisostoMaukkaastiKassanRahaKasvaa() {
        kassapaate.syoMaukkaasti(500);
        assertThat(kassapaate.kassassaRahaa(), is(100400));
    }

    @Test
    public void kateisostoMaukkaastiVaihtoraha() {
        assertThat(kassapaate.syoMaukkaasti(500), is(100));
    }

    @Test
    public void kateisostoMaukkaastiLounaidenMaaraKasvaa() {
        kassapaate.syoMaukkaasti(500);
        assertThat(kassapaate.maukkaitaLounaitaMyyty(), is(1));
    }

    @Test
    public void kateisostoMaukkaastiRahaEiRiitaVaihtoraha() {
        assertThat(kassapaate.syoMaukkaasti(100), is(100));
    }

    @Test
    public void kateisostoMaukkaastiRahaEiRiitaLounaidenMaara() {
        kassapaate.syoMaukkaasti(100);
        assertThat(kassapaate.maukkaitaLounaitaMyyty(), is(0));
    }

    @Test
    public void kateisostoMaukkaastiRahaEiRiitaKassanSaldoEiMuutu() {
        kassapaate.syoMaukkaasti(100);
        assertThat(kassapaate.kassassaRahaa(), is(100000));
    }

    @Test
    public void korttiostoEdullisestiVeloitusToimii() {
        kassapaate.syoEdullisesti(kortti);
        assertThat(kortti.saldo(), is(760));
    }

    @Test
    public void korttiostoEdullisestiPalauttaaTrue() {
        assertThat(kassapaate.syoEdullisesti(kortti), is(true));
    }

    @Test
    public void korttiostoEdullisestiLounaidenMaaraKasvaa() {
        kassapaate.syoEdullisesti(kortti);
        assertThat(kassapaate.edullisiaLounaitaMyyty(), is(1));
    }

    @Test
    public void korttiostoEdullisestiSaldoEiRiitaSaldo() {
        kortti = new Maksukortti(100);
        kassapaate.syoEdullisesti(kortti);
        assertThat(kortti.saldo(), is(100));
    }

    @Test
    public void korttiostoEdullisestiSaldoEiRiitaLounaidenMaara() {
        kortti = new Maksukortti(100);
        kassapaate.syoEdullisesti(kortti);
        assertThat(kassapaate.edullisiaLounaitaMyyty(), is(0));
    }

    @Test
    public void korttiostoEdullisestiSaldoEiRiitaPalautaFalse() {
        kortti = new Maksukortti(100);
        assertThat(kassapaate.syoEdullisesti(kortti), is(false));
    }

    @Test
    public void kortttiostoEdullisestiKassanRahaEiMuutu() {
        kassapaate.syoEdullisesti(kortti);
        assertThat(kassapaate.kassassaRahaa(), is(100000));
    }

    @Test
    public void korttiostoMaukkaastiVeloitusToimii() {
        kassapaate.syoMaukkaasti(kortti);
        assertThat(kortti.saldo(), is(600));
    }

    @Test
    public void korttiostoMaukkaastiPalauttaaTrue() {
        assertThat(kassapaate.syoMaukkaasti(kortti), is(true));
    }

    @Test
    public void korttiostoMaukkaastiLounaidenMaaraKasvaa() {
        kassapaate.syoMaukkaasti(kortti);
        assertThat(kassapaate.maukkaitaLounaitaMyyty(), is(1));
    }

    @Test
    public void korttiostoMaukkaastiSaldoEiRiitaSaldo() {
        kortti = new Maksukortti(100);
        kassapaate.syoMaukkaasti(kortti);
        assertThat(kortti.saldo(), is(100));
    }

    @Test
    public void korttiostoMaukkaastiSaldoEiRiitaLounaidenMaara() {
        kortti = new Maksukortti(100);
        kassapaate.syoMaukkaasti(kortti);
        assertThat(kassapaate.maukkaitaLounaitaMyyty(), is(0));
    }

    @Test
    public void korttiostoMaukkaastiSaldoEiRiitaPalautaFalse() {
        kortti = new Maksukortti(100);
        assertThat(kassapaate.syoMaukkaasti(kortti), is(false));
    }

    @Test
    public void kortttiostoMaukkaastiKassanRahaEiMuutu() {
        kassapaate.syoMaukkaasti(kortti);
        assertThat(kassapaate.kassassaRahaa(), is(100000));
    }

    @Test
    public void kortinLatausKassaRahaKasvaa() {
        kassapaate.lataaRahaaKortille(kortti, 5000);
        assertThat(kassapaate.kassassaRahaa(), is(105000));
    }
    
    @Test
    public void kortinLatausNegatiivinenRaha() {
        kassapaate.lataaRahaaKortille(kortti, -5000);
        assertThat(kassapaate.kassassaRahaa(), is(100000));
    }

}
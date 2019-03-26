package com.mycompany.unicafe;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(10);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertTrue(kortti!=null);      
    }

    @Test
    public void kortinSaldoAlussaOikein() {
        assertEquals("saldo: 0.10", kortti.toString());      
    }
    
    @Test
    public void rahanLataaminenKasvattaaSaldoa() {
        kortti.lataaRahaa(10);
        assertEquals("saldo: 0.20", kortti.toString());      
    }
    
    @Test
    public void saldoVahenneeOikein() {
        kortti.lataaRahaa(20);
        kortti.otaRahaa(10);
        assertEquals("saldo: 0.20", kortti.toString());     
        assertTrue(kortti.otaRahaa(10));      
    }
    
    @Test
    public void saldoEiVaheneJosEiRahaa() {
        kortti.otaRahaa(11);
        assertEquals("saldo: 0.10", kortti.toString());      
        assertFalse(kortti.otaRahaa(11));
    }
}

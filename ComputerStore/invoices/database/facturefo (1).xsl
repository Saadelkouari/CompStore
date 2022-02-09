<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:fo="http://www.w3.org/1999/XSL/Format"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output indent="yes"/> 
    
    <xsl:template match="/facture">
    <fo:root xmlns:fo="http://www.w3.org/1999/XSL/Format">
        
        <fo:layout-master-set>
            <fo:simple-page-master master-name="A4" page-width="210mm"
                page-height="297mm" margin-top="0cm" margin-bottom="0cm"
                margin-left="0cm" margin-right="0cm">
                <!-- Page template goes here -->
                <fo:region-body margin="1cm"/>
                <fo:region-before extent="0cm"/>
                <fo:region-after extent="0cm"/>
                <fo:region-start extent="0cm"/>
                <fo:region-end extent="0cm"/>
                
                
            </fo:simple-page-master>
        </fo:layout-master-set>
        
        <fo:page-sequence master-reference="A4">
            <!-- Page content goes here -->
            <fo:flow flow-name="xsl-region-body" font-family="sans-serif">
                <fo:block font-size="30" text-align="center" font-weight="bold" margin-bottom="30px">Confirmation de facture</fo:block>
                <fo:block font-size="30" text-align="left" font-weight="bold" margin-bottom="10px">Merci pour votre commande</fo:block>
                <fo:block font-size="20" text-align="left" font-weight="bold" margin-bottom="15px">Chere Mme/M  <xsl:value-of select="livraison/recepteur/firstName"/>&#160;<xsl:value-of select="livraison/recepteur/lastName"/>
                    commerce vous remercie pour votre commande.
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    recevrez bientot un email recapulatif de votre commande
                     avec les informations ci-dessous. Veuillez presenter
                     ces informations au moment de la recuperation de votre commande.
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Nº de commande : <xsl:value-of select="@id"/>
                </fo:block>
                <fo:block font-size="30" text-align="left" font-weight="bold" margin-bottom="20px">Composition de votre commande</fo:block>
                <fo:table margin-bottom="20px" >
                    
                        <fo:table-column column-width="200pt"/>
                    <fo:table-column column-width="proportional-column-width(50)"/>
                    <fo:table-column column-width="proportional-column-width(50)"/>
                    <fo:table-column column-width="proportional-column-width(50)"/>
                    
                    <fo:table-header width="100%" table-layout="fixed">
                        <fo:table-row>
                            <fo:table-cell border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                <fo:block font-weight="bold">ARTICLES</fo:block>
                            </fo:table-cell>
                            <fo:table-cell border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                <fo:block font-weight="bold" >QUANTITE</fo:block>
                            </fo:table-cell>
                            <fo:table-cell border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                <fo:block font-weight="bold" >PRIX UNITAIRE</fo:block>
                            </fo:table-cell>
                            <fo:table-cell border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                <fo:block font-weight="bold" >SOUS TOTAL</fo:block>
                            </fo:table-cell>
                        </fo:table-row>
                    </fo:table-header>
                            
                            <fo:table-body width="100%" table-layout="fixed" >
                                <xsl:for-each select="commande/computer">
                            <fo:table-row>
                                <fo:table-cell  border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                    <fo:block><xsl:value-of select="manufacturer"/>&#160;<xsl:value-of select="series"/>&#160;<xsl:value-of select="model"/></fo:block>
                                </fo:table-cell>
                                <fo:table-cell  border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                    <fo:block><xsl:value-of select="qte"/></fo:block>
                                </fo:table-cell>
                                <fo:table-cell  border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                    <fo:block><xsl:value-of select="price"/> DH</fo:block>
                                </fo:table-cell>
                                <fo:table-cell  border="1" text-align="left" padding-top=".5mm" padding-bottom=".5mm">
                                    <fo:block><xsl:value-of select="total"/> DH</fo:block>
                                </fo:table-cell>
                            </fo:table-row>
                                </xsl:for-each>
                            </fo:table-body>
                </fo:table>
                <fo:block font-size="30" text-align="left" font-weight="bold" margin-bottom="20px">Vos informations client</fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Norm et Prenom  : Mme/M <xsl:value-of select="livraison/recepteur/firstName"/>&#160;<xsl:value-of select="livraison/recepteur/lastName"/>
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Adresse : <xsl:value-of select="livraison/adresse"/>
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Email  : <xsl:value-of select="livraison/recepteur/email"/>
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Tel : <xsl:value-of select="livraison/recepteur/phone"/>
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px" font-style="italic">
                    Presentation de la CIN est obligatoire pour la recuperation de la commande
                </fo:block>
                <fo:block font-size="30" text-align="left" font-weight="bold" margin-bottom="20px">Mode de livraison : Livraison a domicile</fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Adresse de Livraison : <xsl:value-of select="livraison/adresse"/>
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Tel : <xsl:value-of select="livraison/recepteur/phone"/>
                </fo:block>
                <fo:block font-size="30" text-align="left" font-weight="bold" margin-bottom="20px">Mode de paiement: Paiement en ligne par carte bancaire</fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Date de reglement : <xsl:value-of select="dateFacturation"/>
                </fo:block>
                <fo:block font-size="20" text-align="left" margin-bottom="20px">
                    Date de reglement : <xsl:value-of select="livraison/dateLivraison"/>
                </fo:block>
                <fo:block font-size="30" text-align="left" font-weight="bold" margin-bottom="20px">Total de la commande : <xsl:value-of select="commande/total"/> DH</fo:block>
                
                
                
            </fo:flow>
        </fo:page-sequence>
    </fo:root>
    </xsl:template>
</xsl:stylesheet>

<xsl:stylesheet version = "1.0" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/facture">
<html>
    <body>
        <h1>Merci pour votre commande</h1>
        <h2>Chere Mme/M  <xsl:value-of select="livraison/recepteur/firstName"/>&#160;<xsl:value-of select="livraison/recepteur/lastName"/>
            commerce vous remercie pour votre commande.</h2>
        <p>recevrez bientot un email recapulatif de votre commande
            <br/> avec les informations ci-dessous. Veuillez presenter
            <br/> ces informations au moment de la recuperation de votre commande.
        </p>
        <p>Nº de commande : <xsl:value-of select="@id"/></p>
        <h1>Composition de votre commande</h1>
        <table border="1">
            <th>ARTICLES</th>
            <th>QUANTITE</th>
            <th>PRIX UNITAIRE</th>
            <th>SOUS TOTAL</th>
            <xsl:for-each select="commande/computer">
             <tr>
                 <td><xsl:value-of select="manufacturer"/>&#160;<xsl:value-of select="series"/>&#160;<xsl:value-of select="manufacturer"/>&#160;<xsl:value-of select="model"/></td>
            <td><xsl:value-of select="qte"/></td>
            <td><xsl:value-of select="price"/>  DH</td>
            <td><xsl:value-of select="total"/>  DH</td>
             </tr>
            </xsl:for-each>
        </table>
        <br/>
         <h1>Vos informations client</h1>
        <p><strong>Norm et Prenom  : </strong>Mme/M <xsl:value-of select="livraison/recepteur/firstName"/>&#160;<xsl:value-of select="livraison/recepteur/lastName"/></p>
        <p><strong>Adresse : </strong><xsl:value-of select="livraison/adresse"/></p>
        <p><strong>Email : </strong><xsl:value-of select="livraison/recepteur/email"/></p>
        <p><strong>Numero de tel  : </strong><xsl:value-of select="livraison/recepteur/phone"/></p>
         <i>Presentation de la CIN est obligatoire pour la recuperation de la commande</i>
         <br/>
         
         <h1>Mode de livraison : Livraison a domicile</h1>
        <p><strong>Adresse de Livraison : </strong><xsl:value-of select="livraison/adresse"/></p>
        <p><strong>Tel : </strong><xsl:value-of select="livraison/recepteur/phone"/>  </p>


         <h1>Mode de paiement: Paiement en ligne par carte bancaire</h1>
        <p><strong>Date de reglement :  </strong><xsl:value-of select="dateFacturation"/></p>
        <p><strong>Date de livraison :  </strong><xsl:value-of select="livraison/dateLivraison"/></p>
         <h1>Total de la commande : <xsl:value-of select="commande/total"/>  DH</h1>

    </body>
</html>

</xsl:template>


</xsl:stylesheet>
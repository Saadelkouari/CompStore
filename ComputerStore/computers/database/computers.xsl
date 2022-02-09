<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:fo="http://www.w3.org/1999/XSL/Format" exclude-result-prefixes="xs" version="2.0">
<xsl:template match="fo:table-row">
   <fo:table-cell border="solid 0.1mm black"><xsl:applay-templates/></fo:table-cell>
</xsl:template>      
<xsl:template match="/">
        <fo:root>
            <fo:layout-master-set>
                <fo:simple-page-master master-name="A4" page-width="7.5in" page-height="10in" margin-top="0.5in" margin-bottom="0.5in" margin-left="0.5in" margin-right="0.5in">
                    <fo:region-body />

                </fo:simple-page-master>
            </fo:layout-master-set>

            <fo:page-sequence master-reference="A4">
  
                <fo:flow flow-name="xsl-region-body" font="9pt Helvatica">
                    <fo:block>

                    <xsl:for-each select="/computers/computer">
                        <xsl:sort select="price" />
                        <fo:block margin="0.5in">
                            <fo:inline-container inline-progression-dimension="40.9%">
                                <fo:block>
                                    <fo:external-graphic src="{image}" content-height="scale-to-fit" content-width="scale-to-fit" height="2.00in" width="2.00in" />
                                </fo:block>
                            </fo:inline-container>
                            <fo:inline-container inline-progression-dimension="40.9%">
                                <fo:block>
                                    <fo:table content-height="scale-to-fit" height="2.00in" width="2.00in">
                                        <fo:table-body>
                                            <xsl:for-each select="*[not(*)]">
                                                <xsl:if test="not(name()='image')">
                                                    <fo:table-row>
                                                        <fo:table-cell border="solid 0.1mm black">
                                                            <fo:block>
                                                                <xsl:value-of select="name()" />
                                                            </fo:block>
                                                        </fo:table-cell >
                                                        <fo:table-cell border="solid 0.1mm black">
                                                            <fo:block>
                                                                <xsl:value-of select="text()" />
                                                            </fo:block>
                                                        </fo:table-cell>
                                                    </fo:table-row>
                                                </xsl:if>
                                            </xsl:for-each>
                                        </fo:table-body>
                                    </fo:table>
                                </fo:block>

                            </fo:inline-container>
                            <xsl:for-each select="*[*]">
                            <fo:block>
                                <fo:table>
                                    <fo:table-body><fo:table-row><fo:table-cell border="solid 0.1mm black"><fo:block font-weight="bold"><xsl:value-of select="name()"/></fo:block></fo:table-cell></fo:table-row>
                                    
                                    <xsl:for-each select="*">
                                        
                                            <fo:table-row><fo:table-cell border="solid 0.1mm black"> <fo:block><xsl:value-of select="name()"/></fo:block></fo:table-cell>
                                           <fo:table-cell border="solid 0.1mm black"><fo:block><xsl:value-of select="text()"/></fo:block></fo:table-cell></fo:table-row>
                                            
                                    </xsl:for-each>
                                </fo:table-body>
                                </fo:table>
                            </fo:block>
                        </xsl:for-each>
                        </fo:block>
                    </xsl:for-each>
                    </fo:block>
                </fo:flow>
            </fo:page-sequence>
        </fo:root>
    </xsl:template>



</xsl:stylesheet>
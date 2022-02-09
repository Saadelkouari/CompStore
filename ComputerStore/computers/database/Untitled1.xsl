<?xml version='1.0'?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
	
	<xsl:for-each select="computers/computer">
	<main style="max-width=1200px;margin=0 auto;padding=15px;display=flex;">
	<div style="width=65% margin-top=60px;display=inline-block;">
    <img style="width=250px;position:relative;left=0;right=0;top=0;" src="{image}"></img>
	<table>
	<xsl:for-each select="*[not(*)]">
	<xsl:if test="not(name()='image')">
	<tr>
    <th><xsl:value-of select="name()"/></th><td><xsl:value-of select="text()"/></td>
	</tr>
	</xsl:if>
 	</xsl:for-each>
	</table>
	</div>
	<div style="width=60%;position=relative;">

	<div style="margin-bottom=30px;">

 <div style="display=inline-block; margin-top=10px;">
 	<span>Couleur: <xsl:value-of select="colour"/></span>
   			
            <span style="margin-left=10px;width=20px; hight=20px;= 50%;background-color={colour}"/>
            

      
        </div>


	</div>
	</div>
	</main>
	</xsl:for-each>
	
</html>
</xsl:template>


</xsl:stylesheet><!-- Stylus Studio meta-information - (c) 2004-2009. Progress Software Corporation. All rights reserved.

<metaInformation>
	<scenarios>
		<scenario default="yes" name="Scenari" userelativepaths="yes" externalpreview="no" url="computers.xml" htmlbaseurl="" outputurl="" processortype="saxon8" useresolver="yes" profilemode="0" profiledepth="" profilelength="" urlprofilexml=""
		          commandline="" additionalpath="" additionalclasspath="" postprocessortype="none" postprocesscommandline="" postprocessadditionalpath="" postprocessgeneratedext="" validateoutput="no" validator="internal" customvalidator="">
			<advancedProp name="bSchemaAware" value="true"/>
			<advancedProp name="xsltVersion" value="2.0"/>
			<advancedProp name="schemaCache" value="||"/>
			<advancedProp name="iWhitespace" value="0"/>
			<advancedProp name="bWarnings" value="true"/>
			<advancedProp name="bXml11" value="false"/>
			<advancedProp name="bUseDTD" value="false"/>
			<advancedProp name="bXsltOneIsOkay" value="true"/>
			<advancedProp name="bTinyTree" value="true"/>
			<advancedProp name="bGenerateByteCode" value="true"/>
			<advancedProp name="bExtensions" value="true"/>
			<advancedProp name="iValidation" value="0"/>
			<advancedProp name="iErrorHandling" value="fatal"/>
			<advancedProp name="sInitialTemplate" value=""/>
			<advancedProp name="sInitialMode" value=""/>
		</scenario>
	</scenarios>
	<MapperMetaTag>
		<MapperInfo srcSchemaPathIsRelative="yes" srcSchemaInterpretAsXML="no" destSchemaPath="" destSchemaRoot="" destSchemaPathIsRelative="yes" destSchemaInterpretAsXML="no">
			<SourceSchema srcSchemaPath="computers.xml" srcSchemaRoot="computers" AssociatedInstance="" loaderFunction="document" loaderFunctionUsesURI="no"/>
		</MapperInfo>
		<MapperBlockPosition>
			<template match="/"></template>
		</MapperBlockPosition>
		<TemplateContext></TemplateContext>
		<MapperFilter side="source"></MapperFilter>
	</MapperMetaTag>
</metaInformation>
-->
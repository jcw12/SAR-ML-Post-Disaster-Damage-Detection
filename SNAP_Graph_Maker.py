# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 14:02:28 2024

@author: user
"""

def Stacks(SLCs,Outputs, Swaths, outpath, msg=True):
    SLC1, SLC2, SLC3 = SLCs
    St1, St2 = Outputs
    Img1, Img2, Img3 = Swaths
    Img1 = [str(item) for item in Img1]
    Img2 = [str(item) for item in Img2]
    Img3 = [str(item) for item in Img3]
    IWImg1, MinImg1, MaxImg1 = Img1
    IWImg2, MinImg2, MaxImg2 = Img2
    IWImg3, MinImg3, MaxImg3 = Img3
    XML = """
    <graph id="Graph">
  <version>1.0</version>
  <node id="Read">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC1+"""</file>
      <copyMetadata>true</copyMetadata>
      <bandNames/>
      <pixelRegion>0,0,69023,15079</pixelRegion>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(2)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC2+"""</file>
      <copyMetadata>true</copyMetadata>
      <bandNames/>
      <pixelRegion>0,0,69586,15089</pixelRegion>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(3)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC3+"""</file>
      <copyMetadata>true</copyMetadata>
      <bandNames/>
      <pixelRegion>0,0,69024,15079</pixelRegion>
      <maskNames/>
    </parameters>
  </node>
  <node id="TOPSAR-Split">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW"""+IWImg1+"""</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>"""+MinImg1+"""</firstBurstIndex>
      <lastBurstIndex>"""+MaxImg1+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="TOPSAR-Split(2)">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW"""+IWImg2+"""</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>"""+MinImg2+"""</firstBurstIndex>
      <lastBurstIndex>"""+MaxImg2+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="TOPSAR-Split(3)">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW"""+IWImg3+"""</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>"""+MinImg3+"""</firstBurstIndex>
      <lastBurstIndex>"""+MaxImg3+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="Apply-Orbit-File">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Apply-Orbit-File(2)">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Apply-Orbit-File(3)">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Back-Geocoding">
    <operator>Back-Geocoding</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
      <sourceProduct.1 refid="Apply-Orbit-File(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <demName>SRTM 1Sec HGT</demName>
      <demResamplingMethod>BICUBIC_INTERPOLATION</demResamplingMethod>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <resamplingType>BISINC_5_POINT_INTERPOLATION</resamplingType>
      <maskOutAreaWithoutElevation>false</maskOutAreaWithoutElevation>
      <outputRangeAzimuthOffset>false</outputRangeAzimuthOffset>
      <outputDerampDemodPhase>false</outputDerampDemodPhase>
      <disableReramp>false</disableReramp>
    </parameters>
  </node>
  <node id="Enhanced-Spectral-Diversity">
    <operator>Enhanced-Spectral-Diversity</operator>
    <sources>
      <sourceProduct refid="Back-Geocoding"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <fineWinWidthStr>512</fineWinWidthStr>
      <fineWinHeightStr>512</fineWinHeightStr>
      <fineWinAccAzimuth>16</fineWinAccAzimuth>
      <fineWinAccRange>16</fineWinAccRange>
      <fineWinOversampling>128</fineWinOversampling>
      <xCorrThreshold>0.1</xCorrThreshold>
      <cohThreshold>0.3</cohThreshold>
      <numBlocksPerOverlap>10</numBlocksPerOverlap>
      <esdEstimator>Periodogram</esdEstimator>
      <weightFunc>Inv Quadratic</weightFunc>
      <temporalBaselineType>Number of images</temporalBaselineType>
      <maxTemporalBaseline>4</maxTemporalBaseline>
      <integrationMethod>L1 and L2</integrationMethod>
      <doNotWriteTargetBands>false</doNotWriteTargetBands>
      <useSuppliedRangeShift>false</useSuppliedRangeShift>
      <overallRangeShift>0.0</overallRangeShift>
      <useSuppliedAzimuthShift>false</useSuppliedAzimuthShift>
      <overallAzimuthShift>0.0</overallAzimuthShift>
    </parameters>
  </node>
  <node id="Back-Geocoding(2)">
    <operator>Back-Geocoding</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
      <sourceProduct.1 refid="Apply-Orbit-File(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <demName>SRTM 1Sec HGT</demName>
      <demResamplingMethod>BICUBIC_INTERPOLATION</demResamplingMethod>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <resamplingType>BISINC_5_POINT_INTERPOLATION</resamplingType>
      <maskOutAreaWithoutElevation>false</maskOutAreaWithoutElevation>
      <outputRangeAzimuthOffset>false</outputRangeAzimuthOffset>
      <outputDerampDemodPhase>false</outputDerampDemodPhase>
      <disableReramp>false</disableReramp>
    </parameters>
  </node>
  <node id="Enhanced-Spectral-Diversity(2)">
    <operator>Enhanced-Spectral-Diversity</operator>
    <sources>
      <sourceProduct refid="Back-Geocoding(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <fineWinWidthStr>512</fineWinWidthStr>
      <fineWinHeightStr>512</fineWinHeightStr>
      <fineWinAccAzimuth>16</fineWinAccAzimuth>
      <fineWinAccRange>16</fineWinAccRange>
      <fineWinOversampling>128</fineWinOversampling>
      <xCorrThreshold>0.1</xCorrThreshold>
      <cohThreshold>0.3</cohThreshold>
      <numBlocksPerOverlap>10</numBlocksPerOverlap>
      <esdEstimator>Periodogram</esdEstimator>
      <weightFunc>Inv Quadratic</weightFunc>
      <temporalBaselineType>Number of images</temporalBaselineType>
      <maxTemporalBaseline>4</maxTemporalBaseline>
      <integrationMethod>L1 and L2</integrationMethod>
      <doNotWriteTargetBands>false</doNotWriteTargetBands>
      <useSuppliedRangeShift>false</useSuppliedRangeShift>
      <overallRangeShift>0.0</overallRangeShift>
      <useSuppliedAzimuthShift>false</useSuppliedAzimuthShift>
      <overallAzimuthShift>0.0</overallAzimuthShift>
    </parameters>
  </node>
  <node id="Write(2)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Enhanced-Spectral-Diversity(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+St1+"""</file>
      <formatName>BEAM-DIMAP</formatName>
    </parameters>
  </node>
  <node id="Write">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Enhanced-Spectral-Diversity"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+St2+"""</file>
      <formatName>BEAM-DIMAP</formatName>
    </parameters>
  </node>
  <applicationData id="Presentation">
    <Description/>
    <node id="Read">
      <displayPosition x="183.0" y="197.0"/>
    </node>
    <node id="Read(2)">
      <displayPosition x="183.0" y="248.0"/>
    </node>
    <node id="Read(3)">
      <displayPosition x="182.0" y="299.0"/>
    </node>
    <node id="TOPSAR-Split">
      <displayPosition x="290.0" y="182.0"/>
    </node>
    <node id="TOPSAR-Split(2)">
      <displayPosition x="276.0" y="248.0"/>
    </node>
    <node id="TOPSAR-Split(3)">
      <displayPosition x="274.0" y="303.0"/>
    </node>
    <node id="Apply-Orbit-File">
      <displayPosition x="425.0" y="180.0"/>
    </node>
    <node id="Apply-Orbit-File(2)">
      <displayPosition x="419.0" y="248.0"/>
    </node>
    <node id="Apply-Orbit-File(3)">
      <displayPosition x="423.0" y="302.0"/>
    </node>
    <node id="Back-Geocoding">
      <displayPosition x="573.0" y="210.0"/>
    </node>
    <node id="Enhanced-Spectral-Diversity">
      <displayPosition x="706.0" y="202.0"/>
    </node>
    <node id="Back-Geocoding(2)">
      <displayPosition x="570.0" y="281.0"/>
    </node>
    <node id="Enhanced-Spectral-Diversity(2)">
      <displayPosition x="709.0" y="304.0"/>
    </node>
    <node id="Write(2)">
      <displayPosition x="954.0" y="299.0"/>
    </node>
    <node id="Write">
      <displayPosition x="952.0" y="200.0"/>
    </node>
  </applicationData>
</graph>
    """
    with open(outpath, 'w') as file:
        file.write(XML)
    if msg==True:     
        print('Graph File written to:',outpath)

def SttoCoh(Stacks, Outputs, outpath, msg=True):
    St1, St2 = Stacks
    Coh1, Coh2 = Outputs
    
    XML = """
    <graph id="Graph">
  <version>1.0</version>
  <node id="Read">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+St1+"""</file>
      <formatName>BEAM-DIMAP</formatName>
      <copyMetadata>true</copyMetadata>
      <bandNames/>
      <pixelRegion>0,0,20612,8940</pixelRegion>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(2)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+St2+"""</file>
      <formatName>BEAM-DIMAP</formatName>
      <copyMetadata>true</copyMetadata>
      <bandNames/>
      <pixelRegion>0,0,20612,8940</pixelRegion>
      <maskNames/>
    </parameters>
  </node>
  <node id="Coherence">
    <operator>Coherence</operator>
    <sources>
      <sourceProduct refid="Read"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <cohWinAz>3</cohWinAz>
      <cohWinRg>10</cohWinRg>
      <subtractFlatEarthPhase>true</subtractFlatEarthPhase>
      <srpPolynomialDegree>5</srpPolynomialDegree>
      <srpNumberPoints>501</srpNumberPoints>
      <orbitDegree>3</orbitDegree>
      <squarePixel>true</squarePixel>
      <subtractTopographicPhase>true</subtractTopographicPhase>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <tileExtensionPercent>100</tileExtensionPercent>
      <singleMaster>true</singleMaster>
    </parameters>
  </node>
  <node id="Coherence(2)">
    <operator>Coherence</operator>
    <sources>
      <sourceProduct refid="Read(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <cohWinAz>3</cohWinAz>
      <cohWinRg>10</cohWinRg>
      <subtractFlatEarthPhase>true</subtractFlatEarthPhase>
      <srpPolynomialDegree>5</srpPolynomialDegree>
      <srpNumberPoints>501</srpNumberPoints>
      <orbitDegree>3</orbitDegree>
      <squarePixel>true</squarePixel>
      <subtractTopographicPhase>true</subtractTopographicPhase>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <tileExtensionPercent>100</tileExtensionPercent>
      <singleMaster>true</singleMaster>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Coherence"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst(2)">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Coherence(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="Terrain-Correction">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.00832</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2583887960837173E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Terrain-Correction(2)">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.00832</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2583887960837173E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Write(2)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Coh2+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <node id="Write">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Coh1+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <applicationData id="Presentation">
    <Description/>
    <node id="Read">
            <displayPosition x="37.0" y="134.0"/>
    </node>
    <node id="Read(2)">
      <displayPosition x="36.0" y="202.0"/>
    </node>
    <node id="Coherence">
      <displayPosition x="128.0" y="136.0"/>
    </node>
    <node id="Coherence(2)">
      <displayPosition x="130.0" y="204.0"/>
    </node>
    <node id="TOPSAR-Deburst">
      <displayPosition x="259.0" y="130.0"/>
    </node>
    <node id="TOPSAR-Deburst(2)">
      <displayPosition x="263.0" y="209.0"/>
    </node>
    <node id="Terrain-Correction">
      <displayPosition x="408.0" y="133.0"/>
    </node>
    <node id="Terrain-Correction(2)">
      <displayPosition x="416.0" y="213.0"/>
    </node>
    <node id="Write(2)">
      <displayPosition x="623.0" y="209.0"/>
    </node>
    <node id="Write">
            <displayPosition x="594.0" y="132.0"/>
    </node>
  </applicationData>
</graph>
    """
    with open(outpath, 'w') as file:
        file.write(XML)
    if msg==True:     
        print('Graph File written to:',outpath)


def Intensity(SLCs,Outputs, Swaths, outpath, msg=True):
    SLC1, SLC2 = SLCs
    Int2, Int1 = Outputs
    Img1, Img2 = Swaths
    Img1 = [str(item) for item in Img1]
    Img2 = [str(item) for item in Img2]
    IWImg1, MinImg1, MaxImg1 = Img1
    IWImg2, MinImg2, MaxImg2 = Img2
    
    XML = """
    <graph id="Graph">
  <version>1.0</version>
  <node id="Read">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC1+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,69035,15070</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(2)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC2+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,68788,15060</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="TOPSAR-Split">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW"""+IWImg1+"""</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>"""+MinImg1+"""</firstBurstIndex>
      <lastBurstIndex>"""+MaxImg2+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="TOPSAR-Split(2)">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW"""+IWImg2+"""</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>"""+MinImg2+"""</firstBurstIndex>
      <lastBurstIndex>"""+MaxImg2+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="Apply-Orbit-File">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Apply-Orbit-File(2)">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Calibration">
    <operator>Calibration</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
      <outputImageInComplex>false</outputImageInComplex>
      <outputImageScaleInDb>false</outputImageScaleInDb>
      <createGammaBand>false</createGammaBand>
      <createBetaBand>false</createBetaBand>
      <selectedPolarisations/>
      <outputSigmaBand>true</outputSigmaBand>
      <outputGammaBand>false</outputGammaBand>
      <outputBetaBand>false</outputBetaBand>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst(3)">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Calibration"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="Multilook">
    <operator>Multilook</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <nRgLooks>3</nRgLooks>
      <nAzLooks>1</nAzLooks>
      <outputIntensity>true</outputIntensity>
      <grSquarePixel>true</grSquarePixel>
    </parameters>
  </node>
  <node id="LinearToFromdB">
    <operator>LinearToFromdB</operator>
    <sources>
      <sourceProduct refid="Multilook"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
    </parameters>
  </node>
  <node id="Calibration(2)">
    <operator>Calibration</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
      <outputImageInComplex>false</outputImageInComplex>
      <outputImageScaleInDb>false</outputImageScaleInDb>
      <createGammaBand>false</createGammaBand>
      <createBetaBand>false</createBetaBand>
      <selectedPolarisations/>
      <outputSigmaBand>true</outputSigmaBand>
      <outputGammaBand>false</outputGammaBand>
      <outputBetaBand>false</outputBetaBand>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst(4)">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Calibration(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="Multilook(2)">
    <operator>Multilook</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst(4)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <nRgLooks>3</nRgLooks>
      <nAzLooks>1</nAzLooks>
      <outputIntensity>true</outputIntensity>
      <grSquarePixel>true</grSquarePixel>
    </parameters>
  </node>
  <node id="LinearToFromdB(2)">
    <operator>LinearToFromdB</operator>
    <sources>
      <sourceProduct refid="Multilook(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
    </parameters>
  </node>
  <node id="Terrain-Correction(3)">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="LinearToFromdB"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Terrain-Correction(4)">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="LinearToFromdB(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Write(3)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Int1+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <node id="Write(4)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction(4)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Int2+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <applicationData id="Presentation">
    <Description/>
    <node id="Read">
      <displayPosition x="183.0" y="197.0"/>
    </node>
    <node id="Read(2)">
      <displayPosition x="183.0" y="248.0"/>
    </node>
    <node id="TOPSAR-Split">
      <displayPosition x="290.0" y="182.0"/>
    </node>
    <node id="TOPSAR-Split(2)">
      <displayPosition x="276.0" y="248.0"/>
    </node>
    <node id="Apply-Orbit-File">
      <displayPosition x="425.0" y="180.0"/>
    </node>
    <node id="Apply-Orbit-File(2)">
      <displayPosition x="419.0" y="248.0"/>
    </node>
    <node id="Calibration">
      <displayPosition x="597.0" y="182.0"/>
    </node>
    <node id="TOPSAR-Deburst(3)">
      <displayPosition x="719.0" y="181.0"/>
    </node>
    <node id="Multilook">
      <displayPosition x="888.0" y="181.0"/>
    </node>
    <node id="LinearToFromdB">
      <displayPosition x="995.0" y="181.0"/>
    </node>
    <node id="Calibration(2)">
      <displayPosition x="601.0" y="253.0"/>
    </node>
    <node id="TOPSAR-Deburst(4)">
      <displayPosition x="722.0" y="253.0"/>
    </node>
    <node id="Multilook(2)">
      <displayPosition x="886.0" y="254.0"/>
    </node>
    <node id="LinearToFromdB(2)">
      <displayPosition x="993.0" y="254.0"/>
    </node>
    <node id="Terrain-Correction(3)">
      <displayPosition x="1140.0" y="181.0"/>
    </node>
    <node id="Terrain-Correction(4)">
      <displayPosition x="1141.0" y="253.0"/>
    </node>
    <node id="Write(3)">
      <displayPosition x="1320.0" y="183.0"/>
    </node>
    <node id="Write(4)">
      <displayPosition x="1322.0" y="256.0"/>
    </node>
  </applicationData>
</graph>
    """
    
    with open(outpath, 'w') as file:
        file.write(XML)
    if msg==True:     
        print('Graph File written to:',outpath)
    
def Coherence(SLCs,Outputs, Swaths, outpath, msg=True):
    SLC1, SLC2, SLC3 = SLCs
    Coh1, Coh2 = Outputs
    Sw1, Sw2 = str(2), str(7)
    XML = """
    <graph id="Graph">
  <version>1.0</version>
  <node id="Read">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC1+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,69035,15070</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(2)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC2+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,68788,15060</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(3)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC3+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,69037,15070</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="TOPSAR-Split">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW1</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>"""+Sw1+"""</firstBurstIndex>
      <lastBurstIndex>"""+Sw2+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="TOPSAR-Split(2)">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW1</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>"""+Sw1+"""</firstBurstIndex>
      <lastBurstIndex>"""+Sw2+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="TOPSAR-Split(3)">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW1</subswath>
      <selectedPolarisations/>
      <firstBurstIndex>"""+Sw1+"""</firstBurstIndex>
      <lastBurstIndex>"""+Sw2+"""</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="Apply-Orbit-File">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Apply-Orbit-File(2)">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Apply-Orbit-File(3)">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Back-Geocoding">
    <operator>Back-Geocoding</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
      <sourceProduct.1 refid="Apply-Orbit-File(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <demName>SRTM 1Sec HGT</demName>
      <demResamplingMethod>BICUBIC_INTERPOLATION</demResamplingMethod>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <resamplingType>BISINC_5_POINT_INTERPOLATION</resamplingType>
      <maskOutAreaWithoutElevation>false</maskOutAreaWithoutElevation>
      <outputRangeAzimuthOffset>false</outputRangeAzimuthOffset>
      <outputDerampDemodPhase>false</outputDerampDemodPhase>
      <disableReramp>false</disableReramp>
    </parameters>
  </node>
  <node id="Enhanced-Spectral-Diversity">
    <operator>Enhanced-Spectral-Diversity</operator>
    <sources>
      <sourceProduct refid="Back-Geocoding"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <fineWinWidthStr>512</fineWinWidthStr>
      <fineWinHeightStr>512</fineWinHeightStr>
      <fineWinAccAzimuth>16</fineWinAccAzimuth>
      <fineWinAccRange>16</fineWinAccRange>
      <fineWinOversampling>128</fineWinOversampling>
      <xCorrThreshold>0.1</xCorrThreshold>
      <cohThreshold>0.3</cohThreshold>
      <numBlocksPerOverlap>10</numBlocksPerOverlap>
      <esdEstimator>Periodogram</esdEstimator>
      <weightFunc>Inv Quadratic</weightFunc>
      <temporalBaselineType>Number of images</temporalBaselineType>
      <maxTemporalBaseline>4</maxTemporalBaseline>
      <integrationMethod>L1 and L2</integrationMethod>
      <doNotWriteTargetBands>false</doNotWriteTargetBands>
      <useSuppliedRangeShift>false</useSuppliedRangeShift>
      <overallRangeShift>0.0</overallRangeShift>
      <useSuppliedAzimuthShift>false</useSuppliedAzimuthShift>
      <overallAzimuthShift>0.0</overallAzimuthShift>
    </parameters>
  </node>
  <node id="Back-Geocoding(2)">
    <operator>Back-Geocoding</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
      <sourceProduct.1 refid="Apply-Orbit-File(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <demName>SRTM 1Sec HGT</demName>
      <demResamplingMethod>BICUBIC_INTERPOLATION</demResamplingMethod>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <resamplingType>BISINC_5_POINT_INTERPOLATION</resamplingType>
      <maskOutAreaWithoutElevation>false</maskOutAreaWithoutElevation>
      <outputRangeAzimuthOffset>false</outputRangeAzimuthOffset>
      <outputDerampDemodPhase>false</outputDerampDemodPhase>
      <disableReramp>false</disableReramp>
    </parameters>
  </node>
  <node id="Enhanced-Spectral-Diversity(2)">
    <operator>Enhanced-Spectral-Diversity</operator>
    <sources>
      <sourceProduct refid="Back-Geocoding(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <fineWinWidthStr>512</fineWinWidthStr>
      <fineWinHeightStr>512</fineWinHeightStr>
      <fineWinAccAzimuth>16</fineWinAccAzimuth>
      <fineWinAccRange>16</fineWinAccRange>
      <fineWinOversampling>128</fineWinOversampling>
      <xCorrThreshold>0.1</xCorrThreshold>
      <cohThreshold>0.3</cohThreshold>
      <numBlocksPerOverlap>10</numBlocksPerOverlap>
      <esdEstimator>Periodogram</esdEstimator>
      <weightFunc>Inv Quadratic</weightFunc>
      <temporalBaselineType>Number of images</temporalBaselineType>
      <maxTemporalBaseline>4</maxTemporalBaseline>
      <integrationMethod>L1 and L2</integrationMethod>
      <doNotWriteTargetBands>false</doNotWriteTargetBands>
      <useSuppliedRangeShift>false</useSuppliedRangeShift>
      <overallRangeShift>0.0</overallRangeShift>
      <useSuppliedAzimuthShift>false</useSuppliedAzimuthShift>
      <overallAzimuthShift>0.0</overallAzimuthShift>
    </parameters>
  </node>
  <node id="Coherence">
    <operator>Coherence</operator>
    <sources>
      <sourceProduct refid="Enhanced-Spectral-Diversity"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <cohWinAz>3</cohWinAz>
      <cohWinRg>10</cohWinRg>
      <subtractFlatEarthPhase>true</subtractFlatEarthPhase>
      <srpPolynomialDegree>5</srpPolynomialDegree>
      <srpNumberPoints>501</srpNumberPoints>
      <orbitDegree>3</orbitDegree>
      <squarePixel>true</squarePixel>
      <subtractTopographicPhase>true</subtractTopographicPhase>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <tileExtensionPercent>100</tileExtensionPercent>
      <singleMaster>true</singleMaster>
    </parameters>
  </node>
  <node id="Coherence(2)">
    <operator>Coherence</operator>
    <sources>
      <sourceProduct refid="Enhanced-Spectral-Diversity(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <cohWinAz>3</cohWinAz>
      <cohWinRg>10</cohWinRg>
      <subtractFlatEarthPhase>true</subtractFlatEarthPhase>
      <srpPolynomialDegree>5</srpPolynomialDegree>
      <srpNumberPoints>501</srpNumberPoints>
      <orbitDegree>3</orbitDegree>
      <squarePixel>true</squarePixel>
      <subtractTopographicPhase>true</subtractTopographicPhase>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <tileExtensionPercent>100</tileExtensionPercent>
      <singleMaster>true</singleMaster>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Coherence"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst(2)">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Coherence(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="Terrain-Correction">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Terrain-Correction(2)">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Write">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Coh1+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <node id="Write(2)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Coh2+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <applicationData id="Presentation">
    <Description/>
    <node id="Read">
      <displayPosition x="183.0" y="197.0"/>
    </node>
    <node id="Read(2)">
      <displayPosition x="183.0" y="248.0"/>
    </node>
    <node id="Read(3)">
      <displayPosition x="182.0" y="299.0"/>
    </node>
    <node id="TOPSAR-Split">
      <displayPosition x="290.0" y="182.0"/>
    </node>
    <node id="TOPSAR-Split(2)">
      <displayPosition x="276.0" y="248.0"/>
    </node>
    <node id="TOPSAR-Split(3)">
      <displayPosition x="274.0" y="303.0"/>
    </node>
    <node id="Apply-Orbit-File">
      <displayPosition x="425.0" y="180.0"/>
    </node>
    <node id="Apply-Orbit-File(2)">
      <displayPosition x="419.0" y="248.0"/>
    </node>
    <node id="Apply-Orbit-File(3)">
      <displayPosition x="423.0" y="302.0"/>
    </node>
    <node id="Back-Geocoding">
      <displayPosition x="573.0" y="210.0"/>
    </node>
    <node id="Enhanced-Spectral-Diversity">
      <displayPosition x="706.0" y="202.0"/>
    </node>
    <node id="Back-Geocoding(2)">
      <displayPosition x="570.0" y="281.0"/>
    </node>
    <node id="Enhanced-Spectral-Diversity(2)">
      <displayPosition x="709.0" y="304.0"/>
    </node>
    <node id="Write(2)">
      <displayPosition x="1352.0" y="313.0"/>
    </node>
    <node id="Coherence">
      <displayPosition x="936.0" y="202.0"/>
    </node>
    <node id="Coherence(2)">
      <displayPosition x="923.0" y="305.0"/>
    </node>
    <node id="TOPSAR-Deburst">
      <displayPosition x="1029.0" y="207.0"/>
    </node>
    <node id="TOPSAR-Deburst(2)">
      <displayPosition x="1035.0" y="309.0"/>
    </node>
    <node id="Terrain-Correction">
      <displayPosition x="1173.0" y="213.0"/>
    </node>
    <node id="Terrain-Correction(2)">
      <displayPosition x="1194.0" y="310.0"/>
    </node>
    <node id="Write">
      <displayPosition x="1326.0" y="210.0"/>
    </node>
  </applicationData>
</graph>
    """
    
    with open(outpath, 'w') as file:
        file.write(XML)
    if msg==True:     
        print('Graph File written to:',outpath)



#While this is theoretically more efficient, it ran out of memory and froze on my laptop.
def Coherence_and_Intensity(SLCs,Outputs, Swaths, outpath, msg=True):
    SLC1, SLC2, SLC3 = SLCs
    Coh1, Coh2, Int1, Int2 = Outputs
    Swath1, Swath2 = Swaths
    
    XML = """
<graph id="Graph">
  <version>1.0</version>
  <node id="Read">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC1+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,69035,15070</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(2)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC2+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,68788,15060</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="Read(3)">
    <operator>Read</operator>
    <sources/>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <useAdvancedOptions>false</useAdvancedOptions>
      <file>"""+SLC3+"""</file>
      <copyMetadata>true</copyMetadata>
      <pixelRegion>0,0,69037,15070</pixelRegion>
      <bandNames/>
      <maskNames/>
    </parameters>
  </node>
  <node id="TOPSAR-Split">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW1</subswath>
      <selectedPolarisations/>
      <firstBurstIndex>2</firstBurstIndex>
      <lastBurstIndex>7</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="TOPSAR-Split(2)">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW1</subswath>
      <selectedPolarisations>VV</selectedPolarisations>
      <firstBurstIndex>2</firstBurstIndex>
      <lastBurstIndex>7</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="TOPSAR-Split(3)">
    <operator>TOPSAR-Split</operator>
    <sources>
      <sourceProduct refid="Read(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <subswath>IW1</subswath>
      <selectedPolarisations/>
      <firstBurstIndex>2</firstBurstIndex>
      <lastBurstIndex>7</lastBurstIndex>
      <wktAoi/>
    </parameters>
  </node>
  <node id="Apply-Orbit-File">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Apply-Orbit-File(2)">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Apply-Orbit-File(3)">
    <operator>Apply-Orbit-File</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Split(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <orbitType>Sentinel Precise (Auto Download)</orbitType>
      <polyDegree>3</polyDegree>
      <continueOnFail>false</continueOnFail>
    </parameters>
  </node>
  <node id="Back-Geocoding">
    <operator>Back-Geocoding</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
      <sourceProduct.1 refid="Apply-Orbit-File(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <demName>SRTM 1Sec HGT</demName>
      <demResamplingMethod>BICUBIC_INTERPOLATION</demResamplingMethod>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <resamplingType>BISINC_5_POINT_INTERPOLATION</resamplingType>
      <maskOutAreaWithoutElevation>false</maskOutAreaWithoutElevation>
      <outputRangeAzimuthOffset>false</outputRangeAzimuthOffset>
      <outputDerampDemodPhase>false</outputDerampDemodPhase>
      <disableReramp>false</disableReramp>
    </parameters>
  </node>
  <node id="Enhanced-Spectral-Diversity">
    <operator>Enhanced-Spectral-Diversity</operator>
    <sources>
      <sourceProduct refid="Back-Geocoding"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <fineWinWidthStr>512</fineWinWidthStr>
      <fineWinHeightStr>512</fineWinHeightStr>
      <fineWinAccAzimuth>16</fineWinAccAzimuth>
      <fineWinAccRange>16</fineWinAccRange>
      <fineWinOversampling>128</fineWinOversampling>
      <xCorrThreshold>0.1</xCorrThreshold>
      <cohThreshold>0.3</cohThreshold>
      <numBlocksPerOverlap>10</numBlocksPerOverlap>
      <esdEstimator>Periodogram</esdEstimator>
      <weightFunc>Inv Quadratic</weightFunc>
      <temporalBaselineType>Number of images</temporalBaselineType>
      <maxTemporalBaseline>4</maxTemporalBaseline>
      <integrationMethod>L1 and L2</integrationMethod>
      <doNotWriteTargetBands>false</doNotWriteTargetBands>
      <useSuppliedRangeShift>false</useSuppliedRangeShift>
      <overallRangeShift>0.0</overallRangeShift>
      <useSuppliedAzimuthShift>false</useSuppliedAzimuthShift>
      <overallAzimuthShift>0.0</overallAzimuthShift>
    </parameters>
  </node>
  <node id="Back-Geocoding(2)">
    <operator>Back-Geocoding</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
      <sourceProduct.1 refid="Apply-Orbit-File(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <demName>SRTM 1Sec HGT</demName>
      <demResamplingMethod>BICUBIC_INTERPOLATION</demResamplingMethod>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <resamplingType>BISINC_5_POINT_INTERPOLATION</resamplingType>
      <maskOutAreaWithoutElevation>false</maskOutAreaWithoutElevation>
      <outputRangeAzimuthOffset>false</outputRangeAzimuthOffset>
      <outputDerampDemodPhase>false</outputDerampDemodPhase>
      <disableReramp>false</disableReramp>
    </parameters>
  </node>
  <node id="Enhanced-Spectral-Diversity(2)">
    <operator>Enhanced-Spectral-Diversity</operator>
    <sources>
      <sourceProduct refid="Back-Geocoding(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <fineWinWidthStr>512</fineWinWidthStr>
      <fineWinHeightStr>512</fineWinHeightStr>
      <fineWinAccAzimuth>16</fineWinAccAzimuth>
      <fineWinAccRange>16</fineWinAccRange>
      <fineWinOversampling>128</fineWinOversampling>
      <xCorrThreshold>0.1</xCorrThreshold>
      <cohThreshold>0.3</cohThreshold>
      <numBlocksPerOverlap>10</numBlocksPerOverlap>
      <esdEstimator>Periodogram</esdEstimator>
      <weightFunc>Inv Quadratic</weightFunc>
      <temporalBaselineType>Number of images</temporalBaselineType>
      <maxTemporalBaseline>4</maxTemporalBaseline>
      <integrationMethod>L1 and L2</integrationMethod>
      <doNotWriteTargetBands>false</doNotWriteTargetBands>
      <useSuppliedRangeShift>false</useSuppliedRangeShift>
      <overallRangeShift>0.0</overallRangeShift>
      <useSuppliedAzimuthShift>false</useSuppliedAzimuthShift>
      <overallAzimuthShift>0.0</overallAzimuthShift>
    </parameters>
  </node>
  <node id="Write(2)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Coh2+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <node id="Coherence">
    <operator>Coherence</operator>
    <sources>
      <sourceProduct refid="Enhanced-Spectral-Diversity"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <cohWinAz>3</cohWinAz>
      <cohWinRg>10</cohWinRg>
      <subtractFlatEarthPhase>true</subtractFlatEarthPhase>
      <srpPolynomialDegree>5</srpPolynomialDegree>
      <srpNumberPoints>501</srpNumberPoints>
      <orbitDegree>3</orbitDegree>
      <squarePixel>true</squarePixel>
      <subtractTopographicPhase>true</subtractTopographicPhase>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <tileExtensionPercent>100</tileExtensionPercent>
      <singleMaster>true</singleMaster>
    </parameters>
  </node>
  <node id="Coherence(2)">
    <operator>Coherence</operator>
    <sources>
      <sourceProduct refid="Enhanced-Spectral-Diversity(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <cohWinAz>3</cohWinAz>
      <cohWinRg>10</cohWinRg>
      <subtractFlatEarthPhase>true</subtractFlatEarthPhase>
      <srpPolynomialDegree>5</srpPolynomialDegree>
      <srpNumberPoints>501</srpNumberPoints>
      <orbitDegree>3</orbitDegree>
      <squarePixel>true</squarePixel>
      <subtractTopographicPhase>true</subtractTopographicPhase>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <tileExtensionPercent>100</tileExtensionPercent>
      <singleMaster>true</singleMaster>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Coherence"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst(2)">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Coherence(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="Terrain-Correction">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Terrain-Correction(2)">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Calibration">
    <operator>Calibration</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
      <outputImageInComplex>false</outputImageInComplex>
      <outputImageScaleInDb>false</outputImageScaleInDb>
      <createGammaBand>false</createGammaBand>
      <createBetaBand>false</createBetaBand>
      <selectedPolarisations/>
      <outputSigmaBand>true</outputSigmaBand>
      <outputGammaBand>false</outputGammaBand>
      <outputBetaBand>false</outputBetaBand>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst(3)">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Calibration"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="Multilook">
    <operator>Multilook</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <nRgLooks>3</nRgLooks>
      <nAzLooks>1</nAzLooks>
      <outputIntensity>true</outputIntensity>
      <grSquarePixel>true</grSquarePixel>
    </parameters>
  </node>
  <node id="LinearToFromdB">
    <operator>LinearToFromdB</operator>
    <sources>
      <sourceProduct refid="Multilook"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
    </parameters>
  </node>
  <node id="Calibration(2)">
    <operator>Calibration</operator>
    <sources>
      <sourceProduct refid="Apply-Orbit-File(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
      <outputImageInComplex>false</outputImageInComplex>
      <outputImageScaleInDb>false</outputImageScaleInDb>
      <createGammaBand>false</createGammaBand>
      <createBetaBand>false</createBetaBand>
      <selectedPolarisations/>
      <outputSigmaBand>true</outputSigmaBand>
      <outputGammaBand>false</outputGammaBand>
      <outputBetaBand>false</outputBetaBand>
    </parameters>
  </node>
  <node id="TOPSAR-Deburst(4)">
    <operator>TOPSAR-Deburst</operator>
    <sources>
      <sourceProduct refid="Calibration(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <selectedPolarisations/>
    </parameters>
  </node>
  <node id="Multilook(2)">
    <operator>Multilook</operator>
    <sources>
      <sourceProduct refid="TOPSAR-Deburst(4)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <nRgLooks>3</nRgLooks>
      <nAzLooks>1</nAzLooks>
      <outputIntensity>true</outputIntensity>
      <grSquarePixel>true</grSquarePixel>
    </parameters>
  </node>
  <node id="LinearToFromdB(2)">
    <operator>LinearToFromdB</operator>
    <sources>
      <sourceProduct refid="Multilook(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
    </parameters>
  </node>
  <node id="Terrain-Correction(3)">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="LinearToFromdB"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Terrain-Correction(4)">
    <operator>Terrain-Correction</operator>
    <sources>
      <sourceProduct refid="LinearToFromdB(2)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <sourceBands/>
      <demName>SRTM 1Sec HGT</demName>
      <externalDEMFile/>
      <externalDEMNoDataValue>0.0</externalDEMNoDataValue>
      <externalDEMApplyEGM>true</externalDEMApplyEGM>
      <demResamplingMethod>BILINEAR_INTERPOLATION</demResamplingMethod>
      <imgResamplingMethod>BILINEAR_INTERPOLATION</imgResamplingMethod>
      <pixelSpacingInMeter>14.01</pixelSpacingInMeter>
      <pixelSpacingInDegree>1.2585397130514497E-4</pixelSpacingInDegree>
      <mapProjection>GEOGCS[&quot;WGS84(DD)&quot;, &#xd;
  DATUM[&quot;WGS84&quot;, &#xd;
    SPHEROID[&quot;WGS84&quot;, 6378137.0, 298.257223563]], &#xd;
  PRIMEM[&quot;Greenwich&quot;, 0.0], &#xd;
  UNIT[&quot;degree&quot;, 0.017453292519943295], &#xd;
  AXIS[&quot;Geodetic longitude&quot;, EAST], &#xd;
  AXIS[&quot;Geodetic latitude&quot;, NORTH]]</mapProjection>
      <alignToStandardGrid>false</alignToStandardGrid>
      <standardGridOriginX>0.0</standardGridOriginX>
      <standardGridOriginY>0.0</standardGridOriginY>
      <nodataValueAtSea>false</nodataValueAtSea>
      <saveDEM>false</saveDEM>
      <saveLatLon>false</saveLatLon>
      <saveIncidenceAngleFromEllipsoid>false</saveIncidenceAngleFromEllipsoid>
      <saveLocalIncidenceAngle>false</saveLocalIncidenceAngle>
      <saveProjectedLocalIncidenceAngle>false</saveProjectedLocalIncidenceAngle>
      <saveSelectedSourceBand>true</saveSelectedSourceBand>
      <saveLayoverShadowMask>false</saveLayoverShadowMask>
      <outputComplex>false</outputComplex>
      <applyRadiometricNormalization>false</applyRadiometricNormalization>
      <saveSigmaNought>false</saveSigmaNought>
      <saveGammaNought>false</saveGammaNought>
      <saveBetaNought>false</saveBetaNought>
      <incidenceAngleForSigma0>Use projected local incidence angle from DEM</incidenceAngleForSigma0>
      <incidenceAngleForGamma0>Use projected local incidence angle from DEM</incidenceAngleForGamma0>
      <auxFile>Latest Auxiliary File</auxFile>
      <externalAuxFile/>
    </parameters>
  </node>
  <node id="Write(3)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction(3)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Int1+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <node id="Write(4)">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction(4)"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Int2+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <node id="Write">
    <operator>Write</operator>
    <sources>
      <sourceProduct refid="Terrain-Correction"/>
    </sources>
    <parameters class="com.bc.ceres.binding.dom.XppDomElement">
      <file>"""+Coh1+"""</file>
      <formatName>GeoTIFF</formatName>
    </parameters>
  </node>
  <applicationData id="Presentation">
    <Description/>
    <node id="Read">
      <displayPosition x="183.0" y="197.0"/>
    </node>
    <node id="Read(2)">
      <displayPosition x="183.0" y="248.0"/>
    </node>
    <node id="Read(3)">
      <displayPosition x="182.0" y="299.0"/>
    </node>
    <node id="TOPSAR-Split">
      <displayPosition x="290.0" y="182.0"/>
    </node>
    <node id="TOPSAR-Split(2)">
      <displayPosition x="276.0" y="248.0"/>
    </node>
    <node id="TOPSAR-Split(3)">
      <displayPosition x="274.0" y="303.0"/>
    </node>
    <node id="Apply-Orbit-File">
      <displayPosition x="425.0" y="180.0"/>
    </node>
    <node id="Apply-Orbit-File(2)">
      <displayPosition x="419.0" y="248.0"/>
    </node>
    <node id="Apply-Orbit-File(3)">
      <displayPosition x="423.0" y="302.0"/>
    </node>
    <node id="Back-Geocoding">
      <displayPosition x="573.0" y="210.0"/>
    </node>
    <node id="Enhanced-Spectral-Diversity">
      <displayPosition x="706.0" y="202.0"/>
    </node>
    <node id="Back-Geocoding(2)">
      <displayPosition x="570.0" y="281.0"/>
    </node>
    <node id="Enhanced-Spectral-Diversity(2)">
      <displayPosition x="709.0" y="304.0"/>
    </node>
    <node id="Write(2)">
      <displayPosition x="1352.0" y="313.0"/>
    </node>
    <node id="Coherence">
      <displayPosition x="936.0" y="202.0"/>
    </node>
    <node id="Coherence(2)">
      <displayPosition x="923.0" y="305.0"/>
    </node>
    <node id="TOPSAR-Deburst">
      <displayPosition x="1029.0" y="207.0"/>
    </node>
    <node id="TOPSAR-Deburst(2)">
      <displayPosition x="1035.0" y="309.0"/>
    </node>
    <node id="Terrain-Correction">
      <displayPosition x="1173.0" y="213.0"/>
    </node>
    <node id="Terrain-Correction(2)">
      <displayPosition x="1194.0" y="310.0"/>
    </node>
    <node id="Calibration">
      <displayPosition x="603.0" y="392.0"/>
    </node>
    <node id="TOPSAR-Deburst(3)">
      <displayPosition x="705.0" y="398.0"/>
    </node>
    <node id="Multilook">
      <displayPosition x="869.0" y="399.0"/>
    </node>
    <node id="LinearToFromdB">
      <displayPosition x="961.0" y="399.0"/>
    </node>
    <node id="Calibration(2)">
      <displayPosition x="594.0" y="456.0"/>
    </node>
    <node id="TOPSAR-Deburst(4)">
      <displayPosition x="710.0" y="462.0"/>
    </node>
    <node id="Multilook(2)">
      <displayPosition x="870.0" y="464.0"/>
    </node>
    <node id="LinearToFromdB(2)">
      <displayPosition x="970.0" y="466.0"/>
    </node>
    <node id="Terrain-Correction(3)">
      <displayPosition x="1137.0" y="399.0"/>
    </node>
    <node id="Terrain-Correction(4)">
      <displayPosition x="1154.0" y="475.0"/>
    </node>
    <node id="Write(3)">
      <displayPosition x="1376.0" y="414.0"/>
    </node>
    <node id="Write(4)">
      <displayPosition x="1388.0" y="488.0"/>
    </node>
    <node id="Write">
      <displayPosition x="1326.0" y="210.0"/>
    </node>
  </applicationData>
</graph>
    """
    with open(outpath, 'w') as file:
        file.write(XML)
    if msg==True:     
        print('Graph File written to:',outpath)
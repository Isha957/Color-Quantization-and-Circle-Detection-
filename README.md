# Color-Quantization-and-Circle-Detection-
Computer Vision Assignment on Color Quantization using K-means and Circle Detection using Hough Transform
<html>
<head>
<html>
<body>
       
<p style="font-family:times" >
<h2>The focus of the Repository:</h2><br>
This Repository contains a code solutions along with a Report for a Computer Vision Assignment for two problems:
<ul>
<li><b><i>Quantization of Color Space using K-means Clustering:</i></b></li>
<li><b><i>Implementation of Hough Transform Circle Detector:</i></b></li>
</ol>

<h2>Problem - 1: COLOR QUANTIZATION:</h2><br>
<p><b>Given Image:</b></p>
<img src = "" style="width:300px;height:200px";></img><br>
<ul>
<li><i>Quantize a 3-dimensional RGB image and map pixels to its nearest k-means center</i></li>
<li><i>Converting a 3-dimensional RGB image into a HSVand quantize the 1-dimensional hue space</i></li>
<li><i>Compute the SSD error between RGB image pixels and quantized pixels for both RGB and HSV space</i></li>
<li><i>Displaying the histograms of hue values with equally spaced bins and bins defined by K cluster centers</i></li>


<h2>Problem - 2: CIRCLE DETECTION</h2><br>
<p><b>Given Image:</b></p>
<img src = "" style="width:300px;height:200px";></img><br>
<ul>
<li><i>Implementing a hough transform Circle Detector that takes an input image and fixed radius and returns centers of any detected circles.</i></li>
<li><i>The output centers is a NX2 matrix in which each row lists (x,y) position of the detected circles' center</i></li>
<li><i>Displaying the Hough Transform accumulator array</i></li>
<li><i>Experimenting on how to determine the number of circlepresent by post-processing the accumulator array</i></li>
<li><i>Describing the impact of the vote space quantization(bin size)/i></li>

<h2>Repository Files:</h2><br>
<b>Code Implementation:</b><br> 
<ul>
<li><b><i>ColorQuantize.py - main code that calls the other helper functions</i></b></li>
       <ul>
              <li>computeQuantizationerror.py - SSD error between quantized and original pixels</li>
              <li>quantizeHSV.py - converts RGB image to HSV and quantize 1-D Hue space </li>
              <li>quantizeRGB.py - quantizes 3D RGB image with K-means</li>
       </ul>
<li><b><i>detectCircles.py - code implementation for CircleDetection</i></b></li> 
       </ul>
<b>Image png files:</b><br> 
       <ul>
              <li>Image 1 - fish.png </li>
              <li>Image 2 - jupiter.png</li>
       </ul>
<b>Report</b><br> 
       
<p>Using the Sentinel-2 Image Collection band data: Bands - B4 (Red) ; B8  (NIR) and the above formula, we obtain max NDVI values for each image. The NDVI tif        images are extracted  at 10m resolution.We generate these values every two weeks between the date range and export these images into a tiff file. These files can be accessed in Python using Geopandas/Rasterio and can be visualized.</p><br>
<img src = "https://github.com/Isha957/yield_forecasting/blob/master/images/NDVI_img.png" style="width:300px;height:200px";></img><br>

<li><b><i>Extraction of GCVI time series data:</i></b></li>
<p>Using the Sentinel-2 Image Collection band data: Bands - B3 (Green) ; B8  (NIR) and the above formula, we obtain max GCVI values for each image. The GCVI        tif images are extracted  at 10m resolution.We generate these values every two weeks between the date range and export these images into a tiff file. These files can be accessed in Python using Geopandas/Rasterio and can be visualized.</ul><br>
<img src = "https://github.com/Isha957/yield_forecasting/blob/master/images/gcvi%20image.png" style="width:300px;height:200px";></img><br>
<img src = "https://github.com/Isha957/yield_forecasting/blob/master/images/monthly%20NDVI%20.png" style="width:500px;height:300px";></img><br>

<h2><u>Building the Regional Model:</u></h2>
Machine Learning using PyspatialML and Scikit-learn
With the python library Pyspatialml, scikit-learn machine learning models can be applied to raster-based datasets. Here we used monthly maximum NDVI rasters extracted from the GEE products as bands with the tsraster library as input features. The target data, field-scale yield values, were in a shapefile format that could be overlaid on the rasters to extract corresponding feature raster values to create the training data set. Pyspatialml also includes methods to plot the results and modify rasters.
<br>
<img src ="https://github.com/Isha957/yield_forecasting/blob/master/Cropmaskvisualization.png" alt = "Applying Cross Mask" style="width:600px;height:400px";></img>

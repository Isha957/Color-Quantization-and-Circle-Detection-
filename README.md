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

<h1>Problem - 1: COLOR QUANTIZATION:</h1><hr>
<p><b>Given Image:</b></p>
<img src = "https://github.com/Isha957/Color-Quantization-and-Circle-Detection-/blob/main/fish.jpg" style="width:300px;height:200px";></img><br>
<ul>
<li><i>Quantize a 3-dimensional RGB image and map pixels to its nearest k-means center</i></li>
<li><i>Converting a 3-dimensional RGB image into a HSVand quantize the 1-dimensional hue space</i></li>
<li><i>Compute the SSD error between RGB image pixels and quantized pixels for both RGB and HSV space</i></li>
<li><i>Displaying the histograms of hue values with equally spaced bins and bins defined by K cluster centers</i></li>

<h2>Results<h2>
       <p><u>RGB Quantized<u></p>
       <img src = "" style="width:300px;height:200px";></img><br>
              
       <p><u>HSV Quantized<u></p>
       <img src = "" style="width:300px;height:200px";></img><br>
  
       <p><u>Histograms<u></p>
       <img src = "" style="width:300px;height:200px";></img><br>
       <img src = "" style="width:300px;height:200px";></img><br>
       
       <p><u>SSD Error<u></p>
       <img src = "" style="width:300px;height:200px";></img><br>
           
<br>
       
<h1>Problem - 2: CIRCLE DETECTION</h1><hr>
<p><b>Given Image:</b></p>
<img src = "https://github.com/Isha957/Color-Quantization-and-Circle-Detection-/blob/main/jupiter.jpg" style="width:300px;height:200px";></img><br>
<ul>
<li><i>Implementing a hough transform Circle Detector that takes an input image and fixed radius and returns centers of any detected circles.</i></li>
<li><i>The output centers is a NX2 matrix in which each row lists (x,y) position of the detected circles' center</i></li>
<li><i>Displaying the Hough Transform accumulator array</i></li>
<li><i>Experimenting on how to determine the number of circlepresent by post-processing the accumulator array</i></li>
<li><i>Describing the impact of the vote space quantization(bin size)/i></li>
       </ul>
       
 <h2>Results<h2>
       <p><u>Detection Radius =10 and accumulator array<u></p>
       <img src = "" style="width:300px;height:200px";></img><br>
              
       <p><u>Detection Radius =30 and accumulator array<u></p>
       <img src = "" style="width:300px;height:200px";></img><br>
  
       <p><u>Detection Radius =100 and accumulator array<u></p>
       <img src = "" style="width:300px;height:200px";></img><br>
       
<h2>Repository Files:</h2><br>
       <b><u>Code Implementation:</u></b><br> 
<ul>
<li><b>ColorQuantize.py - main code that calls the other helper functions</b></li>
       <ul>
              <li>computeQuantizationerror.py - SSD error between quantized and original pixels</li>
              <li>quantizeHSV.py - converts RGB image to HSV and quantize 1-D Hue space </li>
              <li>quantizeRGB.py - quantizes 3D RGB image with K-means</li>
       </ul>
<li><b>detectCircles.py - code implementation for CircleDetection</b></li> 
       </ul>
       <b><u>Image png files:</u></b><br> 
       <ul>
              <li>Image 1 - fish.png </li>
              <li>Image 2 - jupiter.png</li>
       </ul>
       <b><u>Report</u></b><br> 
       
       
       
       
       
   </body>
 </head>
<html>

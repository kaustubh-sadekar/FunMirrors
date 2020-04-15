# FunMirrors
This is a fun project I created to motivate computer vision enthusiasts and to highlight the importance of understanding fundamental concepts related to image formation in a camera.

I developed this fun project as an application of the following concepts:
* Camera projection matrix
* Camera intrinsic and extrinsic parameters
* Image remapping

Main objective of this project is to explain above mentioned fundamental concepts in an interesting and fun way. 
A detailed explaination the above fundamental concepts can be found at [this blog from learnopencv.com](https://www.learnopencv.com/geometry-of-image-formation/)

I will explain the basics of above topics first and then I will explain how I combined all the concepts together.Before that let's have a look at some fun results!!

|![](/gifs/mirror1.gif)|![](/gifs/mirror2.gif)|
|--|--|
|![](/gifs/mirror3.gif)|![](/gifs/mirror4.gif)|
|--|--|
|![](/gifs/mirror5.gif)|![](/gifs/mirror6.gif)|
|--|--|

The implimentation of virtual camera tha I am using is explained in [this repository](https://github.com/kaustubh-sadekar/VirtualCam) It explains how you can change different camera parameters to generate various effects. These two projects aim towards motivating computer vision enthusiasts to study fundamenta concepts related to image formation and camera projection.
 
### [Virtual camera class](https://github.com/kaustubh-sadekar/VirtualCam) is used to create all the different types of mirrors. The virtual camera repository also contains a GUI which helps you to modify all the camera parameters and visually understand effect of each parameter on the final generated image.

## Understanding camera projection matrix
Camera projection matrix (P) provides a mapping between a 3D world coordinate and its corresponding pixel coordinate in an image captured by the respective camera. It is dependent on **intrinsic** and **extrinsic** parameters of a camera.

**Intrinsic camera parameters**:
Internal properties of a camera that do not change when translating or rotating the camera in the 3D world coordinate frame.
* Focal length (depends on the lens used and mechanical arrangement of camera)
* Apperent pixel size (size if one pixel on the image sensor array)
* Pricipal point offset (principal point : intersection of the image plane and its normal)

**Extrinsic camera parameters**:
External camera properties that are dependent on the camera pose.
* Camera rotation (rotation of camera in the 3D world along all the three axis)
* Camera translation (translation of camera in the 3D world)

Derivation of the camera projection matrix is explained in the following image.
<p align="left">
  <img width="850" src="/theory1.jpg">
</p>
<p align="left">
  <img width="550" src="/theory2.png">
</p>

## Creating mirror surfaces using numpy
I have used np.meshgrid to create the entire plane surface in 3D. Some of the planes used are shown below
Mirror using a gaussian function           |  Inverted mirror using an inverted gaussian function  
:-------------------------:|:-------------------------:
![](/Mirror1.png)  |  ![](/Mirror2.png)

## Projecting these surfaces using the camera projection matrix
Now as explained in the camera projection matrix section we can use the projection matrix to project any 3D point in the image. Using numpy functions and concepts of matrix multiplication we apply the projection matrix to the entire 3D surface. 

Mirror using a gaussian function           |  Projection of the grid in virtual camera  
:-------------------------:|:-------------------------:
![](/Mirror1.png)  |  ![](/mesh_projection.png) 


## Image remapping
In image remapping we basically try to change the pixel location. Using mappings U and V we get the new location of x and y coordinates for a given pixel, originally at (x,y) location. Thus we get x_new = U(x,y) and y_new = V(x,y). OpenCV provides a very easy to use method, `remap`. We need to pass the image, and the x and y map i.e. U and V respectively in the above definition. The function basically returns output such that the pixel values at (x,y) in the original image are mapped to (x_new,y_new). This is called forward mapping. To avoid holes we find the inverse mapping such that (x,y) in the original image is determined as `x,y = U_inv(x_new,y_new) , V_inv(x_new,y_new)`.


## Using the projection of the plane as a remapping function and apply remapping the the image to generate different effects
Now we know all the building blocks of this project :
* How to create a virtual camera using numpy and concepts of camera projection
* How to create a 3D plane to be used as out mirror
* How to project the 3D plane in our virtual camera and get the mapping function for remapping the image
* How to use a given map and apply remapping on an image
Following figures show how the mirror is used to generate different effects.

Mirror using a gaussian function           |  Projection of the grid in virtual camera | Effect on remapped image   
:-------------------------:|:-------------------------:|:------------------------------------------:
![](/Mirror1.png)  |  ![](/mesh_projection.png)   | ![](/image_output.png)


## Usage
To run the example code use the following command :
```shell
python3 Example1.py`
```
 



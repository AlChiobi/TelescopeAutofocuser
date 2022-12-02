# :telescope: Autofocuser Telescope :telescope:

## How to use :thought_balloon:


1. Setup the telescope and aim it at the desired celestial object of interest.
2. Connect peripheral devices (mouse, keyboard, external monitor via HDMI) to Raspberry Pi
3. Turn on device by flipping switch on the power supply battery
4. Open terminal, navigate to the directory the GUI is in, and initiate the GUI by entering the command 
    > python3 ProjectGUI.py

    4.1 Once the GUI is open, you should see a screen with a graphic displaying "Telescope Autofocuser" as well as options to Autofocus, Capture Image, Optimize Image, Load Image, and Exit.

5. Assuming the telescope has already been aimed and assembled (with the camera cap on the lens) select the autofocus option.
6. Once the autofocus has completed you can then choose to capture the image which will save the image in the local directory.
7. The user also has the option to optimize the captured image as well as load a previously captured image.
8. If another image is desired begin again at step 5
---

## GUI navigation :dizzy:

### Autofocus Telescope
 > Rotates focuser from maximum to minimum position whiel scanning camera into an image array and Identifies the most focused image in array and adjusts foccuser to be at the optimal position for 
### Image Capture
 > Outputs the most focused image. 
### Capture Image
> User inputs desired file name for a soon to be captured immage, once capturee image is seleccted the camera captures and saves the user named file into local directory 
### Optimize Image
> Inputs File throgh user input or directory browse, returns optimized image into optimized file directory 
### Load Image
> Usere inputts disered file name or directory browse and returns image in a preview window.
Exit 
> Allows user to exit application and terminates any running processes in the app.
---
## [DEMO](https://drive.google.com/drive/u/2/folders/1jnSVn6v47KhGNe5WC25DCf7vLacj2Xek) :tv:

---

## About the Project & Parts :hammer:

* **Telescope**
    - [Apertura 6" f/5 Newtonian OTA - 6F5N](https://www.highpointscientific.com/apertura-6inch-f5-znewtonian-ota-6f5n)

* **Lenses**
    - [Neewer 1.25, F=25mm](https://neewer.com/products/neewer-telescope-lens-25mm-eyepiece-lens-66600754)
    - [Celestron Omni Plossl Eye Piece 1 1/4" 6mm](https://www.amazon.com/Celestron-Omni-1-1-4MM-Eyepiece/dp/B00008Y0S5)

* **Miscilaneous 3D Printed Parts**
    - Gear assembly
    - Motor Mount
    - Raspbeerrry Pi Mount
    - Motor Driver Mount
    -PCB Mount
    -Camera/Lens Mount

* **Raspberry Pi 4B**
    - Raspbeerry Pi OS (64-bit)

* [Celestron Logic Drive](https://www.celestron.com/products/astromaster-powerseeker-motor-drive?utm_source=google&utm_medium=cse&utm_term=93514&utm_content=googleshopping&srsltid=AYJSbAdMVUhHId1mwYoYiMoD2PBH6iV7o8ICmLMGriiWhZf1vKMkKVP0RbQ)

* [Buck Converter](https://www.ebay.com/itm/394297609006?chn=ps&_trkparms=ispr%3D1&amdata=enc%3A1mepjF5xnSUS0ZFiZP71iMw53&norover=1&mkevt=1&mkrid=711-117182-37290-0&mkcid=2&mkscid=101&itemid=394297609006&targetid=1644837434763&device=c&mktype=&googleloc=9027906&poi=&campaignid=16743749222&mkgroupid=138744546207&rlsatarget=pla-1644837434763&abcId=9300842&merchantid=508428421&gclid=Cj0KCQiAvqGcBhCJARIsAFQ5ke5Y1CjlE7Hhc9hPl1-v4KN0wqMU_bkXXzrv5P9vUXxZY37ULt5LHZcaAoOXEALw_wcB)

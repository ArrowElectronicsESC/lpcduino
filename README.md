# LPCduino -- Arduino for the LPC!
Soure code for LPCduino v0.2

***Finally***, Arduino is here for the LPC family!

This is an initial stage of development for Arduino-like environment for the LPC family, this source has it for the LPC812.

We have implemented the following environment with the aid of the following sources:

1. [Build Your Own Arduino Like Board For Just a Few Dollars](https://www.youtube.com/watch?v=4PMj8LfR2m8)
2. [Adafruit's LPC810 CodeBase](https://github.com/microbuilder/LPC810_CodeBase)

Essentially, the hardware components needed for this are found in the number 1, but here you can find them listed:

1. [USB to Serial FTDI](https://www.amazon.com.mx/dp/B00IJXZQ7C?tag=aamx88-20&keywords=fdti&geniuslink=true)
2. [PCB Adapters](https://www.amazon.com.mx/piezas-7value-placa-TSSOP-SOT23/dp/B09P174D5X/ref=sr_1_1?geniuslink=true&keywords=SOP+to+DIP&qid=1653582388&sr=8-1)
3. [LPC812M101JDH20FP](https://www.mouser.com/ProductDetail/NXP-Semiconductors/LPC812M101JDH20FP?qs=WQO6Kzcwo2GnIeUM20H1Mw%3D%3D)
4. LEDs, resistors and pushbuttons (for debugging and testing purposes)

![test board](https://github.com/BrunoSenzioSavinoArrow/lpcduino/blob/main/images/board.png "Test Setup Example")

## Features:

- Signature reading
- Compilation and verification
- GPIO programming (additional libraries and wrappers to come...)

## Requirements:

1. Install ARM-GCC tools for your PC, you can follow point 6 from the following [guide](https://github.com/BrunoSenzioSavinoArrow/lpcduino/blob/main/Getting%20Started%20with%20MCUXpresso%20SDK.pdf)
2. Download and install [FlashMagic Programming Tool for NXP Semiconductors](https://www.flashmagictool.com/download.html)
3. Add the Flashmagic Tool to the Environment variables (PATH)
4. Make sure ARM-GCC also works for your environment
5. Python 3.8 or higher

## Getting started:

1. Install *Tkinter* in your python environment
```python
pip install tk
```
2. In the **lpcduino.py** file, change the compile and flash paths to your desired route

Run **lpcduino.py** and enjoy!

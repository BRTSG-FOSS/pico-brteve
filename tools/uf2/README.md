# UF2 Converter for EVE

## Introduction
This tool helps you to program eve-connected flash with user specified file through the USB interface of Pico.
Before you do anything, please download a customized bootloader(`eve_flash_pico.uf2`) to the RAM of Pico and a new USB drive(`BTEVE-FLASH`) will appear. 

BTW, the customized bootloader assumes the following SPI connection between Eve and Pico: 

#### CS - GP5,  CLK - GP2,  MOSI - GP3, MISO - GP4

Then you need convert your flash image into UF2 format file by running this tool.  Drag and drop the converted 
UF2 file to the new USB drive and wait for the end of programming!


## Prerequirements

```
python -m pip install tqdm
```

## Usage Examples

### Upload the default firmware to your device

```
python uf2conv4eve.py --firmware
```

#### Output

```
Including default EVE3 firmware blob
Including default EVE4 firmware blob
Converting to uf2, output size: 16384
Launching D: (RPI-RP2)
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 120/120 [00:00<00:00, 862.53kB/s]
Wrote 122368 bytes to D:/NEW.UF2
Flashing D: (BT816-RP2040-v1.0)
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 16/16 [00:00<00:00, 262.06kB/s]
Wrote 16384 bytes to D:/NEW.UF2
```

### Upload a specified firmware blob together with your assets

```
python uf2conv4eve.py --firmware BT815 BT815-unified.blob --input __Flash.bin
```

#### Output

```
Including EVE3 firmware blob BT815-unified.blob
Converting to uf2, output size: 33554432
Launching D: (RPI-RP2)
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 120/120 [00:00<00:00, 856.37kB/s]
Wrote 122368 bytes to D:/NEW.UF2
Flashing D: (BT816-RP2040-v1.0)
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████| 32768/32768 [03:23<00:00, 161.17kB/s]
Wrote 33554432 bytes to D:/NEW.UF2
```

### Create a UF2 file from your asset binary

```
python uf2conv4eve.py --input __Flash.bin --convert
```

#### Output

```
Converting to uf2, output size: 33546240
Save as flash.uf2
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 32760/32760 [00:00<00:00, 337427.98kB/s]
Wrote 33546240 bytes to flash.uf2
```

### Help

```
python uf2conv4eve.py --help
```

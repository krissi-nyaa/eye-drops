# eye-drops
Data extraction using high-speed QR codes and cameras for the link layer! Got a file you can't get out? Physical security low but network locked down and local system encrypted? Use your screen and a highspeed camera to save and transfer files, or ball hard and bring a laptop and camera.

# Example

*On the tx system*
```bash
python file_to_qrs.py your_file_to_transfer
```

*on the rx system*
```bash
python qrs_to_file.py file_to_create
```

## Current functionality
- Can transfer utf-8 friendly files over a qr-code gif
- Can now transfer anything! ... small!

## Caveats
- Believe it or not, screen savers...
  - Tested on an OLED monitor for a longer file transfer, came back to a new interpretation of packet drop

## TODO: 
- ~~MAKE IT WORK FOR BYTES!!! Encoding is currently fudged because i bought into QReader, which is amazingly fast... but the encoding used is hard-coded into there and doesn't work for anything but transferring text files.~~
  - So ya, not the best solution but base64 solves everything usually... Also adds 33% payload overhead as an added bonus!
- ~~Take the training wheels off the QR codes (currently capped at 1000 bytes per code)~~
  - We are fairly maxed at version 40 QR codes. With the base64 overhead we're getting a really lame 1.5KB / QR
  - With a bad camera like mine, ~350KB of data will take 4.27 minutes to transfer (assuming 1s per QR code)
- Investigate dropping QR standards and building something custom with better visual-space data compression for this
- Finalize qrs_to_file tool and move the duct tape to qr_get
- Currently the rx tool just waits 60s then dies, should have some sort of 'start capture' and 'end capture' feature
- Take out all the horrible print functions
- Add sequencing and error-checking headers
- Once above is done, loop the jiff
- Expand this into a IPoQR POC - See what horrible throughput we can get with two cameras and two screens talking to each other using virtual interfaces

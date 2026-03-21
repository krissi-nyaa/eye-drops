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

## TODO: 
- MAKE IT WORK FOR BYTES!!! Encoding is currently fudged because i bought into QReader, which is amazingly fast... but the encoding used is hard-coded into there and doesn't work for anything but transferring text files.
- Take the training wheels off the QR codes (currently capped at 1000 bytes per code)
- Finalize qrs_to_file tool and move the duct tape to qr_get
- Currently the rx tool just waits 60s then dies, should have some sort of 'start capture' and 'end capture' feature
- Take out all the horrible print functions
- Add sequencing and error-checking headers
- Once above is done, loop the jiff
- Expand this into a IPoQR POC - See what horrible throughput we can get with two cameras and two screens talking to each other using virtual interfaces

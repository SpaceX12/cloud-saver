import dropbox
import os

class TransferFiles :
    def __init__(self, aT):
        self.aT = aT

    def uploadFiles(self, fF, fT):
        dbx = dropbox.Dropbox(self.aT)
        r = open(fF, 'rb')
        dbx.files_upload(r.read(), fT)


def main():
    acToken = 'wuEivkyQg0MAAAAAAAAAAXjb4h0trKMNmrZY7yFChKSfsk-ULePKf6APIOF1md5l'
    fileF = input('Where to transfer from:')

    if os.path.exists(fileF):
        for root_fol, folders, files in os.walk(fileF):
            rel_path= os.path.join(root_fol, fileF)

    fileT = '/saves/' + str(rel_path)
    trans = TransferFiles(acToken)
    trans.uploadFiles(fileF, fileT)

    print('Done')

main()


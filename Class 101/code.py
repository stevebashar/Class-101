from os import access
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

        def upload_file(self, file_from, file_to):
            
            dbx = dropbox.Dropbox(self.access_token)
            f = open(file_from, 'rb') 
            dbx.files_upload(f.read(), file_to)
            
def main():
    access_token = 'sl.BGB5_RtrA7yx4M-_HZRnmP-bxjT7fi1lk9Zt0_u8VU2gWnwA_TQT4WjucEDMXGjTTXJhUz-ZDFMoevWkG7Sz5BlI3awMpH0PRMr2F-RgRYqOwPDbLIKfE_LmScTQBbwX__pa-L0'
    transferData = TransferData(access_token)

    file_from = input('Enter the file map to transfer: ')
    file_to = input('Enter the full path of the file to upload to dropbox: ')

    transferData.upload_file(file_from, file_to)
    print("file has been moved.")

main()
import dropbox;

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():

    access_token = 'sl.AuU9ZnBEb8qENbu3He5gdyAfMXOps-RS0GnhIDzF888PqYRk4opRquvJbduFy3MGyWPXid6gVtYrxjJQAa9A9M2NZeRD_649xVbM0y8ukHylIIwVrdKHdOhgqzHxVB35pRSrExE'
    transferData = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/WhiteHatJunior_Uploads/Project-101 Folder upload/test.txt'

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()

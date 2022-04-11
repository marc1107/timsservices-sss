def main():
    for x in ('langeSeite', 'kurzeSeite'):
        #with open("/home/tim/Downloads/Versuch1/" + str(x) + ".csv", "r+") as f:
        with open("C:\\Users\\Rolan\\OneDrive\\Dokumente\\sss\\" + str(x) + ".csv", "r+") as f:
            text = f.read()
            f.seek(0)
            f.truncate()
            f.write(text.replace(',', '.'))

main()

import xml.etree.ElementTree as ET

class XML:
    xmlFile = None
    xmlObject = None
    root = None

    def __init__(self, xmlFile):
        self.xmlFile = xmlFile
        self.xmlObject = ET.parse(xmlFile)
        self.root = self.xmlObject.getroot()


    def SearchForTag(self, searchitem):

        for item in self.root.iter(searchitem):
            text = item.text
            #print(text)
        return text

if __name__ =='__main__':
    xml = XML('DBConnection.xml')
    xml.SearchForTag('database')

    xml.SearchForTag('host')
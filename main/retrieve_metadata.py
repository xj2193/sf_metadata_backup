from lxml import etree


def generate_xml_file(log_file_path, package_file_path):
    xml_name = []
    with open(log_file_path, "r") as file:
        for line in file:
            if 'XMLName' in line:
                xml_name.append(line[9:-1])
    top = etree.Element('{http://soap.sforce.com/2006/04/metadata}Package')
    for i in xml_name:
        types = etree.SubElement(top, 'types')
        members = etree.SubElement(types, 'members')
        name = etree.SubElement(types, 'name')
        members.text = '*'
        name.text = i
    version = etree.SubElement(top, 'version')
    version.text = '46.0'
    tree = etree.ElementTree(top)
    tree.write(package_file_path, pretty_print=True)


def main():
    log_file = r"C:\Program Files (x86)\apache-ant-1.9.14\salesforce_ant_46.0\aou_sf_ant\describeMetadata\describe.log"
    package_file = r'C:\Program Files (x86)\apache-ant-1.9.14\salesforce_ant_46.0\aou_sf_ant\retrieveOutput\package.xml'
    return generate_xml_file(log_file, package_file)


if __name__ == '__main__':
    main()

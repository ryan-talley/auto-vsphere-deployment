import sys
import xml.dom.minidom as md

ELEM_IDX = 0
EXIT_ERR = 1

# Arg1: OVF file path, Arg2: guestInfo file path, Arg3 output file path
try:
    ovf_path = sys.argv[1]
    ins_path = sys.argv[2]
    out_path = sys.argv[3]
except IndexError as e:
    print "Usage: python generate_ova_guestinfo.py <input-ovf-path> " + \
        "<input-xml-path> <output-ovf-path>"
    sys.exit(EXIT_ERR)

# Parse the ovf/xml documents on these paths
try:
    ovf_dom = md.parse(ovf_path)
    ins_dom = md.parse(ins_path)
except Exception as e:
    print "Parse file exception: {}".format(e.message)
    sys.exit(EXIT_ERR)

# Get the elements that need to be edited from the documents
try:
    vh_elem = ovf_dom.getElementsByTagName('VirtualHardwareSection')[ELEM_IDX]
    vs_elem = ovf_dom.getElementsByTagName('VirtualSystem')[ELEM_IDX]
    ps_elem = ins_dom.getElementsByTagName('ProductSection')[ELEM_IDX]
except IndexError as e:
    print "Element missing exeption: {}".format(e.message)
    sys.exit(EXIT_ERR)

# Set attribute in the VirtualHardwareSection in the OVF
vh_elem.setAttribute('ovf:transport', 'iso')

# Inject ProductSection into the VirtualSystem in the OVF
vs_elem.appendChild(ps_elem)

# Write the modified OVF to the output file
with open(out_path, 'w') as fd:
    ovf_dom.writexml(fd)

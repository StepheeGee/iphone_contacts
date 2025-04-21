# contacts/utils.py

import vobject
import pandas as pd

def parse_vcf_to_xls(vcf_file, output_path):
    contacts = []

    vcard_data = vcf_file.read().decode('utf-8')

    for vcard in vobject.readComponents(vcard_data):
        contact = {}
        contact['Full Name'] = getattr(vcard, 'fn', None).value if hasattr(vcard, 'fn') else ''
        contact['Phone'] = ''
        contact['Email'] = ''

        if hasattr(vcard, 'tel_list'):
            contact['Phone'] = ', '.join(tel.value for tel in vcard.tel_list)

        if hasattr(vcard, 'email_list'):
            contact['Email'] = ', '.join(email.value for email in vcard.email_list)

        contacts.append(contact)

    df = pd.DataFrame(contacts)
    df.to_excel(output_path, index=False)
    print(f"Contacts have been successfully parsed and saved to {output_path}")
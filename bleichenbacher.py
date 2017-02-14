from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from roots import *
import sys

message1 = "cis331+engelju+5.00"

message = sys.argv[1]

pubkey = """-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEA/eR8aHozuAhH22kyj0MD
Sq7Ljupvho3qJFOEpgAD3AFj58pPzXJRd2vEIAUy49dhM+5Dv2x0GTBPHNMOyCJd
F/lzG0AbYqMmtpcdswrj13Vq+SOGT3o/ulnHWt8GTS6sFFtmC9GgzT4mXUwzTkpl
f6vbM715qBlPQifiqahFUgoq9bmhc1+i0WNNt6rINABB74lOlCKNBvhnGH3apgRr
sdu+eI6+DsGPipRUL3ghP8wg6+Dbl5iH+tsgaaYpLQNaW8frD692PCYtH/6ghSRu
4ipKPOvBlRfXyWeq+rLcrAMsNcczwLPdBG1SiVrM+woh935baPDRpv0dAzlIhsfw
6wIBAw==
-----END PUBLIC KEY-----"""

pad = "" #fix this
asn1 = "3021300906052B0E03021A05000414"
sha = SHA.new(message).hexdigest()



# main testing
pk = RSA.importKey(pubkey)


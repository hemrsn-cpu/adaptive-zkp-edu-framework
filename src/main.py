import json
import datetime

class AdaptiveVerifier:
    def __init__(self):
        self.db = self._load_mock_db()

    def _load_mock_db(self):
        with open('src/database_mock.json', 'r') as f:
            return json.load(f)

    def verify_credential(self, subject_id, threshold, verifier_type):
        subject = next((s for s in self.db['students'] if s['id'] == subject_id), None)
        if not subject: return {"status": "error", "message": "Record not found."}
        if verifier_type == "external_verifier":
            return {"verification_mode": "Zero-Knowledge Proof (ZKP)", "authority": "Model Academic Institution", "is_qualified": subject['gpa'] >= threshold, "timestamp": str(datetime.datetime.now())}
        return {"verification_mode": "Administrative", "authority": "Model Academic Institution", "record": subject, "timestamp": str(datetime.datetime.now())}
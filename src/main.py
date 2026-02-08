import json
import datetime

# Load Database
def load_mock_db():
    try:
        with open('src/database_mock.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # Fallback if file not found in some environments
        return {"students": [{"id": "TEST", "gpa": 4.00}]}

class AdaptiveVerifier:
    def __init__(self):
        self.db = load_mock_db()
        print("✅ Database Connection Established.")

    def verify_degree_claim(self, student_id, claim_gpa_threshold, requester_role):
        """
        Complex Logic: Check if student GPA > threshold WITHOUT revealing actual GPA.
        This simulates a Range Proof (ZKP).
        """
        student = next((s for s in self.db['students'] if s['id'] == student_id), None)
        
        if not student:
            return {"error": "Student not found"}

        actual_gpa = student['gpa']
        
        # Decision Engine
        if requester_role == "employer":
            # ZKP Mode: Return only True/False, hide actual GPA
            is_valid = actual_gpa >= claim_gpa_threshold
            return {
                "verification_mode": "Zero-Knowledge Proof",
                "proof_valid": is_valid,
                "message": f"Student GPA is >= {claim_gpa_threshold}",
                "revealed_data": None  # <--- PRIVACY PRESERVED
            }
        else:
            # Standard Mode
            return {
                "verification_mode": "Standard",
                "actual_gpa": actual_gpa,
                "transcript": student
            }

if __name__ == "__main__":
    system = AdaptiveVerifier()
    
    print("\n--- TEST CASE 1: Employer checking GPA > 3.0 ---")
    # Employer should NOT see the actual GPA (3.85), only the result
    print(system.verify_degree_claim("STU-66001", 3.0, "employer"))
    
    print("\n--- TEST CASE 2: University Admin checking records ---")
    # Admin sees everything
    print(system.verify_degree_claim("STU-66001", 3.0, "university_admin"))

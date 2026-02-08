# System Architecture

## 🧩 High-Level Workflow
This diagram illustrates the **Adaptive ZKP Process** for educational credential verification.

```mermaid
graph TD
    User([🎓 Student / Holder]) -->|1. Request Credential| Issuer([🏛️ University / Issuer])
    Issuer -->|2. Issue Verifiable Credential| User
    
    User -->|3. Select Privacy Level| Adapter{⚙️ Adaptive Engine}
    
    Adapter -->|Low Cost / Public| MethodA[Standard Verification]
    Adapter -->|High Privacy / ZKP| MethodB[Zero-Knowledge Proof]
    
    MethodB -->|4. Generate Proof| Verifier([🏢 Employer / Verifier])
    MethodA -->|4. Show Certificate| Verifier
    
    Verifier -->|5. Verify Validity| Result{✅ Valid?}
    🔍 Component Roles
Issuer (University): Signs and issues the degree on the blockchain/database.

Holder (Student): Owns the data and decides how much to reveal.

Adaptive Engine: The core logic that calculates the trade-off between privacy needs and verification cost.

Verifier (Employer): Checks the proof without needing to see the raw grades/transcript.

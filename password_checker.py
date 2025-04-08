import re

# List of some common passwords that should be rejected
COMMON_PASSWORDS = {
    'password123', 'Password123', '12345678', 'qwerty123',
    'abc123', '123456789', 'password1', 'admin123',
    '1234567890', 'letmein123', 'welcome123', '111111',
    'password', 'admin', 'qwerty', 'welcome'
}

def check_password_strength(password):
    """Check password strength against security criteria including common password check"""
    analysis = {
        'length': len(password) >= 8,
        'upper': bool(re.search(r'[A-Z]', password)),
        'lower': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
        'not_common': password not in COMMON_PASSWORDS
    }
    
    score = sum(analysis.values())
    
    # Common password check is critical - if it fails, password can't be strong
    if not analysis['not_common']:
        return "Weak (Common Password)", analysis
    
    if score == 6:  # All criteria including not being a common password
        return "Very Strong", analysis
    elif score >= 5:
        return "Strong", analysis
    elif score >= 4:
        return "Moderate", analysis
    else:
        return "Weak", analysis

def main():
    print("Password Complexity Checker")
    password = input("\nEnter password to analyze: ")
    
    strength, analysis = check_password_strength(password)
    
    print(f"\nStrength: {strength}")
    print("\nDetailed Analysis:")
    print(f"- Length ≥8 characters: {'✓' if analysis['length'] else '✗'}")
    print(f"- Contains uppercase: {'✓' if analysis['upper'] else '✗'}")
    print(f"- Contains lowercase: {'✓' if analysis['lower'] else '✗'}")
    print(f"- Contains numbers: {'✓' if analysis['digit'] else '✗'}")
    print(f"- Contains special chars: {'✓' if analysis['special'] else '✗'}")
    print(f"- Not a common password: {'✓' if analysis['not_common'] else '✗'}")

if __name__ == "__main__":
    main()
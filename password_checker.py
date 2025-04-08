import re

def check_password_strength(password):
    """Check password strength against 5 criteria"""
    analysis = {
        'length': len(password) >= 8,
        'upper': bool(re.search(r'[A-Z]', password)),
        'lower': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    score = sum(analysis.values())
    
    if score == 5:
        return "Very Strong", analysis
    elif score >= 4:
        return "Strong", analysis
    elif score >= 3:
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

if __name__ == "__main__":
    main()
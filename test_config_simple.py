print("1. Starting simple test...")

try:
    print("2. Importing os...")
    import os
    print("3. OS imported successfully")
    
    print("4. Importing Path...")
    from pathlib import Path
    print("5. Path imported successfully")
    
    print("6. Creating PROJECT_ROOT...")
    PROJECT_ROOT = Path(__file__).parent.parent.parent
    print(f"7. PROJECT_ROOT: {PROJECT_ROOT}")
    
    print("8. Trying to import dotenv...")
    from dotenv import load_dotenv
    print("9. dotenv imported successfully")
    
    print("10. Loading .env...")
    env_path = PROJECT_ROOT / '.env'
    if env_path.exists():
        load_dotenv(env_path)
        print(f"11. ✅ Loaded .env from {env_path}")
    else:
        print(f"11. ⚠️  No .env file found at {env_path}")
    
    print("12. SUCCESS - Config loaded without issues!")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()

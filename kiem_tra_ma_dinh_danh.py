def check_crystal_id(code_str):
    parts = code_str.split('.')
    
    if len(parts) != 4:
        return "NO"
    
    for part in parts:
        if not part.isdigit():
            return "NO"
        if len(part)>1 and part.startswith('0'):
            return "NO"
        
        value = int(part)
        if not (0<= value <=255):
            return "NO"
            
    return "YES"

def solve():
    try:
        line = input().strip()
        if not line: return
        t = int(line)
        
        for _ in range(t):
            s = input().strip()
            print(check_crystal_id(s))
            
    except ValueError:
        return
    except EOFError:
        return

if __name__ == "__main__":
    solve()
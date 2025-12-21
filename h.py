import sys
def solve():
    input_data=sys.stdin.read().splitlines()

    if not input_data:
        return
    
    lines=input_data[1:]
    
    current_topic=None
    count=0
    results=[]

    for line in lines:
        line=line.strip()

        if ' ' not in line:
            if current_topic is not None:
                print(f"{current_topic}:{count}")

            current_topic=line
            count=0
        else:
            count+=1
        
    if current_topic is not None:
        results.append(f"{current_topic}: {count}")
    
    for r in results:
        print(r)

if __name__ == '__main__':
    solve()
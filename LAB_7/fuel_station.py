def parse_purchase(text):
    if text is None or not isinstance(text, str):
        return ("Unknown", 0.0)
    if ":" not in text:
        return (text.strip().title() if text.strip() else "Unknown", 0.0)
    
    parts = text.split(":", 1)
    grade = parts[0].strip().title() or "Unknown"
    
    try:
        litres = float(parts[1].strip())
    except ValueError:
        litres = 0.0
        
    return grade, max(litres, 0.0)


def volume_average(volumes_csv):
    if volumes_csv is None or not isinstance(volumes_csv, str):
        return 0
    
    values = []
    for r in volumes_csv.split(","):
        r_clean = r.strip()
        if r_clean:
            try:
                values.append(int(r_clean))
            except ValueError:
                continue
                
    if not values:
        return 0
        
    return sum(values) // len(values)


def payable_bill(text):
    if text is None or not isinstance(text, str):
        return 0.0
    
    if "|" not in text:
        try:
            bill = float(text.strip())
            return max(bill * 1.18, 0.0)
        except ValueError:
            return 0.0
            
    parts = text.split("|", 1)
    try:
        bill = float(parts[0].strip())
    except ValueError:
        bill = 0.0
        
    try:
        discount = float(parts[1].strip())
    except ValueError:
        discount = 0.0
        
    total = bill * 1.18 - discount
    return max(total, 0.0)


def main():
    print("==== Running parse_purchase ====")
    user_input = input("Enter grade:litres (e.g. diesel:25): ")
    result = parse_purchase(user_input)
    print("Grade and Litres:", result)

    print("\n==== Running volume_average ====")
    user_input = input("Enter pump volumes in litres as CSV (e.g. 10,25,40): ")
    result = volume_average(user_input)
    print("Average Volume:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 2500|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)


if __name__ == "__main__":
    main()

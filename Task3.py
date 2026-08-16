services = {
    "Auth": "200 OK",
    "Cache": "500 Error",
    "Database": "200 OK",
    "Proxy": "404 Not Found"
}

print("\nTask 3 - API Response Validator")

for service, status in services.items():
    print(f"Checking {service}: {status}")

    if "200" in status:
        print(f"{service}: Service Healthy")
    else:
        print(f"{service}: Service Critical")
        continue
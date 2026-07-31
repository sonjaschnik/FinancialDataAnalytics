import requests

reports = {
    "2025": "https://impact.disney.com/app/uploads/2026/05/2025-Sustainability-Social-Impact-Report-2.pdf",
    "2024": "https://impact.disney.com/resources/2024-ssi-report/",
    "2023": "https://impact.disney.com/resources/2023-ssi-report/",
    "2022": "https://impact.disney.com/resources/2022-csr-report/",
    "2021": "https://impact.disney.com/resources/2021-csr-report/"
}

for year, url in reports.items():
    response = requests.get(url)
    filename = f"disney_esg_{year}.pdf"
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename}")
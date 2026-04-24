from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import httpx
import os
import json

load_dotenv()
mcp = FastMCP("jobs")

USER_AGENT = "Mozilla/5.0 (compatible; JobSearchBot/1.0)"
SERPER_URL = "https://google.serper.dev/search"

job_site_urls = {
    "indeed": "https://nl.indeed.com/"
}

def search_web(query: str) -> dict | None:
    payload = json.dumps({"q":query, "num":2})

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }

    with httpx.Client() as client:
        try:
            response = client.post(
                SERPER_URL, headers=headers, data=payload, timeout=2.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}


def fetch_url(url:str):
    headers = {"User-Agent": USER_AGENT}
    with httpx.Client() as client:
        try:
            response = client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            return text[:1000]
        except httpx.TimeoutException:
            return "Timeout error"
        except Exception as e:
            return f"Error fetching URL: {str(e)}"


@mcp.tool()
def search_jobs(
    job_title: str,
    location: str = "Netherlands",
    site: str = "indeed",
    keywords: str = "",
    min_salary: int | None = None,
    currency: str = "EUR"
) -> str:
    """
    Search the web for jobs matching a given title and criteria.
    Supports Indeed and LinkedIn Netherlands.

    Args:
        job_title: The job title to search for (e.g. "Python Developer")
        location: The location to search in (e.g. "Amsterdam")
        site: The job site to search on — "indeed" or "linkedin"
        keywords: Optional extra keywords to filter by (e.g. "remote, senior, fintech")
        min_salary: Minimum salary to filter by (e.g. 60000)
        currency: Currency for the salary (default "EUR")

    Returns:
        Text content from job listing pages matching the search.
    """

    if site not in job_site_urls:
        raise ValueError(f"Site '{site}' not supported. Choose from: {list(job_site_urls.keys())}")

    query = f"site:{job_site_urls[site]} {job_title} {location}"
    if keywords:
        query += f" {keywords}"
    if min_salary:
        query += f" salary {min_salary} {currency}"

    results = search_web(query)

    if not results.get("organic"):
        return "No job listings found."

    text = ""
    for result in results["organic"]:
        url = result.get("link", "")
        snippet = result.get("snippet", "")
        title = result.get("title", "")

        text += f"\n\n--- {title} ---\n{url}\n{snippet}\n"
        text += fetch_url(url)

    return text if text.strip() else "No job details could be retrieved."


if __name__ == "__main__":
    mcp.run(transport="stdio")
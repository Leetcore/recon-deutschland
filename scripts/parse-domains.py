from urllib.parse import urlparse

with open("unis-wiki.txt", "r") as f:
    output: list[str] = []
    for line in f.readlines():
        url_parts = urlparse(line.strip())
        domain = url_parts.netloc
        if domain:
            output.append(domain)
            print(domain)
        else:
            print(line)

with open("unis-wiki-domain.txt", "w") as f:
    f.write("\n".join(output))
